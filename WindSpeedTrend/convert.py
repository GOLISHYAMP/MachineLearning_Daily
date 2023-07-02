import pandas as pd

def excel_to_csv(excel_file, csv_file):
    try:
        # Load the Excel file into a pandas DataFrame
        df = pd.read_excel(excel_file)
        
        # Convert the DataFrame to CSV format and save it
        df.to_csv(csv_file, index=False)
        
        print("Conversion successful!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Specify the paths for the Excel and CSV files
excel_file_path = 'C:\\Users\\SPURUSHO\\Desktop\\Machine Learning\\MachineLearning_Daily\\WindSpeedTrend\\Weather.xlsx'
csv_file_path = 'C:\\Users\\SPURUSHO\\Desktop\\Machine Learning\\MachineLearning_Daily\\WindSpeedTrend\\Weather.csv'

# Convert the Excel file to CSV
excel_to_csv(excel_file_path, csv_file_path)