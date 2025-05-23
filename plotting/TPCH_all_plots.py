import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Load the CSV into the DataFrame
tpch_std = pd.read_csv('../TPCH_RESULTS/processed/results_TPCH_TPCH_STANDARD_GeometricMean_analysis.csv')
tpch_add_indexes = pd.read_csv('../TPCH_RESULTS/processed/results_TPCH_ADD_INDEXES_GeometricMean_analysis.csv')
tpch_add_useful = pd.read_csv('../TPCH_RESULTS/processed/results_TPCH_ADD_USEFUL_GeometricMean_analysis.csv')

# # Load the CSV into the DataFrame
# tpch_std = pd.read_csv('../TPCH_RESULTS/results_TPCH_TPCH_STANDARD.csv')
# tpch_add_indexes = pd.read_csv('../TPCH_RESULTS/results_TPCH_ADD_INDEXES.csv')
# tpch_add_useful = pd.read_csv('../TPCH_RESULTS/results_TPCH_ADD_USEFUL.csv')


# Calculate the mean NOPM for each dataset
mean_gemetric_mean = {
    'Baseline': tpch_std['GeometricMean'].mean(),
    'Added': tpch_add_indexes['GeometricMean'].mean(),
    'Added Used': tpch_add_useful['GeometricMean'].mean(),
}

# Create a bar chart
plt.figure(figsize=(10, 6))

# Bar plot for NOPM means with customized colors
colors = ['#395055', '#407580',  '#3997AA', '#1ED8E6'] # Blue shades for Small datasets

plt.bar(mean_gemetric_mean.keys(), mean_gemetric_mean.values(), color=colors)

# Adding labels and title
plt.ylabel('Mean Geometric Mean')

# Show plot
plt.show()

# Load the CSV into the DataFrame
tpch_std_queries = pd.read_csv('../TPCH_RESULTS/TPCH_STANDARD_query_means.csv')
tpch_add_indexes_queries = pd.read_csv('../TPCH_RESULTS/ADD_INDEXES_query_means.csv')
tpch_add_useful_queries = pd.read_csv('../TPCH_RESULTS/ADD_USEFUL_query_means.csv')

plt.figure(figsize=(10, 6))
plt.bar(tpch_std_queries['QueryNumber'], tpch_std_queries['MeanTimeSeconds'], color='skyblue')
plt.xlabel('Query Number', fontsize=14)
plt.ylabel('Query Time (Seconds)')
plt.xticks(tpch_std_queries['QueryNumber'])
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(tpch_add_indexes_queries['QueryNumber'], tpch_add_indexes_queries['MeanTimeSeconds'], color='skyblue')
plt.xlabel('Query Number', fontsize=14)
plt.ylabel('Query Time (Seconds)')
plt.xticks(tpch_add_indexes_queries['QueryNumber'])
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(tpch_add_useful_queries['QueryNumber'], tpch_add_useful_queries['MeanTimeSeconds'], color='skyblue')
plt.xlabel('Query Number', fontsize=14)
plt.ylabel('Query Time (Seconds)')
plt.xticks(tpch_add_useful_queries['QueryNumber'])
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

print(tpch_std_queries.head(5))
print(tpch_add_indexes_queries.head(5))
print(tpch_add_useful_queries.head(5))

import matplotlib.pyplot as plt

# Load report data
report = pd.read_csv('../TPCH_RESULTS/processed/final_report.csv')

# Calculate error bars for PERCENTAGE CHANGES using original CIs
# For Add Indexes
indexes_lower_err = ((report['CI_Low_idx'] - report['MedianTimeSeconds_std']) / report['MedianTimeSeconds_std']) * 100 - report['PctChange_Indexes']
indexes_upper_err = report['PctChange_Indexes'] - ((report['CI_High_idx'] - report['MedianTimeSeconds_std']) / report['MedianTimeSeconds_std']) * 100

# For Add Useful
useful_lower_err = ((report['CI_Low'] - report['MedianTimeSeconds_std']) / report['MedianTimeSeconds_std']) * 100 - report['PctChange_Useful']
useful_upper_err = report['PctChange_Useful'] - ((report['CI_High'] - report['MedianTimeSeconds_std']) / report['MedianTimeSeconds_std']) * 100

# Convert to absolute error ranges
indexes_err = [np.abs(indexes_lower_err), np.abs(indexes_upper_err)]
useful_err = [np.abs(useful_lower_err), np.abs(useful_upper_err)]

# Create plot
fig, ax = plt.subplots(figsize=(16, 8))
x = np.arange(len(report))
width = 0.35

# Plot bars with corrected error ranges
ax.bar(x - width/2, report['PctChange_Indexes'], width,
       yerr=indexes_err,  # Use calculated error ranges
       label='With Additional Indexes',
       capsize=5)

ax.bar(x + width/2, report['PctChange_Useful'], width,
       yerr=useful_err,  # Use calculated error ranges
       label='With Used Indexes',
       capsize=5)

# Formatting (keep existing code)
ax.set_title('Query Performance Comparison with 95% Confidence Intervals')
ax.set_xlabel('Query Number')
ax.set_ylabel('Percentage Change from Baseline (%)')
ax.set_xticks(x)
ax.set_xticklabels(report['QueryNumber'])
ax.axhline(0, color='black', linewidth=0.8)
ax.legend()
ax.grid(True, axis='y')

# Handle NaN values in CIs (replace with median CI where missing)
report['CI_Low'] = report['CI_Low'].fillna(report['CI_Low'].median())
report['CI_High'] = report['CI_High'].fillna(report['CI_High'].median())

plt.show()

# Calculate the mean TPM for each dataset
mean_storage = {
    'Baseline': tpch_std['TotalIndexStorageBytes'].mean(),
    'Added': tpch_add_indexes['TotalIndexStorageBytes'].mean(),
    'Added Used': tpch_add_useful['TotalIndexStorageBytes'].mean(),
}

# Create a bar chart
plt.figure(figsize=(10, 6))

# Bar plot for TPM means with customized colors
colors = ['#395055', '#407580',  '#3997AA',  # Blue shades for Small datasets
          '#395543', '#408056', '#39AA60',  # Green shades for Medium datasets
          '#553C3D', '#804547', '#AA3F43']  # Red shades for Large datasets

plt.bar(mean_storage.keys(), mean_storage.values(), color=colors)

# Adding labels and title
plt.ylabel('Mean Storage (in bytes)')

# Format y-axis with commas
ax = plt.gca()  # Get current axis
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))

# Show plot
plt.show()