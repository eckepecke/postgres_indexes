EXPLAIN ANALYZE
SELECT l_orderkey, l_shipdate, l_receiptdate
FROM lineitem
WHERE l_shipdate BETWEEN '1998-01-01' AND '1998-01-05'
  AND l_receiptdate < '1998-02-01';

  EXPLAIN ANALYZE
SELECT o_custkey, COUNT(*)
FROM orders
WHERE o_orderdate BETWEEN '1998-01-01' AND '1998-12-31'
GROUP BY o_custkey;

EXPLAIN ANALYZE
SELECT c_name, c_phone
FROM customer
WHERE c_nationkey = 7 AND c_mktsegment = 'AUTOMOBILE';

EXPLAIN ANALYZE
SELECT p_partkey, p_retailprice
FROM part
WHERE p_brand = 'Brand#12' AND p_type = 'SMALL POLISHED STEEL' AND p_size = 5;

EXPLAIN ANALYZE
SELECT ps_availqty
FROM partsupp
WHERE ps_partkey = 12345 AND ps_suppkey = 678;

EXPLAIN ANALYZE
SELECT s_name, s_acctbal
FROM supplier
WHERE s_nationkey = 5
ORDER BY s_acctbal DESC
LIMIT 10;