# Avocado Price Prediction Project

This project implements a machine learning solution to predict avocado prices using historical data. The implementation follows the CRISP-DM methodology and includes comprehensive analysis, model development, and evaluation.

## Project Structure

```
├── README.md
├── requirements.txt
├── getweatherdata.py                                   # script to get weather data
├── avocado2015to2022withweather.csv                    # dataset for train/test
├── avocadoafter2023withweather.csv                     # for prediction after 2023
├── notebooks/
│   ├── 1_Business_Understanding.ipynb
│   ├── 2_Data_Understanding.ipynb
│   └── 3_Data_Preparation_Modeling_Evaluation.ipynb
├── forcastingReport/
│   └── forcasting_2023.csv                             # forcasting report for 2023   
```

## Setup Instructions

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start Jupyter Notebook:
```bash
jupyter notebook
```

### All documentation is in the notebooks folder. 
