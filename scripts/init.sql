-- init.sql
CREATE USER tpcc WITH PASSWORD 'tpcc';
CREATE DATABASE tpcc OWNER tpcc;
GRANT ALL PRIVILEGES ON DATABASE tpcc TO tpcc;

-- Connect to `tpcc` and create extensions
\c tpcc
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;