export TMP=`pwd`/TMP
mkdir -p $TMP

INDEX_SETTING="MORE_MULTI_COLUMN"
TIMESTAMP=$(TZ="Europe/Stockholm" date +"%Y%m%d_%H%M%S")
RUN_DIR="${RESULTS_DIR}/TPCH/${INDEX_SETTING}/${TIMESTAMP}"
PG_METRICS_DIR="${RUN_DIR}/postgres_metrics"
mkdir -p ${PG_METRICS_DIR}

echo "BUILD HAMMERDB SCHEMA WITH MINIMAL MULTI-COLOMN INDEXES"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
./hammerdbcli py auto ./scripts/python/postgres/tproch/pg_tproch_buildschema.py
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
echo "CHECK HAMMERDB SCHEMA"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
./hammerdbcli py auto ./scripts/python/postgres/tproch/pg_tproch_checkschema.py
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"

PGPASSWORD="tpch" psql -h postgres -U tpch -d tpch <<EOF

-- 2. Verify index state
\echo '=== Current Indexes ==='
SELECT
    tablename AS table_name,
    indexname AS index_name,
    array_length(regexp_split_to_array(indexdef, ', '), 1) AS column_count,
    indexdef AS index_definition
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY column_count DESC, table_name, index_name;

-- 1. LineItem: Speeds up date-range filters
-- on shipping dates (e.g., reporting/analytics by shipment window).
CREATE INDEX lineitem_shipdate_idx ON lineitem (l_shipdate);  -- Date-range queries

-- 2. Orders: Optimizes time-based order analysis
-- and customer-centric queries (e.g., orders per customer in a date range).
CREATE INDEX orders_orderdate_custkey_idx ON orders (o_orderdate, o_custkey);  -- Time-based analysis

-- 3. LineItem: Accelerates joins with Orders/Partsupp and filters on
-- orderkey, partkey, or suppkey (common in TPCH joins).
CREATE INDEX lineitem_cover_idx ON lineitem (l_orderkey, l_partkey, l_suppkey);  

-- 4. Orders: Optimizes time-based queries (order date) and customer joins (custkey).  
CREATE INDEX orders_orderdate_custkey_idx
ON orders (o_orderdate, o_custkey);

-- 5. Part: Streamlines part categorization queries (brand, type, size).  
CREATE INDEX part_brand_type_size_idx
ON part (p_brand, p_type, p_size);

-- 6. PartSupp: Enables fast stock availability checks via index-only scans (avoids table lookups). 
CREATE INDEX partsupp_partkey_suppkey_availqty_idx
ON partsupp (ps_partkey, ps_suppkey) INCLUDE (ps_availqty);

-- 7. Supplier: Improves filtering by nation and sorting/analyzing supplier financials (account balance). 
CREATE INDEX supplier_nationkey_acctbal_idx
ON supplier (s_nationkey, s_acctbal);

\echo '=== Current Indexes ==='
SELECT 
  indexname AS name,
  tablename AS table,
  indexdef AS definition
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;

-- 2. Verify index state
\echo '=== Current Indexes ==='
SELECT
    tablename AS table_name,
    indexname AS index_name,
    array_length(regexp_split_to_array(indexdef, ', '), 1) AS column_count,
    indexdef AS index_definition
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY column_count DESC, table_name, index_name;
EOF

echo "RUN HAMMERDB TEST"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
./hammerdbcli py auto ./scripts/python/postgres/tproch/pg_tproch_run.py
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"

echo "CAPTURE INDEX METRICS"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"

# Define output files relative to the run directory
INDEX_STORAGE_DETAILS="${PG_METRICS_DIR}/index_storage_tpch.csv"
INDEX_USAGE_DETAILS="${PG_METRICS_DIR}/index_usage_tpch.csv"
STORAGE_OVERVIEW="${PG_METRICS_DIR}/index_storage_overview_tpch.csv"
USAGE_STATISTICS="${PG_METRICS_DIR}/index_usage_statistics_tpch.csv"
PG_SETTINGS="${PG_METRICS_DIR}/postgres_settings_tpch.txt"
FULL_REPORT="${RUN_DIR}/full_report_tpch.txt"

# Capture all output to the full report in the run directory
exec > >(tee "${FULL_REPORT}") 2>&1

PGPASSWORD="tpch" psql -h postgres -U tpch -d tpch <<EOF
-- Save detailed metrics to CSV files
\echo '\n=== SAVING INDEX STATISTICS ==='

-- Save storage overhead details to CSV
\copy (SELECT indexname, tablename, pg_relation_size(indexname::regclass) AS size_bytes, indexdef FROM pg_indexes WHERE schemaname = 'public') TO '${INDEX_STORAGE_DETAILS}' CSV HEADER;

-- Save usage details overhead summary to CSV
\copy (SELECT indexrelname, idx_scan, idx_tup_read, idx_tup_fetch FROM pg_stat_user_indexes WHERE schemaname = 'public') TO '${INDEX_USAGE_DETAILS}' CSV HEADER;

-- Save storage overhead summary to CSV
\copy (SELECT indexname, tablename, pg_relation_size(indexname::regclass), pg_total_relation_size(tablename::regclass), ROUND(100 * pg_relation_size(indexname::regclass)::numeric / NULLIF(pg_total_relation_size(tablename::regclass), 0), 2), indexdef FROM pg_indexes WHERE schemaname = 'public' ORDER BY pg_relation_size(indexname::regclass) DESC) TO '${STORAGE_OVERVIEW}' CSV HEADER;

-- Save index usage statistics to CSV
\copy (SELECT indexrelname, pg_stat_user_indexes.schemaname, pg_stat_user_indexes.relname, pg_stat_user_indexes.idx_scan, pg_stat_user_indexes.idx_tup_read, pg_stat_user_indexes.idx_tup_fetch, ROUND(100.0 * pg_stat_user_indexes.idx_tup_fetch / NULLIF(pg_stat_user_indexes.idx_tup_read, 0), 2) FROM pg_stat_user_indexes JOIN pg_stat_user_tables ON pg_stat_user_indexes.relid = pg_stat_user_tables.relid WHERE pg_stat_user_indexes.schemaname = 'public' ORDER BY pg_stat_user_indexes.idx_scan DESC) TO '${USAGE_STATISTICS}' CSV HEADER;

-- Save PostgreSQL settings
\o ${PG_SETTINGS}
SHOW ALL;
\o

-- Print summary to console
\echo '\n=== INDEX STORAGE OVERHEAD ==='
SELECT 
  indexname AS name,
  tablename AS table,
  pg_size_pretty(pg_relation_size(indexname::regclass)) AS size,
  pg_size_pretty(pg_total_relation_size(tablename::regclass)) AS table_size,
  ROUND(100 * pg_relation_size(indexname::regclass)::numeric / 
        NULLIF(pg_total_relation_size(tablename::regclass), 0), 2) AS pct_of_table,
  indexdef AS definition
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY pg_relation_size(indexname::regclass) DESC;

\echo '\n=== INDEX USAGE STATISTICS ==='
SELECT
  indexrelname AS index,
  tablename AS table,
  idx_scan AS scans,
  idx_tup_read AS tuples_read,
  idx_tup_fetch AS tuples_fetched,
  ROUND(100.0 * idx_tup_fetch / NULLIF(idx_tup_read, 0), 2) AS efficiency_pct
FROM pg_stat_user_indexes
JOIN pg_indexes ON indexrelname = indexname
WHERE pg_stat_user_indexes.schemaname = 'public'
ORDER BY idx_scan DESC;
EOF

# echo "DROP HAMMERDB SCHEMA"
# ./hammerdbcli py auto ./scripts/python/postgres/tproch/pg_tproch_deleteschema.py
# echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
echo "HAMMERDB RESULT"
./hammerdbcli py auto ./scripts/python/postgres/tproch/pg_tproch_result.py

# Save hammerdb result to correct folder
cp "${RESULTS_DIR}/benchmark_results_tproch.txt" "${RUN_DIR}/"

# Compress the entire run directory for easy download
tar -czvf "${RUN_DIR}_${INDEX_SETTING}.tar.gz" -C "${RUN_DIR}/.." "$(basename "${RUN_DIR}")"

echo "PostgreSQL metrics saved to: ${PG_METRICS_DIR}"
echo "Compressed metrics archive: ${RUN_DIR}.tar.gz"
