import pandas as pd
import matplotlib.pyplot as plt

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
mean_TPM = {
    'Baseline S': tpcc_std_small['TPM'].mean(),
    'Added S': add_indexes_small['TPM'].mean(),
    'Dropped S': drop_indexes_small['TPM'].mean(),

    'Baseline M': tpcc_std_medium['TPM'].mean(),
    'Added M': add_indexes_medium['TPM'].mean(),
    'Dropped M': drop_indexes_medium['TPM'].mean(),

    'Baseline L': tpcc_std_big['TPM'].mean(),
    'Added L': add_indexes_big['TPM'].mean(),
    'Dropped L': drop_indexes_big['TPM'].mean()
}

# Create a bar chart
plt.figure(figsize=(10, 6))

# Bar plot for TPM means with customized colors
colors = ['#395055', '#407580',  '#3997AA',  # Blue shades for Small datasets
          '#395543', '#408056', '#39AA60',  # Green shades for Medium datasets
          '#553C3D', '#804547', '#AA3F43']  # Red shades for Large datasets


plt.bar(mean_TPM.keys(), mean_TPM.values(), color=colors)

# Adding labels and title
plt.xlabel('Dataset')
plt.ylabel('Mean TPM (New Orders per Minute)')
plt.title('Mean TPM for Small, Medium, and Big Datasets with and without Add Indexes')

# Show plot
plt.show()