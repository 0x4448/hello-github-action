#!/usr/bin/env python3

import os
import sys

from datetime import datetime

print(f"Hello {sys.argv[1]}")

with open(os.environ["GITHUB_OUTPUT"], "a") as fp:
    fp.write(f"out-var1=The time is {datetime.now()}")
