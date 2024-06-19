#!/usr/bin/python3
"""
Module contains the method print_stats that parse the log
"""

import re
import signal
import sys
from collections import defaultdict

total_size = 0
status_codes = defaultdict(int)
line_count = 1

# Regular expression pattern for the log lines
log_pattern = re.compile(
    r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
    r'\[(.*?)\] "GET /projects/260 HTTP/1\.1" '
    r"(\d{3}) (\d+)"
)


def print_stats(signum=None, frame=None):
    """Function to print the statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
    if signum is not None:
        sys.exit(0)


# Set up signal handling for CTRL+C
signal.signal(signal.SIGINT, print_stats)

# Read from stdin line by line
try:
    for line in sys.stdin:
        try:
            match = log_pattern.match(line)
            if match:
                total_size += int(match.group(4))
                status_codes[match.group(3)] += 1
                line_count += 1
            if line_count % 10 == 0:
                print_stats()
        except Exception:
            pass

except KeyboardInterrupt:
    pass

finally:
    print_stats()
