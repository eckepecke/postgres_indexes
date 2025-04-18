# export TMP=`pwd`/TMP
# mkdir -p $TMP
# echo "BUILD HAMMERDB SCHEMA"
# echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
# ./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_buildschema.py
# echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
# echo "CHECK HAMMERDB SCHEMA"
# echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
# ./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_checkschema.py
# echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
# echo "RUN HAMMERDB TEST"
# echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
# ./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_run.py
# echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
# echo "DROP HAMMERDB SCHEMA"
# ./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_deleteschema.py
# echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
# echo "HAMMERDB RESULT"
# ./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_result.py


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
-- 1. Drop non-PK multi-column indexes
WITH droppable_indexes AS (
  SELECT 
    indexname AS index_name,
    tablename AS table_name,
    indexdef AS index_definition
  FROM pg_indexes
  WHERE schemaname = 'public'
    AND indexname NOT IN (
      SELECT conindid::regclass::text
      FROM pg_constraint
      WHERE contype = 'p'
    )
    AND array_length(string_to_array(indexdef, ','), 1) > 1
)
SELECT 
  format('DROP INDEX IF EXISTS %I; -- Original: %s', index_name, index_definition) AS drop_command
FROM droppable_indexes
\gexec

-- 2. Create BRIN indexes (only on suitable columns)
CREATE INDEX IF NOT EXISTS idx_orders_entry_brin ON orders USING brin (o_entry_d) WITH (pages_per_range=32);
CREATE INDEX IF NOT EXISTS idx_customer_since_brin ON customer USING brin (c_since) WITH (pages_per_range=16);

-- 3. Update statistics and configure planner
ANALYZE orders;
ANALYZE customer;

-- Force BRIN usage for testing (not for production!)
SET enable_seqscan = off;
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM orders 
WHERE o_entry_d BETWEEN '2023-01-01' AND '2023-01-02';  -- Hypothetical range scan
RESET enable_seqscan;

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