-- Step 1: Identify all droppable multi-column indexes (non-PK)
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
-- Step 2: Generate and execute DROP statements
SELECT 
  format('
    -- Dropping index: %I on table %I (definition: %s)
    DROP INDEX IF EXISTS %I;
    ',
    index_name,
    table_name,
    index_definition,
    index_name
  ) AS drop_command
FROM droppable_indexes
\gexec

-- Step 3: Verify remaining indexes
SELECT 
  tablename AS table_name,
  indexname AS index_name, 
  indexdef AS index_definition,
  CASE 
    WHEN indexname IN (
      SELECT conindid::regclass::text 
      FROM pg_constraint 
      WHERE contype = 'p'
    ) THEN 'PRIMARY KEY'
    WHEN array_length(string_to_array(indexdef, ','), 1) = 1 THEN 'SINGLE-COLUMN'
    ELSE 'MULTI-COLUMN'
  END AS index_type
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY 
  table_name,
  index_type DESC;