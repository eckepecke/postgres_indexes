import os
import sys

tmpdir = os.getenv('TMP')
outputfile = os.path.join(tmpdir, 'pg_tprocc')
result_file = os.path.join(tmpdir, 'benchmark_results_tprocc.txt')  # New results file

result_folder = os.getenv('RESULTS_DIR', '/home/HammerDB-4.12/hammerdb_results')

# Ensure result_folder is valid
if result_folder:
    result_file = os.path.join(result_folder, 'benchmark_results_tprocc.txt')

# Redirect standard output to a file
with open(result_file, 'w') as f:
    original_stdout = sys.stdout
    sys.stdout = f
    try:
        exec(open('./scripts/python/generic/generic_tprocc_result.py').read())
    finally:
        sys.stdout = original_stdout

exit()
