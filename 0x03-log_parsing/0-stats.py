#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """

import sys


status_code = {"200": 0,\
               "301": 0,\
               "400": 0,\
               "401": 0,\
               "403": 0,\
               "404": 0,\
               "405": 0,\
               "500": 0}
count = 1
file_size = 0

def get_size(line):
    """ Get file size of each line """
    try:
        line_arr = line.split()
        code = line_arr[-2]
        if code in status_code.keys():
            status_code[code] += 1
        return int(line_arr[-1])
    except Exception:
        return 0

def print_metrics():
    """ Print line metrics """
    print("File size: {}".format(file_size))
    for key in sorted(status_code.keys()):
        if status_code[key]:
            print("{}: {}".format(key, status_code[key]))

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            file_size += get_size(line)
            if count % 10 == 0:
                print_metrics()
            count += 1
    except KeyboardInterrupt:
        print_metrics()
        raise
    print_metrics()
