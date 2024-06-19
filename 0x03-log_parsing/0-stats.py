#!/usr/bin/python3

import sys
from collections import defaultdict


def print_stats(status_codes, total_size):
    """
    Function to print the statistics
    Args:
        status_codes: dict of status codes
        total_size: total size of the files
    """
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


status_codes = defaultdict(int)
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        parsed_line = line.split()
        if len(parsed_line) > 2:
            counter += 1
            total_size += int(parsed_line[-1])  # file size
            code = parsed_line[-2]  # status code

            if code in status_codes:
                status_codes[code] += 1

            if counter % 10 == 0:
                print_stats(status_codes, total_size)

finally:
    print_stats(status_codes, total_size)
