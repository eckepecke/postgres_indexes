!/bin/bash
set -e

# Wait for PostgreSQL to start
until psql -U admin -d benchmarkdb -c '\q'; do
  sleep 1
done

# Load TPC-H data
for f in /datasets/tpch/*.tbl; do
  TABLE=$(basename $f .tbl)
  psql -U admin -d benchmarkdb -c "COPY $TABLE FROM '$f' WITH DELIMITER '|'"
done

Load TPC-C data
for f in /datasets/tpcc/*.csv; do
  TABLE=$(basename $f .csv)
  psql -U admin -d benchmarkdb -c "COPY $TABLE FROM '$f' WITH CSV"
done