#!/bin/tclsh
# maintainer: Pooja Jain
import os

print("SETTING CONFIGURATION")
dbset('db','pg')
dbset('bm','TPC-C')

diset('connection','pg_host','postgres')
diset('connection','pg_port','5432')
diset('connection','pg_sslmode','prefer')

vu = int(os.getenv('HAMMERDB_VU', 4))  # Default: 4 virtual users
warehouse = int(os.getenv('HAMMERDB_WAREHOUSES', 10))  # Default: 10 warehouses

diset('tpcc','pg_count_ware', warehouse)
diset('tpcc','pg_num_vu', vu)

diset('tpcc','pg_superuser','postgres')
diset('tpcc','pg_superuserpass','postgres')
diset('tpcc','pg_defaultdbase','postgres')

diset('tpcc','pg_user','tpcc')
diset('tpcc','pg_pass','tpcc')
diset('tpcc','pg_dbase','tpcc')
diset('tpcc','pg_tspace','pg_default')

diset('tpcc', 'pg_partition', 'true' if warehouse >= 200 else 'false')

print("SCHEMA BUILD STARTED")
buildschema()
print("SCHEMA BUILD COMPLETED")
exit()
