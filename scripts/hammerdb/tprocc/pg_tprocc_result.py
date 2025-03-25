# import os
# tmpdir = os.getenv('TMP')
# outputfile = os.path.join(tmpdir, 'pg_tprocc' )
# exec(open('./scripts/python/generic/generic_tprocc_result.py').read())
# exit()

import os
import sys

tmpdir = os.getenv('TMP')
outputfile = os.path.join(tmpdir, 'pg_tprocc')
result_file = os.path.join(tmpdir, 'benchmark_results.txt')  # New results file

# Redirect standard output to a file
with open(result_file, 'w') as f:
    original_stdout = sys.stdout
    sys.stdout = f
    try:
        exec(open('./scripts/python/generic/generic_tprocc_result.py').read())
    finally:
        sys.stdout = original_stdout

exit()