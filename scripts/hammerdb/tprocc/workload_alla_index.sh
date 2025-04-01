export TMP=`pwd`/TMP
mkdir -p $TMP

echo "BUILD HAMMERDB SCHEMA"
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
PGPASSWORD="tpcc" psql -h postgres -U tpcc -d tpcc <<EOF
-- Save metrics to CSV files
\copy (SELECT indexname, tablename, pg_relation_size(indexname::regclass) AS size_bytes, indexdef FROM pg_indexes WHERE schemaname = 'public') TO '/tmp/index_storage_tpcc.csv' CSV HEADER;
\copy (SELECT indexrelname, idx_scan, idx_tup_read, idx_tup_fetch FROM pg_stat_user_indexes WHERE schemaname = 'public') TO '/tmp/index_usage.csv' CSV HEADER;

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

SHOW enable_indexscan;
SHOW enable_bitmapscan;
SHOW enable_seqscan;

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