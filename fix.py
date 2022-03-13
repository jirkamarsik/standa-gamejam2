#!/usr/bin/env python3

import re
import sys

in_file = sys.argv[1] if len(sys.argv) >= 2 else 'Karty - List 1.csv'
out_file = re.sub(r'(.*)\.csv', r'\1 - fixed.csv', in_file)

# Read
csv = open(in_file, 'r', newline='').read()

# Fix newlines
csv = re.sub(r'[^\r]\n', r'<br>', csv)

# Fix non-ASCII chars
def use_entity(match):
    return "&#" + str(ord(match.group(0)[0])) + ";"

csv = re.sub(r'[\x80-\u10FFFF]', use_entity, csv)

# Write
print(csv, file=open(out_file, 'w'), end='')
