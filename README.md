🌍 Global Temperature Analysis using Apache Spark

A Big Data Analytics project for identifying long-term climate trends, anomalies, and forecasting using distributed computation.

📌 Overview

This project analyzes 160+ years of historical global temperature data using Apache Spark to uncover long-term climate patterns, detect anomalies, and forecast future temperature behavior.

The work includes:

Data preparation

Distributed Spark analytics

Trend and anomaly computation

Machine learning forecasting

Power BI visualization

A research paper based on this analysis is currently under preparation.

🛠️ Tech Stack
Big Data Processing

Apache Spark (PySpark)

Spark SQL

Distributed DataFrame API

Machine Learning

Random Forest Regressor

Linear Regression

Z-Score anomaly detection

Visualization

Power BI

Matplotlib

Programming / Tools

Python

Jupyter + PySpark Shell

📂 Dataset Summary
Dataset Name	Rows	Columns	Date Range	Description
GlobalLandTemperaturesByCountry	577,462	4	1743–2013	Country-level temperatures
GlobalLandTemperaturesByState	645,000+	4	1850–2013	State-level temperatures
GlobalLandTemperaturesByMajorCity	239,177	7	1743–2013	Major city temperatures
GlobalTemperatures	3,192	9	1750–2015	Global monthly temperatures
Final Enriched Dataset	233,506	11	1850–2013	Unified dataset for modeling
🔍 Methodology
1️⃣ Data Cleaning & Preprocessing

Removed missing or invalid entries

Standardized date formats

Extracted features (year, decade, season)

Merged datasets with location hierarchy

Generated enriched ML-ready dataset

2️⃣ Distributed Trend Analysis (PySpark)

Global long-term trend analysis

Country and state-level warming evaluation

Seasonal and decadal variations

City-level temperature pattern tracking

3️⃣ Anomaly Detection (Z-Score)
z = (x - μ) / σ


Cities with |z| > 2.5 were marked as temperature anomalies.

4️⃣ Machine Learning Forecasting

A Random Forest model was trained using:

Latitude & longitude

Historical averages

Seasonal indicators

Trend features

5️⃣ Visualization

Power BI dashboards display:

Temperature trends

Anomaly distributions

Forecast curves

Geographic comparisons

📊 Results
Global Temperature Trend

Clear warming trend since the 1850s

Sharp acceleration after 1950

Global temperature increased by ~11.8°C across dataset coverage

Top 10 Anomalous Cities (Z-Score)
City	Mean Temp (°C)	Z-Score	Notes
Surabaya	28.7	3.87	Highest anomaly
Nagpur	26.9	3.42	Heat events
Bangkok	27.4	3.11	Seasonal instability
Delhi	29.1	3.05	Urban heat island
Cairo	28.2	2.97	Rapid warming
Mumbai	27.8	2.88	High humidity effect
Dhaka	27.6	2.77	Monsoon variability
Karachi	28.3	2.65	Extreme summer peaks
Manila	27.1	2.61	Tropical anomaly
Singapore	27.9	2.55	Coastal warming
Machine Learning Model Performance
Model	RMSE	MAE	R²
Linear Regression	3.6998	2.8288	0.8583
Random Forest	0.9637	0.6916	0.9904

Random Forest achieved near-perfect predictive accuracy.

Forecast Results

Maximum predicted future temperature: ~34.9°C

Temperature distribution is right-skewed, indicating more frequent extreme heat events

📈 Power BI Dashboard

This project includes:

Global and national trend pages

Seasonal and annual analysis

City anomaly detection visualization

Forecast dashboard

Screenshots can be added to visualizations/ folder.

📁 Project Structure
GlobalTemperatureAnalysis/
│── scripts/
│   └── temperature_analysis.py
│── notebooks/
│── data/
│── outputs/
│── visualizations/
│── powerbi-dashboard/
│── README.md

▶️ Running the Project
Start PySpark
pyspark --master local[*]

Run Analysis Script
python temperature_analysis.py

Export Results for Dashboard
df_final.toPandas().to_csv("processed_temperature.csv", index=False)

📝 References

The analysis follows the academic structure and dataset references included in the project report.

👨‍💻 Author

Utsav Chatterjee
BTech in Artificial Intelligence & Data Science
REVA University
