import pandas as pd
import matplotlib.pyplot as plt

 

# Read the wind speed data from a CSV file or any other source
data = pd.read_csv('C:\\Users\\SPURUSHO\\Desktop\\Machine Learning\\MachineLearning_Daily\\WindSpeedTrend\\Weather.csv')

 

# Calculate descriptive statistics
mean_speed = data['WS'].mean()
median_speed = data['WS'].median()
std_deviation = data['WS'].std()
min_speed = data['WS'].min()
max_speed = data['WS'].max()

 

# Print the descriptive statistics
print(f"Mean: {mean_speed:.2f} m/s")
print(f"Median: {median_speed:.2f} m/s")
print(f"Standard Deviation: {std_deviation:.2f} m/s")
print(f"Minimum: {min_speed:.2f} m/s")
print(f"Maximum: {max_speed:.2f} m/s")

 

# Create a line plot of wind speed over time
plt.plot(data['Observation'], data['WS'])
plt.xlabel('Date')
plt.ylabel('Wind Speed (m/s)')
plt.title('Wind Speed Trend')
plt.xticks(rotation=45)
plt.show()