import pandas as pd
import matplotlib.pyplot as plt

# Read the wind speed data from a CSV file or any other source
data = pd.read_csv('C:\\Users\\SPURUSHO\\Desktop\\Machine Learning\\MachineLearning_Daily\\WindSpeedTrend\\Weather.csv')

# Convert the 'Observation' column to datetime format
data['Observation'] = pd.to_datetime(data['Observation'])

# Set the 'Observation' column as the index
data.set_index('Observation', inplace=True)

# Resample the data by month and calculate the monthly statistics
monthly_data = data['WS'].resample('M').agg(['mean', 'median', 'std', 'min', 'max'])

# Print the monthly statistics
print(monthly_data)

# Create a line plot of monthly wind speed
plt.plot(monthly_data.index, monthly_data['mean'])
plt.xlabel('Date')
plt.ylabel('Mean Wind Speed (m/s)')
plt.title('Monthly Mean Wind Speed')
plt.xticks(rotation=45)
plt.show()
