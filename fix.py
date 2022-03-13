#!/usr/bin/env python3

import sys

for line in sys.stdin:
    fixed_line = ""
    end_of_line = line.endswith("\r\n")
    for char in line.strip():
        if char == '\n':
            fixed_line = fixed_line + '<br>'
        if ord(char) < 128:
            fixed_line = fixed_line + char
        else:
            fixed_line = fixed_line + "&#" + str(ord(char)) + ";"
    if not end_of_line:
        fixed_line = fixed_line + '<br>'
    print(fixed_line, end='\n' if end_of_line else '')
