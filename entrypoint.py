#!/usr/bin/env python3

import os
import sys

from datetime import datetime

print(f"Hello {sys.argv[1]}")
print(f"GITHUB_TOKEN length: {len(os.environ.get('GITHUB_TOKEN', ''))}")

for key in sorted(os.environ.keys()):
    print(key)

with open(os.environ["GITHUB_OUTPUT"], "a") as fp:
    fp.write(f"out-var1=The time is {datetime.now()}")
