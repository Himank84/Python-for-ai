import requests
import pandas as pd
from datetime import datetime, timedelta

import matplotlib.pyplot as plt

# Fetch weather data for Delhi from Open-Meteo API (free, no key required)
def get_delhi_weather():
    # Open-Meteo API endpoint
    url = "https://archive-api.open-meteo.com/v1/archive"
    
    # Calculate dates for past 10 days
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=10)
    
    params = {
        "latitude": 28.7041,
        "longitude": 77.1025,
        "start_date": str(start_date),
        "end_date": str(end_date),
        "daily": "temperature_2m_max,temperature_2m_min,temperature_2m_mean",
        "timezone": "Asia/Kolkata"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    return data

# Extract and process data
weather_data = get_delhi_weather()
daily = weather_data['daily']

dates = pd.to_datetime(daily['time'])
max_temp = daily['temperature_2m_max']
min_temp = daily['temperature_2m_min']
avg_temp = daily['temperature_2m_mean']

# Create the plot
plt.figure(figsize=(12, 6))

plt.plot(dates, max_temp, color='red', marker='o', label='Maximum Temperature', linewidth=2)
plt.plot(dates, min_temp, color='green', marker='s', label='Minimum Temperature', linewidth=2)
plt.plot(dates, avg_temp, color='blue', marker='^', label='Average Temperature', linewidth=2)

plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.title('Delhi Weather - Past 10 Days', fontsize=14, fontweight='bold')
plt.legend(loc='lower right', fontsize=10)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('delhi weather 2.png', dpi=300, bbox_inches='tight')
print("Plot saved as 'delhi weather 2.png'")
plt.show()