#!/usr/bin/env python3

import re
import sys

src = open('Karty - List 1.csv', 'r').read()

src = re.sub(r'(?<!\r)\n', '<br>', src)

def use_entity(match):
    return "&#" + str(ord(match.group(0)[0])) + ";"

src = re.sub(r'[\x80-\u10FFFF]', use_entity, src)

print(src, file=open('Karty-fixed.csv', 'w'), end='')
