import netCDF4 as nc
import pandas as pd

def convert_netcdf_to_excel(input_file, output_file):
    # Read the NetCDF file
    dataset = nc.Dataset(input_file)

    # Get the variable names
    variable_names = dataset.variables.keys()
    print(dataset.variables["TAXIS"][:])
    # Create a Pandas DataFrame to store the data
#     data_dict = {}
#     for var_name in variable_names:
#         var_data = dataset.variables[var_name][:]
#         data_dict[var_name] = var_data

#     df = pd.DataFrame(data_dict)

#     # Write DataFrame to Excel file
#     df.to_excel(output_file, index=False)

# Usage example
input_file = "WindSpeedTrend\IIG-bharati-AWS.nc"
output_file = "output.xlsx"
convert_netcdf_to_excel(input_file, output_file)
