import requests
import time
import csv
import os
from datetime import datetime
import pandas as pd
from geopy.geocoders import Nominatim

# API Configuration
API_HOST = "meteostat.p.rapidapi.com"
API_KEY = "37fa141feemsh532174c3a7fcc2cp1ea25ajsn347b84a8c7de"  # Replace with your actual API key

# List of US regions

regions = [
    "BuffaloRochester", "HarrisburgScranton", "PeoriaSpringfield", 
    "WestTexNewMexico", "NewOrleans", 
    "LasVegas", "SouthCarolina"
]
# Initialize geocoder
geolocator = Nominatim(user_agent="weather_data_collector")

# Output directory
output_dir = "weather_data"
os.makedirs(output_dir, exist_ok=True)

# Create a log file
log_file = os.path.join(output_dir, "log.txt")
with open(log_file, "w") as f:
    f.write(f"Weather data collection started at {datetime.now()}\n")

def get_coordinates(region_name):
    try:
        # Hard-coded coordinates for problematic regions
        hardcoded_coords = {
            # Combined city regions
            "BuffaloRochester": (42.8864, -78.8784),  # Buffalo
            "HarrisburgScranton": (40.2732, -76.8867),  # Harrisburg
            "PeoriaSpringfield": (40.6936, -89.5890),  # Peoria
            "WestTexNewMexico": (31.7619, -106.4850),  # El Paso (West Texas)
            "PhoenixTucson": (33.4484, -112.0740),  # Phoenix
            "NewOrleans": (29.9511, -90.0715),
            "HartfordSpringfield": (41.7658, -72.6734),  # Hartford
            "DallasFtWorth": (32.7767, -96.7970),  # Dallas
            "CincinnatiDayton": (39.1031, -84.5120),  # Cincinnati
            "RaleighGreensboro": (35.7796, -78.6382),  # Raleigh
            "RichmondNorfolk": (37.5407, -77.4360),  # Richmond
            "BirminghamMontgomery": (33.5186, -86.8104),  # Birmingham
            
            # One-word cities that need special handling
            "LasVegas": (36.1699, -115.1398),
            
            # States/regions
            "SouthCarolina": (34.0007, -81.0348),  # Columbia, SC
            "Northeast": (42.3601, -71.0589),  # Boston
            "Southeast": (33.7490, -84.3880),  # Atlanta
            "West": (37.7749, -122.4194),  # San Francisco
            "SouthCentral": (32.7767, -96.7970),  # Dallas
            "Plains": (41.2565, -95.9345),  # Omaha
            "GreatLakes": (41.8781, -87.6298),  # Chicago
            "NorthernNewEngland": (44.4759, -73.2121),  # Burlington, VT
            "California": (36.7783, -119.4179),  # Central California
            "Midsouth": (36.1627, -86.7816),  # Nashville
            "TotalUS": (39.8283, -98.5795),  # Geographic center of the US
        }
        
        # Check if region is in our hardcoded dictionary
        if region_name in hardcoded_coords:
            return hardcoded_coords[region_name]
            
        # For regions with two cities that aren't hardcoded, try to handle them
        if any(c.isupper() for c in region_name[1:]):
            # Find the first uppercase letter after the first character
            for i in range(1, len(region_name)):
                if region_name[i].isupper():
                    search_name = region_name[:i]
                    break
            else:
                search_name = region_name
        else:
            search_name = region_name
            
        # Add ", USA" to ensure we get US locations
        search_query = f"{search_name}, USA"
        
        # Try the geocoder
        location = geolocator.geocode(search_query)
        if location:
            return location.latitude, location.longitude
        
        # Fallback to a basic mapping for common cities
        fallback_coords = {
            "NewYork": (40.7128, -74.0060),
            "LosAngeles": (34.0522, -118.2437),
            "SanFrancisco": (37.7749, -122.4194),
            "Miami": (25.7617, -80.1918),
            "Chicago": (41.8781, -87.6298),
            "Houston": (29.7604, -95.3698),
            "Boston": (42.3601, -71.0589),
            "Atlanta": (33.7490, -84.3880),
            "Dallas": (32.7767, -96.7970),
            "Seattle": (47.6062, -122.3321)
        }
        
        for city, coords in fallback_coords.items():
            if city in region_name:
                return coords
                
        # Last resort: log error and return None
        with open(log_file, "a") as f:
            f.write(f"ERROR: Could not find coordinates for {region_name}\n")
        return None
        
    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"ERROR: Exception while finding coordinates for {region_name}: {str(e)}\n")
        return None

# Function to fetch weather data for a specific region and date range
def get_weather_data(region_name, start_date, end_date):
    coords = get_coordinates(region_name)
    if not coords:
        return None
    
    lat, lon = coords
    
    url = f"https://meteostat.p.rapidapi.com/point/daily"
    querystring = {"lat": lat, "lon": lon, "start": start_date, "end": end_date}
    
    headers = {
        "x-rapidapi-host": API_HOST,
        "x-rapidapi-key": API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            with open(log_file, "a") as f:
                f.write(f"ERROR: API request failed for {region_name} with status code {response.status_code}\n")
            return None
    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"ERROR: Exception during API request for {region_name}: {str(e)}\n")
        return None

# Process the data
def process_data():
    # Create a CSV file for all regions
    all_data_file = os.path.join(output_dir, "all_regions_weather_data.csv")
    with open(all_data_file, 'w', newline='') as csvfile:
        fieldnames = ['region', 'date', 'tavg', 'tmin', 'tmax', 'prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for region in regions:
            print(f"Processing {region}...")
            with open(log_file, "a") as f:
                f.write(f"Processing {region} at {datetime.now()}\n")
                
            # Process data year by year to avoid hitting API limits
            for year in range(2015, 2024):
                start_date = f"{year}-01-01"
                end_date = f"{year}-12-31"
                
                data = get_weather_data(region, start_date, end_date)
                if data and 'data' in data:
                    # Handle data['data'] as a list
                    for weather_entry in data['data']:
                        if 'date' in weather_entry:
                            row = {'region': region, 'date': weather_entry['date']}
                            # Remove the date key since we've already used it
                            weather_dict = {k: v for k, v in weather_entry.items() if k != 'date'}
                            row.update(weather_dict)
                            writer.writerow(row)
                        
                # Create individual region files as well
                region_file = os.path.join(output_dir, f"{region}_{year}_weather_data.csv")
                if data and 'data' in data:
                    df = pd.DataFrame(data['data'])
                    df['region'] = region
                    df.to_csv(region_file, index=False)
                    
                    with open(log_file, "a") as f:
                        f.write(f"Successfully saved data for {region} {year}\n")
                else:
                    with open(log_file, "a") as f:
                        f.write(f"No data available for {region} {year}\n")
                
                # Wait 5 seconds between requests
                time.sleep(5)

if __name__ == "__main__":
    process_data()
    print("Data collection complete. Check the 'weather_data' directory for CSV files.")