#!/bin/bash

SIZE=$1
SETTING=$2

TARGET_DIR="../hammerdb_results/TPCC/${SIZE}/${SETTING}"

OUTPUT_DIR="../TPCC_RESULTS"
mkdir -p "$OUTPUT_DIR"
OUTPUT_FILE="${OUTPUT_DIR}/results_TPCC_${SIZE}_${SETTING}.csv"

# CSV Header
echo "Folder,NOPM,TPM,TotalIndexStorageBytes" > "$OUTPUT_FILE"

# Process each benchmark_results*.txt
find "$TARGET_DIR" -type f -name 'benchmark_results*.txt' | while read -r file; do
    # Extract NOPM and TPM
    result_line=$(grep 'TEST RESULT' "$file")
    NOPM=$(echo "$result_line" | sed -n 's/.*achieved \([0-9]*\) NOPM.*/\1/p')
    TPM=$(echo "$result_line" | sed -n 's/.*from \([0-9]*\) PostgreSQL TPM.*/\1/p')

    # Extract the directory path
    folder=$(dirname "$file")

    # Default index storage value
    total_index_storage=0

    # If index_storage_tpcc.csv exists, calculate sum
    index_file="$folder/postgres_metrics/index_storage_tpcc.csv"
    if [[ -f "$index_file" ]]; then
        # Skip header and sum the third column
        total_index_storage=$(awk -F',' 'NR > 1 {sum += $3} END {print sum}' "$index_file")
    fi

    # Write result to CSV
    echo "$folder,$NOPM,$TPM,$total_index_storage" >> "$OUTPUT_FILE"
done