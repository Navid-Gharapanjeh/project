# Avocado Prices Forecasting

## 1. Business Understanding

### Short Description
Avocado prices fluctuate significantly each season, making it challenging for consumers and businesses to anticipate future costs. The goal of this project is to develop a machine learning model to accurately predict avocado prices for the upcoming months.

### Objective
- Develop a machine learning model that can predict avocado prices with high accuracy.
- Analyze extracted features and their correlation with avocado prices.
- Explore additional external factors (e.g., economic indicators, weather) that could improve model performance.
- Ensure thorough research and justification of all methodological decisions.

### Expected Deliverables
- A well-documented Jupyter Notebook with a structured CRISP-DM approach (excluding deployment).
- A fully reproducible environment setup to run the notebook.
- A bibliography using a standard citation format (IEEE, APA, etc.).
- Comprehensive justifications for design choices and trade-offs made during development.

---

## 2. Data Understanding

### Dataset Source
The dataset is sourced from Kaggle: [Avocado Prices Dataset](https://www.kaggle.com/datasets/neuromusic/avocado-prices/).

### Data Overview
The dataset contains weekly avocado sales and pricing data across multiple US regions, including:
- Date
- Average price per avocado
- Total volume sold
- Sales by type (conventional/organic)
- Regional and national sales breakdown

### Initial Exploratory Analysis
- Loaded dataset using Pandas.
- Renamed columns for clarity (e.g., 'Unnamed: 0' renamed to 'Id').
- Converted 'Date' column to datetime format.
- Checked for missing values and data inconsistencies.
- Visualized price trends over time and across regions.
- Conducted correlation analysis to understand relationships between features.
- Performed outlier detection to assess data anomalies.

---

## 3. Data Preparation

### Preprocessing Steps
- Handled missing values: Imputed or removed incomplete records as necessary.
- Feature engineering:
  - Extracted new temporal features from the 'Date' column (e.g., Year, Month, Week).
  - Created rolling averages to capture price trends.
  - Considered external economic indicators for potential feature augmentation.
- Data transformation: Normalization or scaling applied where necessary.
- Splitting the dataset:
  - Used time-series split instead of random train-test split to ensure chronological integrity.
  - Established a validation set to ensure robust model performance.

---

## 4. Modeling

### Model Selection
The following models were implemented and evaluated:
1. **Linear Regression** – Baseline model for capturing trends.
2. **Random Forest Regressor** – Non-linear model for capturing complex relationships.
3. **Gradient Boosting Regressor** – Evaluated to potentially improve performance beyond Random Forest.

### Model Training & Hyperparameter Tuning
- Used cross-validation to optimize model performance.
- Applied hyperparameter tuning for Random Forest and Gradient Boosting using GridSearchCV.
- Compared models based on multiple error metrics.

---

## 5. Evaluation

### Performance Metrics
- **Mean Absolute Error (MAE)** – Measures absolute differences.
- **Mean Squared Error (MSE)** – Penalizes larger errors.
- **R-squared Score** – Evaluates the proportion of variance explained.

### Model Comparison
- Linear Regression provided a basic benchmark.
- Random Forest Regressor showed improved accuracy by capturing non-linear trends.
- Gradient Boosting further refined predictions but required additional computation time.

### Statistical Analysis & Insights
- Evaluated feature importance to interpret key drivers of avocado prices.
- Conducted residual analysis to detect patterns in errors.
- Visualized model predictions against actual price trends to assess forecasting reliability.

---

## 6. Documentation & Submission

### Deliverables
- A Jupyter Notebook containing:
  - Detailed markdown explanations.
  - Well-structured and readable code.
  - Comprehensive data visualizations illustrating key insights.
  - Model evaluation and justifications for approach.
- A requirements file for easy environment setup.
- A bibliography for references and citations.
- Explanation of trade-offs made in model selection and feature engineering.

### Final Notes
- Ensured all external code is well-understood and properly cited.
- Prioritized clarity and explanation over achieving the highest model performance.
- Included thorough justifications and research to meet the highest rubric standards.
- Submitted before the deadline at the end of week 3.5.