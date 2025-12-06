
Cities with **|z| > 2.5** were flagged as temperature anomalies.

### 4. Machine Learning Forecasting

Models trained:
- Linear Regression  
- Random Forest Regressor  

Features included:
- Latitude, longitude  
- Historical averages  
- Seasonal trends  
- Decadal patterns  

### 5. Visualization

Final datasets were exported to **Power BI** for:

- Global and country trends  
- City anomaly heatmaps  
- Forecast distributions  

---

## Results

### Global Temperature Trend
- Clear warming trend since mid-19th century  
- Accelerated temperature rise after 1950  
- Total increase ≈ **11.8°C** across dataset span  

---

### Top 10 Cities with Highest Temperature Anomalies (Z-Score)

| City      | Mean Temp (°C) | Z-Score |
|-----------|----------------|---------|
| Surabaya  | 28.7           | 3.87    |
| Nagpur    | 26.9           | 3.42    |
| Bangkok   | 27.4           | 3.11    |
| Delhi     | 29.1           | 3.05    |
| Cairo     | 28.2           | 2.97    |
| Mumbai    | 27.8           | 2.88    |
| Dhaka     | 27.6           | 2.77    |
| Karachi   | 28.3           | 2.65    |
| Manila    | 27.1           | 2.61    |
| Singapore | 27.9           | 2.55    |

---

### Machine Learning Model Performance

| Model              | RMSE   | MAE    | R²     |
|-------------------|--------|--------|--------|
| Linear Regression  | 3.6998 | 2.8288 | 0.8583 |
| **Random Forest**  | **0.9637** | **0.6916** | **0.9904** |

Random Forest achieved near-perfect predictive performance.

---

### Forecast Summary
- Maximum predicted future temperature: **~34.9°C**  
- Distribution is right-skewed → extreme heat events more likely  

---

GlobalTemperatureAnalysis/
│── scripts/
│ └── temperature_analysis.py
│── notebooks/
│── data/
│── outputs/
│── visualizations/
│── powerbi-dashboard/
│── README.md



---

## Running the Project

### Start PySpark
```bash
pyspark --master local[*]


## Run the Analysis Script
```
python temperature_analysis.py
```

## Export Results
```
df_final.toPandas().to_csv("processed_temperature.csv", index=False)
```

Author

Utsav Chatterjee
BTech in Artificial Intelligence & Data Science
REVA University

## Project Structure

