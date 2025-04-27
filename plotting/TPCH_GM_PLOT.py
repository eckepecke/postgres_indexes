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

# Load the CSV into the DataFrame
tpch_std_qmeans = pd.read_csv('../TPCH_RESULTS/TPCH_STANDARD_query_means.csv')
tpch_add_indexes_qmeans = pd.read_csv('../TPCH_RESULTS/ADD_INDEXES_query_means.csv')
tpch_add_useful_qmeans = pd.read_csv('../TPCH_RESULTS/ADD_USEFUL_query_means.csv')



# Calculate the percentage difference compared to the standard
# Formula: ((new - standard) / standard) * 100

add_indexes_pct_change = ((tpch_add_indexes_qmeans['MeanTimeSeconds'] - tpch_std_qmeans['MeanTimeSeconds']) / tpch_std_qmeans['MeanTimeSeconds']) * 100
add_useful_pct_change = ((tpch_add_useful_qmeans['MeanTimeSeconds'] - tpch_std_qmeans['MeanTimeSeconds']) / tpch_std_qmeans['MeanTimeSeconds']) * 100

# If you want to put it nicely into a DataFrame:
result = pd.DataFrame({
    'QueryNumber': tpch_std_qmeans['QueryNumber'],
    'Standard_MeanTimeSeconds': tpch_std_qmeans['MeanTimeSeconds'],
    'Add_Indexes_MeanTimeSeconds': tpch_add_indexes_qmeans['MeanTimeSeconds'],
    'Add_Indexes_PercentChange': add_indexes_pct_change,
    'Add_Useful_MeanTimeSeconds': tpch_add_useful_qmeans['MeanTimeSeconds'],
    'Add_Useful_PercentChange': add_useful_pct_change
})

# Set a nice big figure
# plt.figure(figsize=(14, 7))

# # Plot both % changes
# plt.plot(result['QueryNumber'], result['Add_Indexes_PercentChange'], marker='o', label='Add Indexes % Change')
# plt.plot(result['QueryNumber'], result['Add_Useful_PercentChange'], marker='s', label='Add Useful % Change')

# # Add a horizontal line at 0% for reference
# plt.axhline(0, color='black', linewidth=0.8, linestyle='--')

# # Add labels and title
# plt.xlabel('Query Number')
# plt.ylabel('Percentage Change (%)')
# plt.title('Percentage Change in Mean Time per Query Compared to Standard')
# plt.legend()
# plt.grid(True)

# # Show the plot
# plt.show()

# Set up
x = np.arange(len(result['QueryNumber']))  # the label locations
width = 0.35  # width of the bars

fig, ax = plt.subplots(figsize=(16, 8))

# Plot bars
rects1 = ax.bar(x - width/2, result['Add_Indexes_PercentChange'], width, label='Add Indexes % Change')
rects2 = ax.bar(x + width/2, result['Add_Useful_PercentChange'], width, label='Add Useful % Change')

# Add a horizontal line at 0%
ax.axhline(0, color='black', linewidth=0.8)

# Labels and title
ax.set_xlabel('Query Number')
ax.set_ylabel('Percentage Change (%)')
ax.set_title('Percentage Change in Mean Time per Query Compared to Standard')
ax.set_xticks(x)
ax.set_xticklabels(result['QueryNumber'])
ax.legend()
ax.grid(True, axis='y')

fig.tight_layout()
plt.show()
