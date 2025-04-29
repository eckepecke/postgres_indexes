import pandas as pd

# Load processed data
std = pd.read_csv('TPCH_RESULTS/TPCH_STANDARD_processed.csv')
idx = pd.read_csv('TPCH_RESULTS/ADD_INDEXES_processed.csv')
usf = pd.read_csv('TPCH_RESULTS/ADD_USEFUL_processed.csv')

# Merge data
merged = std.merge(idx, on='QueryNumber', suffixes=('_std', '_idx')) \
            .merge(usf, on='QueryNumber', suffixes=('', '_usf'))

# Calculate percentage changes
merged['PctChange_Indexes'] = ((merged['MedianTimeSeconds_idx'] - merged['MedianTimeSeconds_std']) / 
                               merged['MedianTimeSeconds_std']) * 100
merged['PctChange_Useful'] = ((merged['MedianTimeSeconds'] - merged['MedianTimeSeconds_std']) / 
                             merged['MedianTimeSeconds_std']) * 100

# Generate final report
report = merged[[
    'QueryNumber',
    'MedianTimeSeconds_std', 'CI_Low_std', 'CI_High_std',
    'MedianTimeSeconds_idx', 'CI_Low_idx', 'CI_High_idx',
    'PctChange_Indexes',
    'MedianTimeSeconds', 'CI_Low', 'CI_High',
    'PctChange_Useful'
]]

report.to_csv('TPCH_RESULTS/final_report.csv', index=False)
print(report)


print("Queries in Standard:", std['QueryNumber'].unique())
print("Queries in Indexed:", idx['QueryNumber'].unique())
print("Queries in Useful:", usf['QueryNumber'].unique())