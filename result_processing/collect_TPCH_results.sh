#!/bin/bash

SETTING=$1

TARGET_DIR="../hammerdb_results/TPCH/${SETTING}"

OUTPUT_DIR="../TPCH_RESULTS"
mkdir -p "$OUTPUT_DIR"
OUTPUT_FILE="${OUTPUT_DIR}/results_TPCH_${SETTING}.csv"
QUERY_TIMES_FILE="${OUTPUT_DIR}/query_times_TPCH_${SETTING}.csv"

# CSV Headers
echo "Folder,GeometricMean,TotalIndexStorageBytes" > "$OUTPUT_FILE"
echo "Folder,QueryNumber,QueryTimeSeconds" > "$QUERY_TIMES_FILE"

# Process each benchmark_results*.txt
find "$TARGET_DIR" -type f -name 'benchmark_results*.txt' | while read -r file; do
    echo "Processing file: $file"

    # Extract geometric mean
    line=$(grep 'Geometric mean of query times' "$file")
    echo "Found line: $line"
    geometric_mean=$(echo "$line" | sed -n 's/.*is \\"*\([0-9.]*\)\\"*.*/\1/p')
    echo "Geometric mean extracted: $geometric_mean"

    folder=$(dirname "$file")

    # Index storage
    total_index_storage=0
    index_file="$folder/postgres_metrics/index_storage_tpch.csv"
    if [[ -f "$index_file" ]]; then
        total_index_storage=$(awk -F',' 'NR > 1 {sum += $3} END {print sum}' "$index_file")
    fi

    # Save to results CSV
    if [[ -n "$geometric_mean" ]]; then
        echo "$folder,$geometric_mean,$total_index_storage" >> "$OUTPUT_FILE"
    else
        echo "$folder,,0" >> "$OUTPUT_FILE"
    fi

    # Extract individual query times
    grep -oE '"query [0-9]+ completed in [0-9.]+ seconds"' "$file" | while read -r line; do
        line=$(echo "$line" | tr -d '"')
        query_num=$(echo "$line" | grep -oE 'query [0-9]+' | cut -d' ' -f2)
        time_sec=$(echo "$line" | grep -oE '[0-9.]+ seconds' | cut -d' ' -f1)
        echo "$folder,$query_num,$time_sec" >> "$QUERY_TIMES_FILE"
    done

done
