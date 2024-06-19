#!/usr/bin/python3
"""
Module contains the method print_stats that parse the log
"""
import signal
import sys
from collections import defaultdict

# Initialize variables
total_size = 0
status_codes = defaultdict(int)
line_count = 0


def print_stats():
    """[TODO:description]"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """[TODO:description]

    Args:
        sig ([TODO:parameter]): [TODO:description]
        frame ([TODO:parameter]): [TODO:description]
    """
    print_stats()
    sys.exit(0)


# Handle Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            size = int(parts[-1])
            code = parts[-2]

            if code in status_codes:
                status_codes[code] += 1

            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except Exception:
            pass

except KeyboardInterrupt:
    pass

finally:
    print_stats()
