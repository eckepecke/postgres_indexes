SELECT 
  indexname AS index_name,
  tablename AS table_name,
  indexdef AS index_definition
FROM pg_indexes
WHERE schemaname = 'public'
  AND indexname NOT IN (
    -- Exclude indexes tied to primary keys
    SELECT conindid::regclass::text
    FROM pg_constraint
    WHERE contype = 'p'
  )
  AND array_length(string_to_array(indexdef, ','), 1) > 1; -- Multi-column indexes

SELECT 
  conname AS constraint_name,
  conrelid::regclass AS table_name,
  confrelid::regclass AS referenced_table
FROM pg_constraint
WHERE conindid IN (
  SELECT indexname::regclass
  FROM pg_indexes
  WHERE indexname IN ('customer_i2', 'orders_i2')
);

BEGIN; -- Start transaction for safety

DROP INDEX customer_i2;
DROP INDEX orders_i2;

COMMIT; -- Commit changes

SELECT 
  tablename,
  indexname,
  indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename;