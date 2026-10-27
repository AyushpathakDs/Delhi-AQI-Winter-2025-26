import pandas as pd
import matplotlib.pyplot as plt

# Load data - teri file ka naam
df = pd.read_csv('Delhi_aqi_winter_2025_2026')

print(f"Peak AQI: {df['AQI'].max()}")
print(f"Traffic vs AQI Correlation: {df['traffic_volume'].corr(df['AQI']):.2f}")

# Chart 1
plt.figure()
plt.plot(df['date'], df['AQI'], marker='o')
plt.title('Delhi AQI Trend Winter 2025-26')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('aqi_trend.png')
plt.show()

# Chart 2
plt.figure()
plt.scatter(df['traffic_volume'], df['AQI'])
plt.title('Traffic vs AQI')
plt.xlabel('Traffic Volume')
plt.ylabel('AQI')
plt.savefig('traffic_vs_aqi.png')
plt.show()
