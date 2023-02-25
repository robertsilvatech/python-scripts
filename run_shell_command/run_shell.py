#!/usr/bin/env python
#
# Author: Robert Silva
#

import subprocess

cmd = 'ls -lh'
result = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
error = result.stderr.readlines()
output = result.stdout.readlines()
if error:
    print('Problems found')
    for line in error:
        print(line)
else:
    count = 0
    for line in output:
        line_result = line.decode('UTF-8').replace('\n','')
        count += 1
        print(f'Line {count}: {line_result}')
