#!/usr/bin/python3
"""This module contains a script"""
import re
import sys


def printstats(total_size, status_tally):
    """Prints the total file size(should be called after 10 lines)
    and the total number of times a status code has been shown
    in stdin"""
    print(f"File size: {total_size}")
    for code in [200, 301, 400, 401, 403, 404, 405, 500]:
        if code in status_tally:
            print(f"{code}: {status_tally[code]}")


if __name__ == "__main__":
    """reads stdin line by line and parses it if it follows
    a specific input format"""
    count = 0
    size = 0
    status_tally = {}
    pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2}\ - \d{2}:\d{2}:\d{2}.\d{6}\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d{1,4})"
    try:
        for line in sys.stdin:
            match = re.match(pattern, line)
            if match:
                count += 1
                size += int(match.group(2))
                code = int(match.group(1))
                status_tally[code] = status_tally.get(code, 0) + 1
                if count % 10 == 0:
                    printstats(size, status_tally)
    except KeyboardInterrupt:
        printstats(size, status_tally)
