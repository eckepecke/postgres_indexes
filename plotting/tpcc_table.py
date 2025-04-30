import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Function to filter out outliers
def filter_outliers(df):
    return df[(df['is_outlier_NOPM'] == False) & (df['is_outlier_TPM'] == False)]

# Load and filter each dataset
tpcc_std_small = filter_outliers(pd.read_csv('../TPCC_RESULTS/processed/results_TPCC_SMALL_TPCC_STANDARD_analysis.csv'))
tpcc_std_medium = filter_outliers(pd.read_csv('../TPCC_RESULTS/processed/results_TPCC_MEDIUM_TPCC_STANDARD_analysis.csv'))
tpcc_std_big = filter_outliers(pd.read_csv('../TPCC_RESULTS/processed/results_TPCC_BIG_TPCC_STANDARD_analysis.csv'))

add_indexes_small = filter_outliers(pd.read_csv('../TPCC_RESULTS/processed/results_TPCC_SMALL_ADD_INDEXES_analysis.csv'))
add_indexes_medium = filter_outliers(pd.read_csv('../TPCC_RESULTS/processed/results_TPCC_MEDIUM_ADD_INDEXES_analysis.csv'))
add_indexes_big = filter_outliers(pd.read_csv('../TPCC_RESULTS/processed/results_TPCC_BIG_ADD_INDEXES_analysis.csv'))

drop_indexes_small = filter_outliers(pd.read_csv('../TPCC_RESULTS/processed/results_TPCC_SMALL_DROP_INDEXES_analysis.csv'))
drop_indexes_medium = filter_outliers(pd.read_csv('../TPCC_RESULTS/processed/results_TPCC_MEDIUM_DROP_INDEXES_analysis.csv'))
drop_indexes_big = filter_outliers(pd.read_csv('../TPCC_RESULTS/processed/results_TPCC_BIG_DROP_INDEXES_analysis.csv'))

add_read_heavy_small = filter_outliers(pd.read_csv('../TPCC_RESULTS/processed/results_TPCC_SMALL_ADD_READ_HEAVY_analysis.csv'))
add_read_heavy_medium = filter_outliers(pd.read_csv('../TPCC_RESULTS/processed/results_TPCC_MEDIUM_ADD_READ_HEAVY_analysis.csv'))
add_read_heavy_big = filter_outliers(pd.read_csv('../TPCC_RESULTS/processed/results_TPCC_BIG_ADD_READ_HEAVY_analysis.csv'))


# Calculate the mean TPM for each dataset
mean_tpm = {
    'Baseline S': tpcc_std_small['TPM'].mean(),
    'Added S': add_indexes_small['TPM'].mean(),
    'Dropped S': drop_indexes_small['TPM'].mean(),
    'Added RH S': add_read_heavy_small['TPM'].mean(),

    'Baseline M': tpcc_std_medium['TPM'].mean(),
    'Added M': add_indexes_medium['TPM'].mean(),
    'Dropped M': drop_indexes_medium['TPM'].mean(),
    'Added RH M': add_read_heavy_medium['TPM'].mean(),

    'Baseline L': tpcc_std_big['TPM'].mean(),
    'Added L': add_indexes_big['TPM'].mean(),
    'Dropped L': drop_indexes_big['TPM'].mean(),
    'Added RH L': add_read_heavy_big['TPM'].mean()
}

# Define a helper function to handle key formatting
# Update the key formatting helper function
def get_key(config, size):
    return f"{config} {size}"  # No exceptions now; all keys include size (e.g., "Added RH S")

def format_bytes_to_mb(x):
    return f"{x / (1024 * 1024):.2f} MB"


# Configurations and sizes
configs = ['Baseline', 'Added', 'Dropped', 'Added RH']
sizes = ['S', 'M', 'L']

# Build the data for the DataFrame
data = []
for config in configs:
    row = {'Configuration': config}
    for size in sizes:
        key = get_key(config, size)
        row[size] = mean_tpm[key]
    data.append(row)

# Create and format the DataFrame
df = pd.DataFrame(data).set_index('Configuration')
df_rounded = df.round(2)

# Display the table
print(df_rounded)

from tabulate import tabulate
print(tabulate(df_rounded, headers='keys', tablefmt='grid'))

# Calculate the mean NOPM for each dataset
mean_nopm = {
    'Baseline S': tpcc_std_small['NOPM'].mean(),
    'Added S': add_indexes_small['NOPM'].mean(),
    'Dropped S': drop_indexes_small['NOPM'].mean(),
    'Added RH S': add_read_heavy_small['NOPM'].mean(),

    'Baseline M': tpcc_std_medium['NOPM'].mean(),
    'Added M': add_indexes_medium['NOPM'].mean(),
    'Dropped M': drop_indexes_medium['NOPM'].mean(),
    'Added RH M': add_read_heavy_medium['NOPM'].mean(),

    'Baseline L': tpcc_std_big['NOPM'].mean(),
    'Added L': add_indexes_big['NOPM'].mean(),
    'Dropped L': drop_indexes_big['NOPM'].mean(),
    'Added RH L': add_read_heavy_big['NOPM'].mean()
}

# Reuse the same logic to build the DataFrame
configs = ['Baseline', 'Added', 'Dropped', 'Added RH']
sizes = ['S', 'M', 'L']

data = []
for config in configs:
    row = {'Configuration': config}
    for size in sizes:
        key = get_key(config, size)
        row[size] = mean_nopm[key]  # Pull from mean_nopm instead of mean_tpm
    data.append(row)

df_nopm = pd.DataFrame(data).set_index('Configuration')
df_nopm_rounded = df_nopm.round(2)

# Print the table (with borders for copy-pasting)

print(tabulate(df_nopm_rounded, headers='keys', tablefmt='grid'))

mean_storage = {
    'Baseline S': tpcc_std_small['TotalIndexStorageBytes'].mean(),
    'Added S': add_indexes_small['TotalIndexStorageBytes'].mean(),
    'Dropped S': drop_indexes_small['TotalIndexStorageBytes'].mean(),
    'Added RH S': add_read_heavy_small['TotalIndexStorageBytes'].mean(),

    'Baseline M': tpcc_std_medium['TotalIndexStorageBytes'].mean(),
    'Added M': add_indexes_medium['TotalIndexStorageBytes'].mean(),
    'Dropped M': drop_indexes_medium['TotalIndexStorageBytes'].mean(),
    'Added RH M': add_read_heavy_medium['TotalIndexStorageBytes'].mean(),

    'Baseline L': tpcc_std_big['TotalIndexStorageBytes'].mean(),
    'Added L': add_indexes_big['TotalIndexStorageBytes'].mean(),
    'Dropped L': drop_indexes_big['TotalIndexStorageBytes'].mean(),
    'Added RH L': add_read_heavy_big['TotalIndexStorageBytes'].mean()
}

data = []
for config in configs:
    row = {'Configuration': config}
    for size in sizes:
        key = get_key(config, size)
        bytes_value = mean_storage[key]
        row[size] = format_bytes_to_mb(bytes_value)
    data.append(row)

df_nopm = pd.DataFrame(data).set_index('Configuration')

# Print the table (with borders for copy-pasting)
from tabulate import tabulate
print(tabulate(df_nopm, headers='keys', tablefmt='grid'))