import pandas as pd
import matplotlib.pyplot as plt

# Load data - .csv lagana zaruri hai
df = pd.read_csv('Delhi_aqi_winter_2025_2026.csv')
df['date'] = pd.to_datetime(df['date'])

print(f"Peak AQI: {df['AQI'].max()}")
print(f"Traffic vs AQI Correlation: {df['traffic_volume'].corr(df['AQI']):.2f}")

# Chart 1
plt.figure(figsize=(10,5))
plt.plot(df['date'], df['AQI'], marker='o', color='crimson')
plt.title('Delhi AQI Trend Winter 2025-26')
plt.xticks(rotation=45)
plt.ylabel('AQI')
plt.tight_layout()
plt.savefig('aqi_trend.png')
plt.show()

# Chart 2
plt.figure(figsize=(8,5))
plt.scatter(df['traffic_volume'], df['AQI'], color='royalblue')
plt.title('Traffic vs AQI')
plt.xlabel('Traffic Volume')
plt.ylabel('AQI')
plt.tight_layout()
plt.savefig('traffic_vs_aqi.png')
plt.show()
