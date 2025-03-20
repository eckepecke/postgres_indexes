#!/bin/tclsh
# maintainer: Pooja Jain

print("SETTING CONFIGURATION")
dbset('db','pg')
dbset('bm','TPC-C')

diset('connection','pg_host','postgres')
diset('connection','pg_port','5432')
diset('connection','pg_sslmode','prefer')

# vu = tclpy.eval('numberOfCPUs')
# warehouse = int(vu) * 5
# diset('tpcc','pg_count_ware',warehouse)
# diset('tpcc','pg_num_vu',vu)

# Override CPU-based calculation for better control
vu = 4                          # Example: 4 virtual users (adjust based on your needs)
warehouse = 10                  # Example: 10 warehouses (start small for testing)
diset('tpcc','pg_count_ware', warehouse)
diset('tpcc','pg_num_vu', vu)

diset('tpcc','pg_superuser','postgres')
diset('tpcc','pg_superuserpass','postgres')
diset('tpcc','pg_defaultdbase','postgres')

diset('tpcc','pg_user','tpcc')
diset('tpcc','pg_pass','tpcc')
diset('tpcc','pg_dbase','tpcc')
diset('tpcc','pg_tspace','pg_default')

# if (warehouse >= 200): 
#     diset('tpcc','pg_partition','true') 
# else:
#     diset('tpcc','pg_partition','false') 

# 🚀 Partitioning (Disable for small datasets)
diset('tpcc','pg_partition','false') # Keep false if warehouses < 200

print("SCHEMA BUILD STARTED")
buildschema()
print("SCHEMA BUILD COMPLETED")
exit()
