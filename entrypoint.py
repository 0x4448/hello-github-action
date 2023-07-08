#!/usr/bin/env python3

import os
import sys

from datetime import datetime

print(f"Hello {sys.argv[0]}")
print(f"GITHUB_OUTPUT: {os.environ.get('GITHUB_OUTPUT')}")
