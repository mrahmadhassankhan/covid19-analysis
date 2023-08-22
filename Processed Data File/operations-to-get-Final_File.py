import pandas as pd

# Read the data from the Files
path1 = "Orignal Data Files\\us-counties-2020.csv"
path2 = "Population_Modified.csv"
df1 = pd.read_csv(path1)
df2 = pd.read_csv(path2)

# Merge the DataFrames based on the 'State' column
merged_df = pd.merge(df1, df2, on='State')

# Group by 'State' and aggregate cases and deaths
grouped_df = merged_df.groupby('State').agg({
    'Total': 'first',
    'Rural': 'first',
    'Urban': 'first',
    'cases': 'sum',
    'deaths': 'sum'
}).reset_index()

# Save the grouped DataFrame to a CSV file
output_csv_filename = 'Final_File.csv'
grouped_df.to_csv(output_csv_filename, index=False)

print(f"Saved to {output_csv_filename}")
