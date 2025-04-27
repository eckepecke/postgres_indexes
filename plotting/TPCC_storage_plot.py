import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load the CSV into the DataFrame
tpcc_std_small = pd.read_csv('../TPCC_RESULTS/results_TPCC_SMALL_TPCC_STANDARD.csv')
tpcc_std_medium = pd.read_csv('../TPCC_RESULTS/results_TPCC_MEDIUM_TPCC_STANDARD.csv')
tpcc_std_big = pd.read_csv('../TPCC_RESULTS/results_TPCC_BIG_TPCC_STANDARD.csv')

# Load the CSV into the DataFrame
add_indexes_small = pd.read_csv('../TPCC_RESULTS/results_TPCC_SMALL_ADD_INDEXES.csv')
add_indexes_medium = pd.read_csv('../TPCC_RESULTS/results_TPCC_MEDIUM_ADD_INDEXES.csv')
add_indexes_big = pd.read_csv('../TPCC_RESULTS/results_TPCC_BIG_ADD_INDEXES.csv')

# Load the CSV into the DataFrame
drop_indexes_small = pd.read_csv('../TPCC_RESULTS/results_TPCC_SMALL_DROP_INDEXES.csv')
drop_indexes_medium = pd.read_csv('../TPCC_RESULTS/results_TPCC_MEDIUM_DROP_INDEXES.csv')
drop_indexes_big = pd.read_csv('../TPCC_RESULTS/results_TPCC_BIG_DROP_INDEXES.csv')

# Calculate the mean TPM for each dataset
mean_storage = {
    'Baseline S': tpcc_std_small['TotalIndexStorageBytes'].mean(),
    'Added S': add_indexes_small['TotalIndexStorageBytes'].mean(),
    'Dropped S': drop_indexes_small['TotalIndexStorageBytes'].mean(),

    'Baseline M': tpcc_std_medium['TotalIndexStorageBytes'].mean(),
    'Added M': add_indexes_medium['TotalIndexStorageBytes'].mean(),
    'Dropped M': drop_indexes_medium['TotalIndexStorageBytes'].mean(),

    'Baseline L': tpcc_std_big['TotalIndexStorageBytes'].mean(),
    'Added L': add_indexes_big['TotalIndexStorageBytes'].mean(),
    'Dropped L': drop_indexes_big['TotalIndexStorageBytes'].mean()
}

# Create a bar chart
plt.figure(figsize=(10, 6))

# Bar plot for TPM means with customized colors
colors = ['#395055', '#407580',  '#3997AA',  # Blue shades for Small datasets
          '#395543', '#408056', '#39AA60',  # Green shades for Medium datasets
          '#553C3D', '#804547', '#AA3F43']  # Red shades for Large datasets


plt.bar(mean_storage.keys(), mean_storage.values(), color=colors)

# Adding labels and title
plt.xlabel('Dataset')
plt.ylabel('Mean STORAGE (New Orders per Minute)')
plt.title('Mean STORAGE for Small, Medium, and Big Datasets with and without Add Indexes')


# Format y-axis with commas
ax = plt.gca()  # Get current axis
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))

# Show plot
plt.show()