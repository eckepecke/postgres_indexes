# import os
# tmpdir = os.getenv('TMP')
# outputfile = os.path.join(tmpdir, 'pg_tprocc' )
# exec(open('./scripts/python/generic/generic_tprocc_result.py').read())
# exit()

##################################
#  This works
# import os
# import sys

# tmpdir = os.getenv('TMP')
# outputfile = os.path.join(tmpdir, 'pg_tprocc')
# result_file = os.path.join(tmpdir, 'benchmark_results.txt')  # New results file

# result_folder = os.getenv('RESULT_DIR')


# # Redirect standard output to a file
# with open(result_file, 'w') as f:
#     original_stdout = sys.stdout
#     sys.stdout = f
#     try:
#         exec(open('./scripts/python/generic/generic_tprocc_result.py').read())
#     finally:
#         sys.stdout = original_stdout



# exit()

import os
import sys

tmpdir = os.getenv('TMP')
outputfile = os.path.join(tmpdir, 'pg_tprocc')
result_file = os.path.join(tmpdir, 'benchmark_results.txt')  # New results file

result_folder = os.getenv('RESULTS_DIR', '/home/HammerDB-4.12/hammerdb_results')

# Ensure result_folder is valid
if result_folder:
    result_file = os.path.join(result_folder, 'benchmark_results.txt')

# Redirect standard output to a file
with open(result_file, 'w') as f:
    original_stdout = sys.stdout
    sys.stdout = f
    try:
        exec(open('./scripts/python/generic/generic_tprocc_result.py').read())
    finally:
        sys.stdout = original_stdout

exit()
##################################

# import os
# import sys
# from datetime import datetime

# # Get timestamp FIRST
# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# # Configure paths
# results_dir = os.getenv('RESULTS_DIR', '/home/HammerDB-4.12/hammerdb_results').strip('"\'')
# os.makedirs(results_dir, exist_ok=True)  # Create dir if missing

# # 1. FIRST CREATE THE pg_tprocc FILE (from your run script)
# jobid_file = os.path.join(results_dir, f'pg_tprocc_{timestamp}')
# with open(jobid_file, 'w') as f:  # <-- This was missing
#     # Replace this with your actual job ID content
#     f.write("your_job_id_here")  

# # 2. THEN PROCESS RESULTS
# result_file = os.path.join(results_dir, f'benchmark_results_{timestamp}.txt')

# with open(result_file, 'w') as f:
#     sys.stdout = f
#     try:
#         # Use absolute path for reliability
#         script_path = '/home/HammerDB-4.12/scripts/python/generic/generic_tprocc_result.py'
#         exec(open(script_path).read()) 
#     finally:
#         sys.stdout = sys.__stdout__

# print(f"Job ID file created: {jobid_file}")
# print(f"Results saved to: {result_file}")
# exit()