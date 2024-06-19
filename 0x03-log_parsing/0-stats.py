#!/usr/bin/python3
"""[TODO:description]

[TODO:description]
"""


import re
import signal
import sys

status_counts = {}
total_size = 0
line_count = 0

# Validate input format
log_regex = re.compile(
    r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - "
    r'\[\S+ \S+\] "GET /projects/260 HTTP/1.1" '
    r"(\d{3}) (\d+)$"
)


# Signal handler for keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def print_stats():
    """[TODO:description]"""
    global total_size, status_counts
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


# Reading from stdin line by line
try:
    for line in sys.stdin:
        match = log_regex.match(line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            # Update total file size
            total_size += file_size

            # Update status code count
            if status_code not in status_counts:
                status_counts[status_code] = 0
            status_counts[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)

# Final statistics printout
print_stats()
