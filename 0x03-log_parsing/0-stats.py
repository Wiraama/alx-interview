#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics: """
import sys


def print_metrics(total_size, status_counts):
    print("File size:", total_size)
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()


        if len(parts) >= 7 and parts[5] == '"GET' and parts[6] == '/projects/260':
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except (ValueError, IndexError):
                pass
        line_count += 1
        if line_count % 10 == 0:
            print_metrics(total_size, status_counts)

except KeyboardInterrupt:
    pass
finally:
    print_metrics(total_size, status_counts)
