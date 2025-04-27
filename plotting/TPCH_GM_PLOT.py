import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV into the DataFrame
tpch_std_small = pd.read_csv('../TPCH_RESULTS/results_TPCH_TPCH_STANDARD.csv')
tpch_add_indexes = pd.read_csv('../TPCH_RESULTS/results_TPCH_ADD_INDEXES.csv')
tpch_add_useful = pd.read_csv('../TPCH_RESULTS/results_TPCH_ADD_USEFUL.csv')


# Calculate the mean NOPM for each dataset
mean_gemetric_mean = {
    'Baseline': tpch_std_small['GeometricMean'].mean(),
    'Added': tpch_add_indexes['GeometricMean'].mean(),
    'Added useful': tpch_add_useful['GeometricMean'].mean(),
}

# Create a bar chart
plt.figure(figsize=(10, 6))

# Bar plot for NOPM means with customized colors
colors = ['#395055', '#407580',  '#3997AA', '#1ED8E6'] # Blue shades for Small datasets



plt.bar(mean_gemetric_mean.keys(), mean_gemetric_mean.values(), color=colors)

# Adding labels and title
plt.xlabel('Dataset')
plt.ylabel('Mean Geometric Mean')
plt.title('Mean Geometric mean for different index configurations in TPCH')

# Show plot
plt.show()# Create a scatter plot
# Create a boxplot
plt.figure(figsize=(10, 6))

# Combine the datasets into a list for plotting
data = [
    tpch_std_small['GeometricMean'],
    tpch_add_indexes['GeometricMean'],
    tpch_add_useful['GeometricMean']
]

# Boxplot for the datasets
plt.boxplot(data, patch_artist=True, 
            boxprops=dict(facecolor='#395055', color='#395055'),
            medianprops=dict(color='white'),
            flierprops=dict(markerfacecolor='red', marker='o', markersize=5, linestyle='None'))

# Adding labels and title
plt.xlabel('Dataset')
plt.ylabel('Geometric Mean')
plt.title('Boxplot for Geometric Mean for different index configurations in TPCH')

# Customizing x-axis for clarity
plt.xticks([1, 2, 3], ['Baseline S', 'Added S', 'Dropped S'])

# Show plot
plt.show()# Combine the datasets into a list for plotting


# Load the CSV into the DataFrame
tpch_std_queries = pd.read_csv('../TPCH_RESULTS/query_times_TPCH_TPCH_STANDARD.csv')
tpch_add_indexes_queries = pd.read_csv('../TPCH_RESULTS/query_times_TPCH_ADD_INDEXES.csv')
tpch_add_useful_queries = pd.read_csv('../TPCH_RESULTS/query_times_TPCH_ADD_USEFUL.csv')



plt.figure(figsize=(10, 6))
plt.bar(tpch_std_queries['QueryNumber'], tpch_std_queries['QueryTimeSeconds'], color='skyblue')
plt.xlabel('Query Number')
plt.ylabel('Query Time (Seconds)')
plt.title('Query Execution Times with Added Indexes')
plt.xticks(tpch_std_queries['QueryNumber'])
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(tpch_add_indexes_queries['QueryNumber'], tpch_add_indexes_queries['QueryTimeSeconds'], color='skyblue')
plt.xlabel('Query Number')
plt.ylabel('Query Time (Seconds)')
plt.title('Query Execution Times with Added Indexes')
plt.xticks(tpch_add_indexes_queries['QueryNumber'])
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(tpch_add_useful_queries['QueryNumber'], tpch_add_useful_queries['QueryTimeSeconds'], color='skyblue')
plt.xlabel('Query Number')
plt.ylabel('Query Time (Seconds)')
plt.title('Query Execution Times with Added Indexes')
plt.xticks(tpch_add_useful_queries['QueryNumber'])
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

print(tpch_std_queries.head(5))
print(tpch_add_indexes_queries.head(5))
print(tpch_add_useful_queries.head(5))

# Merge DataFrames on QueryNumber
merged = tpch_std_queries.merge(
    tpch_add_indexes_queries[['QueryNumber', 'QueryTimeSeconds']],
    on='QueryNumber',
    suffixes=('_std', '_index')
).merge(
    tpch_add_useful_queries[['QueryNumber', 'QueryTimeSeconds']],
    on='QueryNumber'
).rename(columns={'QueryTimeSeconds': 'QueryTimeSeconds_useful'})

# Calculate percentage changes relative to standard configuration
merged['pct_change_index'] = ((merged['QueryTimeSeconds_index'] - merged['QueryTimeSeconds_std']) / merged['QueryTimeSeconds_std']) * 100
merged['pct_change_useful'] = ((merged['QueryTimeSeconds_useful'] - merged['QueryTimeSeconds_std']) / merged['QueryTimeSeconds_std']) * 100

# Sort by QueryNumber for consistent ordering
merged = merged.sort_values('QueryNumber').reset_index(drop=True)

# Prepare data for plotting
x = np.arange(len(merged))  # Create an array for the x positions
width = 0.35  # Width of the bars

# Assign colors based on improvement (green) or degradation (red)
colors_index = ['green' if val < 0 else 'red' for val in merged['pct_change_index']]
colors_useful = ['green' if val < 0 else 'red' for val in merged['pct_change_useful']]

# Create the plot
plt.figure(figsize=(14, 7))
plt.bar(x - width/2, merged['pct_change_index'], width, color=colors_index, label='Added Indexes')
plt.bar(x + width/2, merged['pct_change_useful'], width, color=colors_useful, label='Added Useful')

# Customize the plot
plt.xlabel('Query Number')
plt.ylabel('Percentage Change (%)')
plt.title('Percentage Change in Query Execution Time Compared to Standard Configuration')
plt.xticks(x, merged['QueryNumber'])  # Set x-ticks to actual query numbers
plt.axhline(0, color='black', linewidth=0.8)  # Add a baseline at 0%
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()

