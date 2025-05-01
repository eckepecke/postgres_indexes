import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from tabulate import tabulate


# # Load the CSV into the DataFrame
# tpch_standard = pd.read_csv('../TPCH_RESULTS/results_TPCH_TPCH_STANDARD.csv')
# add_indexes = pd.read_csv('../TPCH_RESULTS/results_TPCH_ADD_INDEXES.csv')
# add_useful = pd.read_csv('../TPCH_RESULTS/results_TPCH_ADD_USEFUL.csv')


# Function to filter out outliers
def filter_outliers(df):
    return df[(df['is_outlier'] == False)]

# Load and filter each dataset
tpch_standard = filter_outliers(pd.read_csv('../TPCH_RESULTS/processed/results_TPCH_TPCH_STANDARD_GeometricMean_analysis.csv'))
add_indexes = filter_outliers(pd.read_csv('../TPCH_RESULTS/processed/results_TPCH_ADD_INDEXES_GeometricMean_analysis.csv'))
add_useful = filter_outliers(pd.read_csv('../TPCH_RESULTS/processed/results_TPCH_ADD_USEFUL_GeometricMean_analysis.csv'))


# Calculate the mean TPM for each dataset
mean_gm = {
    'Baseline': tpch_standard['GeometricMean'].mean(),
    'Added Indexes': add_indexes['GeometricMean'].mean(),
    'Added Useful': add_useful['GeometricMean'].mean(),
}

def format_bytes_to_mb(x):
    return f"{x / (1024 * 1024):.2f} MB"


# Configurations and sizes
configs = ['Baseline', 'Added Indexes', 'Added Useful']


data = []
for config in configs:
    row = mean_gm[config]
    data.append(row)

df = pd.DataFrame(data, index=configs)
df.index.name = 'Configuration'
df_rounded = df.round(2)

# Display the table
print(df_rounded)

print(tabulate(df_rounded, headers='keys', tablefmt='grid'))


# Load the CSV into the DataFrame
final_report = pd.read_csv('../TPCH_RESULTS/final_report.csv')

# Select only the columns we want
result_table = final_report[['QueryNumber', 'PctChange_Useful']]

# Round the percentage change to 2 decimal places
result_table['PctChange_Useful'] = result_table['PctChange_Useful'].round(2)

# Rename columns for nicer display
result_table = result_table.rename(columns={
    'QueryNumber': 'Query Number',
    'PctChange_Useful': 'Performance Change (%)'
})

# Display using tabulate
print(tabulate(result_table, headers='keys', tablefmt='grid', showindex=False))

mean_storage = {
    'Baseline': tpch_standard['TotalIndexStorageBytes'].mean(),
    'Added Indexes': add_indexes['TotalIndexStorageBytes'].mean(),
    'Added Useful': add_useful['TotalIndexStorageBytes'].mean(),
}


data = []
for config in configs:
    bytes_value = mean_storage[config]
    row = format_bytes_to_mb(bytes_value)
    data.append(row)


df = pd.DataFrame(data, index=configs, columns=['Index Storage (MB)'])
df.index.name = 'Configuration'
df_rounded = df.round(2)

# Display the table
print(df_rounded)

print(tabulate(df_rounded, headers='keys', tablefmt='grid'))

