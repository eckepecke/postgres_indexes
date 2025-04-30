#!/usr/bin/env python3
import pandas as pd
import numpy as np
import sys
import os
import glob
import argparse

def detect_outliers(data, column, method='iqr'):
    """
    Detect outliers in a dataset using the 1.5×IQR rule.
    
    Args:
        data (pd.DataFrame): DataFrame containing the data
        column (str): Column name to check for outliers
        method (str): Method to use for outlier detection ('iqr' is supported)
    
    Returns:
        pd.DataFrame: DataFrame with outlier status as a boolean column
    """
    if method == 'iqr':
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        data['is_outlier'] = (data[column] < lower_bound) | (data[column] > upper_bound)
        
        return data
    else:
        raise ValueError(f"Method {method} not supported. Use 'iqr'.")

def process_file(file_path, metrics, output_dir=None, exclude_outliers=False):
    """
    Process a single file for outlier detection on specified metrics.
    
    Args:
        file_path (str): Path to the CSV file
        metrics (list): List of metrics to check for outliers
        output_dir (str): Directory to save output files (if None, no files are saved)
        exclude_outliers (bool): Whether to exclude outliers in output files
    """
    try:
        # Extract file name for reporting
        file_name = os.path.basename(file_path)
        
        # Read the data
        data = pd.read_csv(file_path)
        
        print(f"\n{'='*80}")
        print(f"Processing file: {file_name}")
        print(f"{'='*80}")
        
        # Process each metric
        for metric in metrics:
            if metric not in data.columns:
                print(f"Warning: Column '{metric}' not found in {file_name}, skipping this metric.")
                continue
            
            print(f"\nAnalyzing metric: {metric}")
            print(f"{'-'*50}")
            
            # Detect outliers
            data_with_outliers = detect_outliers(data, metric)
            
            # Get outlier information
            outlier_count = data_with_outliers['is_outlier'].sum()
            total_count = len(data_with_outliers)
            print(f"Found {outlier_count} outliers out of {total_count} data points ({outlier_count/total_count*100:.2f}%)")
            
            if outlier_count > 0:
                print("\nOutliers:")
                print(data_with_outliers[data_with_outliers['is_outlier']])
            
            # Print summary statistics for non-outliers
            non_outliers = data_with_outliers[~data_with_outliers['is_outlier']]
            if not non_outliers.empty:
                print("\nSummary statistics for non-outliers:")
                print(f"Count: {len(non_outliers)}")
                print(f"Median {metric}: {non_outliers[metric].median()}")
                print(f"Mean {metric}: {non_outliers[metric].mean()}")
                print(f"Std Dev {metric}: {non_outliers[metric].std()}")
                
                # Calculate 95% confidence interval for the mean
                mean = non_outliers[metric].mean()
                std_err = non_outliers[metric].std() / np.sqrt(len(non_outliers))
                conf_interval = 1.96 * std_err  # 95% confidence
                print(f"95% Confidence Interval: {mean - conf_interval} to {mean + conf_interval}")
            
            # Save results if output directory is specified
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
                
                # Create output filename based on original filename and metric
                base_name = os.path.splitext(file_name)[0]
                output_path = os.path.join(output_dir, f"{base_name}_{metric}_analysis.csv")
                
                if exclude_outliers:
                    # Save only non-outliers
                    non_outliers.drop(columns=['is_outlier']).to_csv(output_path, index=False)
                    print(f"\nNon-outlier data saved to {output_path}")
                else:
                    # Save all data with outlier status
                    data_with_outliers.to_csv(output_path, index=False)
                    print(f"\nData with outlier information saved to {output_path}")
                
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Batch process TPC-H benchmark results for outlier detection')
    parser.add_argument('--input_dir', default='../TPCH_results', 
                        help='Directory containing CSV files to analyze (default: ../TPCH_results)')
    parser.add_argument('--metrics', nargs='+', default=['GeometricMean'],
                        help='Metrics to analyze for outliers (default: GeometricMean)')
    parser.add_argument('--output_dir', help='Directory to save output files')
    parser.add_argument('--exclude', action='store_true', help='Output only non-outlier data in output files')
    parser.add_argument('--pattern', default='*.csv', help='File pattern to match (default: *.csv)')
    
    args = parser.parse_args()
    
    # Find all CSV files in the input directory
    file_pattern = os.path.join(args.input_dir, args.pattern)
    files = glob.glob(file_pattern)
    
    if not files:
        print(f"No files matching '{args.pattern}' found in '{args.input_dir}'")
        sys.exit(1)
    
    print(f"Found {len(files)} files to process.")
    
    # Process each file
    for file_path in files:
        process_file(file_path, args.metrics, args.output_dir, args.exclude)
    
    print("\nBatch processing complete!")

if __name__ == "__main__":
    main()