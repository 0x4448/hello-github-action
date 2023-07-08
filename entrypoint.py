#!/usr/bin/env python3

import os
import sys

from datetime import datetime
from pathlib import Path

print(f"Hello {sys.argv[1]}")

token = Path("/run/secrets/github_token")
print(f"token: {token.exists()}")

if token.exists():
    with open(token) as fp:
        line = fp.readline()
        print(line[0:4])

with open(os.environ["GITHUB_OUTPUT"], "a") as fp:
    fp.write(f"out-var1=The time is {datetime.now()}")
