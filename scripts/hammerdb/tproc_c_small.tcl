#!/bin/hammerdbcli
dbset db pg
diset connection pg_host exjobb-postgres-1  # Use your PostgreSQL container name
diset connection pg_port 5432
diset connection pg_user admin
diset connection pg_password admin
diset tpcc pg_dbase benchmarkdb
diset tpcc pg_count_ware 1  # Tiny dataset (1 warehouse)
build  # Generates schema and data