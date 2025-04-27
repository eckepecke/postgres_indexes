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

# Load the CSV into the DataFrame
# add_read_heavy_small = pd.read_csv('../TPCC_RESULTS/results_TPCC_SMALL_DROP_INDEXES.csv')
add_read_heavy_medium = pd.read_csv('../TPCC_RESULTS/results_TPCC_MEDIUM_ADD_READ_HEAVY.csv')
add_read_heavy_big = pd.read_csv('../TPCC_RESULTS/results_TPCC_BIG_ADD_READ_HEAVY.csv')

# Calculate the mean NOPM for each dataset
mean_nopm = {
    'Baseline S': tpcc_std_small['NOPM'].mean(),
    'Added S': add_indexes_small['NOPM'].mean(),
    'Dropped S': drop_indexes_small['NOPM'].mean(),
    'TEMP': drop_indexes_small['NOPM'].mean(),

    #'Added RH S': add_read_heavy_small['NOPM'].mean(),


    'Baseline M': tpcc_std_medium['NOPM'].mean(),
    'Added M': add_indexes_medium['NOPM'].mean(),
    'Dropped M': drop_indexes_medium['NOPM'].mean(),
    'Added RH M': add_read_heavy_medium['NOPM'].mean(),


    'Baseline L': tpcc_std_big['NOPM'].mean(),
    'Added L': add_indexes_big['NOPM'].mean(),
    'Dropped L': drop_indexes_big['NOPM'].mean(),
    'Added RH L': add_read_heavy_big['NOPM'].mean()
}

# Create a bar chart
plt.figure(figsize=(10, 6))

# Bar plot for NOPM means with customized colors
colors = ['#395055', '#407580',  '#3997AA', '#1ED8E6', # Blue shades for Small datasets
          '#395543', '#408056', '#39AA60',  '#7EE500',# Green shades for Medium datasets
          '#553C3D', '#804547', '#AA3F43', '#E5001C']  # Red shades for Large datasets


plt.bar(mean_nopm.keys(), mean_nopm.values(), color=colors)

# Adding labels and title
plt.xlabel('Dataset')
plt.ylabel('Mean NOPM (New Orders per Minute)')
plt.title('Mean NOPM for Small, Medium, and Big Datasets with and without Add Indexes')

# Show plot
plt.show()

# Calculate the mean TPM for each dataset
mean_TPM = {
    'Baseline S': tpcc_std_small['TPM'].mean(),
    'Added S': add_indexes_small['TPM'].mean(),
    'Dropped S': drop_indexes_small['TPM'].mean(),
    'TEMP': drop_indexes_small['TPM'].mean(),


    'Baseline M': tpcc_std_medium['TPM'].mean(),
    'Added M': add_indexes_medium['TPM'].mean(),
    'Dropped M': drop_indexes_medium['TPM'].mean(),
    'Added RH M': add_read_heavy_medium['TPM'].mean(),

    'Baseline L': tpcc_std_big['TPM'].mean(),
    'Added L': add_indexes_big['TPM'].mean(),
    'Dropped L': drop_indexes_big['TPM'].mean(),
    'Added RH L': add_read_heavy_big['TPM'].mean()
}

# Create a bar chart
plt.figure(figsize=(10, 6))


plt.bar(mean_TPM.keys(), mean_TPM.values(), color=colors)

# Adding labels and title
plt.xlabel('Dataset')
plt.ylabel('Mean TPM (New Orders per Minute)')
plt.title('Mean TPM for Small, Medium, and Big Datasets with and without Add Indexes')

# Show plot
plt.show()# Calculate the mean TPM for each dataset

mean_storage = {
    'Baseline S': tpcc_std_small['TotalIndexStorageBytes'].mean(),
    'Added S': add_indexes_small['TotalIndexStorageBytes'].mean(),
    'Dropped S': drop_indexes_small['TotalIndexStorageBytes'].mean(),
    'TEMP': drop_indexes_small['TotalIndexStorageBytes'].mean(),


    'Baseline M': tpcc_std_medium['TotalIndexStorageBytes'].mean(),
    'Added M': add_indexes_medium['TotalIndexStorageBytes'].mean(),
    'Dropped M': drop_indexes_medium['TotalIndexStorageBytes'].mean(),
    'Added RH M': add_read_heavy_medium['TotalIndexStorageBytes'].mean(),


    'Baseline L': tpcc_std_big['TotalIndexStorageBytes'].mean(),
    'Added L': add_indexes_big['TotalIndexStorageBytes'].mean(),
    'Dropped L': drop_indexes_big['TotalIndexStorageBytes'].mean(),
    'Added RH L': add_read_heavy_big['TotalIndexStorageBytes'].mean()
}

# Create a bar chart
plt.figure(figsize=(10, 6))


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
