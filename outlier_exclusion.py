import pandas as pd
import numpy as np
from scipy.stats import bootstrap

def process_file(input_path, output_path):
    # Load raw data
    df = pd.read_csv(input_path)
    
    # Group by QueryNumber and process each group
    results = []
    for qnum, group in df.groupby('QueryNumber'):
        times = group['QueryTimeSeconds']
        
        # IQR Outlier Detection
        q1 = times.quantile(0.25)
        q3 = times.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        # Filter outliers
        filtered = times[(times >= lower_bound) & (times <= upper_bound)]
        
        # Calculate median
        median_time = filtered.median()
        
        # Calculate 95% CI using bootstrapping
        res = bootstrap((filtered,), np.median, confidence_level=0.95)
        ci_low, ci_high = res.confidence_interval
        
        results.append({
            'QueryNumber': qnum,
            'MedianTimeSeconds': median_time,
            'CI_Low': ci_low,
            'CI_High': ci_high
        })
    
    # Save results
    result_df = pd.DataFrame(results)
    result_df.to_csv(output_path, index=False)

# Process all configurations
configs = ['TPCH_STANDARD', 'ADD_INDEXES', 'ADD_USEFUL']
for config in configs:
    input_file = f'TPCH_RESULTS/query_times_TPCH_{config}.csv'
    output_file = f'TPCH_RESULTS/{config}_processed.csv'
    process_file(input_file, output_file)