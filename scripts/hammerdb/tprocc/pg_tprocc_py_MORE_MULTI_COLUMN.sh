export TMP=`pwd`/TMP
mkdir -p $TMP

INDEX_SETTING="MORE_MULTI_COLUMN"
TIMESTAMP=$(TZ="Europe/Stockholm" date +"%Y%m%d_%H%M%S")
RUN_DIR="${RESULTS_DIR}/${INDEX_SETTING}/${TIMESTAMP}"
PG_METRICS_DIR="${RUN_DIR}/postgres_metrics"
mkdir -p ${PG_METRICS_DIR}

echo "BUILD HAMMERDB SCHEMA WITH ${INDEX_SETTING}"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_buildschema.py

echo "DROP NON-PK MULTI-COLUMN INDEXES"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
# 2. Drop non-PK multi-column indexes
echo "DROP NON-PK MULTI-COLUMN INDEXES"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
PGPASSWORD="tpcc" psql -h postgres -U tpcc -d tpcc <<EOF


-- 2. Create HASH indexes (only on suitable columns)
\echo '=== Adding more multi-column Indexes ==='


-- For Payment Transaction:
CREATE INDEX customer_c_last_idx ON customer USING btree (c_w_id, c_d_id, c_last, c_first);

-- For Delivery Transaction:
CREATE INDEX new_order_combo_idx ON new_order USING btree (no_w_id, no_d_id, no_o_id);

-- For Stock-Level Transaction:
CREATE INDEX stock_level_idx ON stock USING btree (s_w_id, s_quantity);

SHOW enable_indexscan;
SHOW enable_bitmapscan;
SHOW enable_seqscan;


-- 4. Verify index state
\echo '=== Current Indexes ==='
SELECT 
  indexname AS name,
  tablename AS table,
  indexdef AS definition
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;
EOF


echo "CHECK HAMMERDB SCHEMA"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_checkschema.py

echo "RUN HAMMERDB TEST"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_run.py

echo "CAPTURE INDEX METRICS"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"

# Define output files
INDEX_STORAGE_DETAILS="${PG_METRICS_DIR}/index_storage_tpcc.csv"
INDEX_USAGE_DETAILS="${PG_METRICS_DIR}/index_usage_tpcc.csv"
STORAGE_OVERVIEW="${PG_METRICS_DIR}/index_storage_overview_tpcc.csv"
USAGE_STATISTICS="${PG_METRICS_DIR}/index_usage_statistics_tpcc.csv"
PG_SETTINGS="${PG_METRICS_DIR}/postgres_settings_tpcc.txt"
FULL_REPORT="${PG_METRICS_DIR}/full_report_tpcc.txt"

# Capture all output to a full report file
exec > >(tee "${FULL_REPORT}") 2>&1

PGPASSWORD="tpcc" psql -h postgres -U tpcc -d tpcc <<EOF
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

\echo '\n=== DATABASE SETTINGS ==='
SHOW enable_indexscan;
SHOW enable_bitmapscan;
SHOW enable_seqscan;
SHOW work_mem;
SHOW maintenance_work_mem;
SHOW random_page_cost;
SHOW effective_cache_size;

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

echo "DROP HAMMERDB SCHEMA"
./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_deleteschema.py
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
echo "HAMMERDB RESULT"
./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_result.py

# Save hammerdb result to correct folder
cp "${RESULTS_DIR}/benchmark_results_tprocc.txt" "${RUN_DIR}/"

# Compress the metrics files for easy download
tar -czvf "${RUN_DIR}.tar.gz" -C "${RESULTS_DIR}" "$(basename "${RUN_DIR}")"

echo "PostgreSQL metrics saved to: ${PG_METRICS_DIR}"
echo "Compressed metrics archive: ${RUN_DIR}.tar.gz"