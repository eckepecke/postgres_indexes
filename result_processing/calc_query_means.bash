awk -F, '
NR > 1 {
    sum[$2] += $3;  # Sum of QueryTimeSeconds for each QueryNumber
    count[$2] += 1; # Count occurrences of each QueryNumber
}
END {
    # Print the header for the new CSV file
    print "QueryNumber,MeanTimeSeconds";
    for (q in sum) {
        mean = sum[q] / count[q];  # Calculate mean for each QueryNumber
        print q "," mean;          # Print the result in CSV format
    }
}
' ../TPCH_RESULTS/query_times_TPCH_TPCH_STANDARD.csv > ../TPCH_RESULTS/TPCH_STANDARD_query_means.csv

awk -F, '
NR > 1 {
    sum[$2] += $3;  # Sum of QueryTimeSeconds for each QueryNumber
    count[$2] += 1; # Count occurrences of each QueryNumber
}
END {
    # Print the header for the new CSV file
    print "QueryNumber,MeanTimeSeconds";
    for (q in sum) {
        mean = sum[q] / count[q];  # Calculate mean for each QueryNumber
        print q "," mean;          # Print the result in CSV format
    }
}
' ../TPCH_RESULTS/query_times_TPCH_ADD_INDEXES.csv > ../TPCH_RESULTS/ADD_INDEXES_query_means.csv

awk -F, '
NR > 1 {
    sum[$2] += $3;  # Sum of QueryTimeSeconds for each QueryNumber
    count[$2] += 1; # Count occurrences of each QueryNumber
}
END {
    # Print the header for the new CSV file
    print "QueryNumber,MeanTimeSeconds";
    for (q in sum) {
        mean = sum[q] / count[q];  # Calculate mean for each QueryNumber
        print q "," mean;          # Print the result in CSV format
    }
}
' ../TPCH_RESULTS/query_times_TPCH_ADD_USEFUL.csv > ../TPCH_RESULTS/ADD_USEFUL_query_means.csv