#!/bin/tclsh
# maintainer: Pooja Jain
import os
tmpdir = os.getenv('TMP')

vu = int(os.getenv('HAMMERDB_VU', 4))  # Default: 4 virtual users
warehouse = int(os.getenv('HAMMERDB_WAREHOUSES', 10))  # Default: 10 warehouses

print("SETTING CONFIGURATION")
dbset('db','pg')
dbset('bm','TPC-C')

diset('connection','pg_host','postgres')
diset('connection','pg_port','5432')
diset('connection','pg_sslmode','prefer')

diset('tpcc', 'pg_count_ware', str(warehouse))  # Use env var
diset('tpcc', 'pg_num_vu', str(vu))            # Use env var (min 8 for PG)

diset('tpcc','pg_superuser','postgres')
diset('tpcc','pg_superuserpass','postgres')
diset('tpcc','pg_defaultdbase','postgres')
diset('tpcc','pg_user','tpcc')
diset('tpcc','pg_pass','tpcc')
diset('tpcc','pg_dbase','tpcc')
diset('tpcc','pg_driver','timed')
diset('tpcc','pg_total_iterations','10000000')
diset('tpcc','pg_rampup','2')
diset('tpcc','pg_duration','3') # Duration
diset('tpcc','pg_allwarehouse','false')
diset('tpcc','pg_timeprofile','true')
diset('tpcc','pg_vacuum','true')

# Load TPC-H script and inject planner flags
loadscript()


# loadscript()
print("TEST STARTED")
vuset('vu', vu)
vucreate()
tcstart()
tcstatus()
jobid = tclpy.eval('vurun')
vudestroy()
tcstop()
print("TEST COMPLETE")
file_path = os.path.join(tmpdir , "pg_tprocc" )
fd = open(file_path, "w")
fd.write(jobid)
fd.close()
exit()
