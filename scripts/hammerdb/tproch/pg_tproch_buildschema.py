#!/bin/tclsh
# maintainer: Pooja Jain
import os

print("SETTING CONFIGURATION")
dbset('db','pg')
dbset('bm','TPC-H')

diset('connection','pg_host','postgres')
diset('connection','pg_port','5432')
diset('connection','pg_sslmode','prefer')

vu = int(os.getenv('HAMMERDB_VU', 4))  # Default: 4 virtual users
# vu = tclpy.eval('numberOfCPUs')
diset('tpch','pg_scale_fact','1')
diset('tpch','pg_num_tpch_threads',vu)
diset('tpch','pg_tpch_superuser','postgres')
diset('tpch','pg_tpch_superuserpass','postgres')
diset('tpch','pg_tpch_defaultdbase','postgres')
diset('tpch','pg_tpch_user','tpch')
diset('tpch','pg_tpch_pass','tpch')
diset('tpch','pg_tpch_dbase','tpch')
diset('tpch','pg_tpch_tspace','pg_default')

print("SCHEMA BUILD STARTED")
buildschema()
print("SCHEMA BUILD COMPLETED")
exit()
