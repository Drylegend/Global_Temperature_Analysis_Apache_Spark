🌍 Global Temperature Analysis using Apache Spark

A Big Data Analytics project for understanding long-term climate trends, anomalies, and forecasts.

📌 Overview

This project analyzes more than 170 years of global, national, and regional temperature data using PySpark, distributed computation, and machine-learning forecasting. The pipeline integrates multiple historical climate datasets into an enriched, multi-scale analytical model covering:

Global temperature trends

Country-level temperature patterns

State-level warming dynamics

City-level anomaly detection

Forecasting future temperature behavior

The results show a persistent rise in global average temperature since the mid-19th century, with accelerated warming after the mid-20th century. A supervised ML model is used to predict future temperature trajectories, achieving high accuracy (R² ≈ 0.99).

This work demonstrates a complete big-data workflow—from ingestion and cleansing to distributed analytics, forecasting, and visualization.

🛠️ Tech Stack
Big Data Processing

Apache Spark (PySpark)

Spark SQL

Distributed DataFrame operations

Machine Learning

Random Forest Regressor

Linear Regression

Statistical anomaly detection (z-score)

Visualization

Power BI

Matplotlib

Languages / Tools

Python

Jupyter / PySpark Shell

📂 Dataset Summary

Merged from multiple Kaggle/NASA/global archives:

Dataset Name	Rows	Columns	Date Range	Description
GlobalLandTemperaturesByCountry	577,462	4	1743–2013	Country-level temps
GlobalLandTemperaturesByState	645,000+	4	1850–2013	State-level temps
GlobalLandTemperaturesByMajorCity	239,177	7	1743–2013	Major-city temps
GlobalTemperatures	3,192	9	1750–2015	Global monthly temps
Final Enriched Dataset	233,506	11	1850–2013	Unified dataset for modeling

Dataset preparation included:

Cleaning missing/invalid temperature values

Standardizing date formats

Extracting year, season, and multi-decade windows

Merging global, country, state, and city datasets

Generating enriched features for ML

🔍 Methodology

This project follows a multi-stage pipeline:

1️⃣ Data Cleaning & Preprocessing

Remove invalid temperature entries

Resolve mismatched geographic labels

Aggregate by year, season, and decades

Compute long-term averages for stability

Merge datasets for unified analysis

2️⃣ Distributed Trend Analysis (PySpark)

Using Spark SQL & DataFrames to compute:

Yearly and seasonal temperature trends

50-year period analysis

Geographic variation

State- and city-specific warming behavior

3️⃣ Anomaly Detection (Z-Score Method)

A z-score was used to detect statistically unusual temperatures:

z = (x − μ) / σ


Cities with z-scores > 2.5 were flagged as anomalous.

4️⃣ Machine Learning Forecasting

A Random Forest Regressor was trained using:

Latitude, longitude

Historical temperature averages

Seasonal indicators

Trend features

5️⃣ Visualization

Final outputs were exported to Power BI dashboards showing:

Global warming trends

Country and state comparisons

City anomaly rankings

Prediction distributions

📊 Results
Global Temperature Trend

Global average temperature increased by ~11.8°C from earliest records to the present dataset endpoint.

Significant acceleration after 1950 correlates with increased industrial emissions.

City-Level Anomalies (Top 10)
City	Mean Temp (°C)	Z-Score	Notes
Surabaya	28.7	3.87	Highest anomaly
Nagpur	26.9	3.42	Strong heat events
Bangkok	27.4	3.11	Seasonal instability
Delhi	29.1	3.05	Urban heat island
Cairo	28.2	2.97	Persistent warming
Mumbai	27.8	2.88	Humidity amplification
Dhaka	27.6	2.77	Monsoon variability
Karachi	28.3	2.65	Extreme summer peaks
Manila	27.1	2.61	Tropical anomalies
Singapore	27.9	2.55	Coastal warming
Machine Learning Model Performance
Model	RMSE	MAE	R²
Linear Regression	3.6998	2.8288	0.8583
Random Forest	0.9637	0.6916	0.9904

Random Forest achieved near-perfect predictive accuracy (R² ≈ 0.99).

Forecast

Maximum future projected temperature ≈ 34.9°C

Predictions show right-skewed distribution, meaning extreme heat events will become more frequent.

📌 Key Insights

Global warming is consistent, measurable, and accelerating.

Regional differences are significant—urban areas show strong heat anomalies.

State-level warming in India highlights Delhi, TN, and AP as high-risk zones.

ML forecasting strongly supports continuation of warming trends.

📈 Power BI Dashboard

This project includes a multi-page Power BI dashboard with:

Global trends

Country comparisons

City-level anomaly scoring

Forecast visualizations

📁 Project Structure
/GlobalTemperatureAnalysis
│── notebooks/
│── scripts/
│   └── temperature_analysis.py
│── data/
│── output/
│── visualizations/
│── powerbi-dashboard/
│── README.md

▶️ Running the Project
Start PySpark
pyspark --master local[*]

Run Analysis Script
python temperature_analysis.py

Export for Visualization
df_final.toPandas().to_csv("processed_temperature.csv", index=False)

📝 References

References are consistent with the citations in the main report.


BDA_LAB_PROJECT

👨‍💻 Author

Utsav Chatterjee
BTech in AI & Data Science
REVA University
