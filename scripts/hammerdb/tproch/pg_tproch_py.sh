export TMP=`pwd`/TMP
mkdir -p $TMP
echo "BUILD HAMMERDB SCHEMA"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
./hammerdbcli py auto ./scripts/python/postgres/tproch/pg_tproch_buildschema.py
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
echo "CHECK HAMMERDB SCHEMA"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
./hammerdbcli py auto ./scripts/python/postgres/tproch/pg_tproch_checkschema.py
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"

PGPASSWORD="tpch" psql -h postgres -U tpch -d tpch <<EOF
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

-- 2. Create BRIN indexes for TPC-H pattern
CREATE INDEX IF NOT EXISTS idx_lineitem_shipdate_brin ON lineitem USING brin (l_shipdate) WITH (pages_per_range=16);
CREATE INDEX IF NOT EXISTS idx_lineitem_commitdate_brin ON lineitem USING brin (l_commitdate) WITH (pages_per_range=32);
CREATE INDEX IF NOT EXISTS idx_orders_orderdate_brin ON orders USING brin (o_orderdate) WITH (pages_per_range=16);
CREATE INDEX IF NOT EXISTS idx_part_retailprice_brin ON part USING brin (p_retailprice) WITH (pages_per_range=64);


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


echo "RUN HAMMERDB TEST"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
./hammerdbcli py auto ./scripts/python/postgres/tproch/pg_tproch_run.py
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"

echo "CAPTURE INDEX METRICS"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
PGPASSWORD="tpch" psql -h postgres -U tpch -d tpch <<EOF
-- Save metrics to CSV files
\copy (SELECT indexname, tablename, pg_relation_size(indexname::regclass) AS size_bytes, indexdef FROM pg_indexes WHERE schemaname = 'public') TO '/tmp/index_storage_tpch.csv' CSV HEADER;
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
./hammerdbcli py auto ./scripts/python/postgres/tproch/pg_tproch_deleteschema.py
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
echo "HAMMERDB RESULT"
./hammerdbcli py auto ./scripts/python/postgres/tproch/pg_tproch_result.py
