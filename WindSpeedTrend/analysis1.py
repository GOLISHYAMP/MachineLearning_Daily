import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

 

# Read the data from a CSV file or any other source
data = pd.read_csv('C:\\Users\\SPURUSHO\\Desktop\\Machine Learning\\MachineLearning_Daily\\WindSpeedTrend\\Weather.csv')

 

# Calculate the correlation matrix
correlation_matrix = data[['WS', 'AP', 'RH']].corr()

 

# Create a heatmap of the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()