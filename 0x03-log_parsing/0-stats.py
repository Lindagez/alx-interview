#!/usr/bin/python3

'''
    script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
'''
import sys

# initialize variables to store metrics
total_size = 0
stat_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    line_count = 0
    for line in sys.stdin:
        line = line.strip()

        # Check if the line matches the expected format
        parts = line.split()
        if len(parts) != 10 or parts[2] != "GET" or not parts[7].isdigit():
            continue

        # Extract file size and status code
        file_size = int(parts[7])
        status_code = int(parts[8])

        # Update metrics
        total_size += file_size
        stat_count[status_code] = stat_count.get(status_code, 0) + 1

        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")

            # Print status code counts in ascending order
            for code in sorted(stat_count.keys()):
                print(f"{code}: {stat_count[code]}")

    # Print final statistics when the loop ends
    print(f"Total file size: {total_size}")

    # Print status code counts in ascending order
    for code in sorted(stat_count.keys()):
        print(f"{code}: {stat_count[code]}")

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print("\nKeyboard interruption received. Printing current statistics:")

    print(f"Total file size: {total_size}")

    # Print status code counts in ascending order
    for code in sorted(stat_count.keys()):
        print(f"{code}: {stat_count[code]}")
