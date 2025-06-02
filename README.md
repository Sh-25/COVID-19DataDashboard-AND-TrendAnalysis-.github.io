#  COVID-19 Data Dashboard & Trend Analysis

**Visualizing Pandemic Trends and Metrics**
**Author:** Shruti Badagandi
**Year:** 2025

## 📌 Overview

This project analyzes and visualizes global COVID-19 data to uncover trends, assess country-level responses, and predict outcomes. It integrates multiple tools — Python and Power BI — for a comprehensive, interactive experience. Key pandemic metrics like confirmed cases, deaths, recoveries, vaccinations, and testing rates are explored through statistical analysis and dynamic dashboards.

## 🔧 Tools & Technologies

* **Python**

  * Used for data cleaning, visualization, and modeling
  * Libraries: `pandas`, `matplotlib`, `seaborn`, `scikit-learn`

* **Power BI**

  * Used for building an interactive and filterable dashboard

* **Platform**: Visual Studio Code

* **Data Source**: `COVID-19 Dataset.csv` (structured time-series data from 190+ countries)

## 📊 Key Features

### 1. **Data Preprocessing**

* Cleaned, casted, and handled missing values using `pandas`
* Converted date columns for time-series aggregation

### 2. **Trend Analysis**

* **Confirmed, Recovered, and Death Cases**:
  Daily global trends analyzed and visualized using scatter plots
* **Vaccination Progress**:
  Top 10 countries with the highest number of fully vaccinated individuals
* **Top 5 Affected Countries**:
  Pie chart of countries with the most confirmed cases
* **Death Rate Analysis**:
  Bar chart highlighting countries with the highest death rate

### 3. **Predictive Modeling**

* **Model**: Linear Regression
* **Goal**: Predict COVID-19 death counts based on confirmed case numbers
* **Performance**:

  * Intercept: `-1910.20`
  * Coefficient: `0.0257`
  * R² Score: `0.398`
  * MAE: `~30,533`
  * MSE: `1.65 billion`
* **Visualization**: Actual vs Predicted death counts via scatter plot

### 4. **Interactive Dashboard (Power BI)**

* Dynamic filters by country and date
* Visual summary of key metrics including:

  * Case progression
  * Deaths
  * Recoveries
  * Testing rates
  * Vaccination statistics

## 📈 Insights & Observations

* Seasonal trends (winter, monsoon) in 2025 show renewed spikes in cases
* Recovery and death trends reflect better global response over time
* Vaccine rollouts have significantly reduced severity and fatality rates
* High-risk individuals (older adults, immunocompromised) remain vulnerable
* Preventative measures like masking, hygiene, and boosters are still crucial

## 📁 Project Files

* `COVID-19 Dataset.csv` — Primary dataset
* `COVID-19.py` — Python script for trend analysis and modeling
* `Dashboard.pbix` — Power BI dashboard file
* `COVID-19 Data Dashboard and Trend Analysis-.pdf` — Report
* `COVID-19 Data Dashboard and Trend Analysis-.pptx` — Presentation slides

## ✅ How to Run

1. Clone the repository or download the files.
2. Ensure Python 3 and required libraries are installed.
3. Run `COVID-19.py` in a Python environment.
4. Open `Dashboard.pbix` in Power BI Desktop to explore interactive visuals.

