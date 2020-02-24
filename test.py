#!/usr/bin/env python3
"""
from lanimret import Color

print(f"{Color.fg.b_green}{Color.dec.underline}green{Color.bg.red}red bg{Color.reset}")
"""
import time
from lanimret import Cursor

cur = Cursor()

for i in range(101):
    print(f"{i}%", end="")
    time.sleep(0.05)
    cur.left(3)

# or
print("")

for i in range(101):
    print(f"{i}%", end="")
    time.sleep(0.05)
    cur.clear_line(2)
