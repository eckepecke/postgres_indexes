import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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

# Define bar colors
colors = ['#395055', '#407580', '#3997AA', '#1ED8E6',   # Small datasets
          '#395543', '#408056', '#39AA60', '#7EE500',   # Medium datasets
          '#553C3D', '#804547', '#AA3F43', '#E5001C']   # Large datasets

# Set manual x positions
group_gap = 0.35  # Extra gap between groups
x_positions = []

# Base x = 0
x = 0
for i in range(len(mean_nopm)):
    x_positions.append(x)
    if (i + 1) % 4 == 0:  # After every 4 bars (small, medium)
        x += group_gap
    x += 1  # Normal step between bars

# Create the bar plot
plt.figure(figsize=(12, 6))
plt.bar(x_positions, mean_nopm.values(), color=colors)

# Customize x-axis
plt.xticks(x_positions, mean_nopm.keys(), rotation=45, ha='right')

# Adding labels and title
plt.xlabel('Configuration')
plt.ylabel('Mean NOPM (New Orders per Minute)')

plt.tight_layout()
plt.show()

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

# Define bar colors (same color palette)
colors = ['#395055', '#407580', '#3997AA', '#1ED8E6',   # Small datasets
          '#395543', '#408056', '#39AA60', '#7EE500',   # Medium datasets
          '#553C3D', '#804547', '#AA3F43', '#E5001C']   # Large datasets

# Set manual x positions
group_gap = 0.35  # Extra gap between groups
x_positions = []

x = 0
for i in range(len(mean_tpm)):
    x_positions.append(x)
    if (i + 1) % 4 == 0:
        x += group_gap
    x += 1

# Create the bar plot
plt.figure(figsize=(12, 6))
plt.bar(x_positions, mean_tpm.values(), color=colors)

# Customize x-axis
plt.xticks(x_positions, mean_tpm.keys(), rotation=45, ha='right')

# Adding labels and title
plt.xlabel('Configuration')
plt.ylabel('Mean TPM (Transactions per Minute)')

plt.tight_layout()
plt.show()
# mean_storage dictionary (without TEMP)
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

# Define bar colors (reuse the same)
colors = ['#395055', '#407580', '#3997AA', '#1ED8E6',   # Small datasets
          '#395543', '#408056', '#39AA60', '#7EE500',   # Medium datasets
          '#553C3D', '#804547', '#AA3F43', '#E5001C']   # Large datasets

# Set manual x positions
group_gap = 0.35  # Extra gap between groups
x_positions = []

x = 0
for i in range(len(mean_storage)):
    x_positions.append(x)
    if (i + 1) % 4 == 0:
        x += group_gap
    x += 1

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.bar(x_positions, mean_storage.values(), color=colors)

# Customize x-axis
plt.xticks(x_positions, mean_storage.keys(), rotation=45, ha='right')

# Add labels and title
plt.xlabel('Configuration')
plt.ylabel('Mean Total Index Storage (Bytes)')

# Format y-axis with commas
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))

plt.tight_layout()
plt.show()