#!/usr/bin/env python
"""lanimret v1.00"""

import subprocess
import sys


class AltScreen:
    """provide controls for the terminal's alternate screen"""

    def show(self):
        """show terminal's alternate screen"""
        subprocess.call("tput smcup", shell=True)

    def close(self):
        """close terminal's alternate screen"""
        subprocess.call("tput rmcup", shell=True)

    access = {
        "show": show,
        "close": close
        }


class Color:
    """easily access ANSI color/decorator codes"""

    class fg:
        """foreground formatting"""

        black = "\u001b[30m"
        red = "\u001b[31m"
        green = "\u001b[32m"
        yellow = "\u001b[33m"
        blue = "\u001b[34m"
        magenta = "\u001b[35m"
        cyan = "\u001b[36m"
        white = "\u001b[37m"
        b_black = "\u001b[30;1m"
        b_red = "\u001b[31m;1"
        b_green = "\u001b[32;1m"
        b_yellow = "\u001b[33;1m"
        b_blue = "\u001b[34;1m"
        b_magenta = "\u001b[35;1m"
        b_cyan = "\u001b[36;1m"
        b_white = "\u001b[37;1m"

        access = {
            "black": black,
            "red": red,
            "green": green,
            "yellow": yellow,
            "blue": blue,
            "magenta": magenta,
            "cyan": cyan,
            "white": white,
            "b_black": b_black,
            "b_red": b_red,
            "b_green": b_green,
            "b_yellow": b_yellow,
            "b_blue": b_blue,
            "b_magenta": b_magenta,
            "b_cyan": b_cyan,
            "b_white": b_white
            }

    class bg:
        """background formatting"""

        black = "\u001b[40m"
        red = "\u001b[41m"
        green = "\u001b[42m"
        yellow = "\u001b[44m"
        blue = "\u001b[44m"
        magenta = "\u001b[45m"
        cyan = "\u001b[46m"
        white = "\u001b[47m"
        b_black = "\u001b[40;1m"
        b_red = "\u001b[41m;1"
        b_green = "\u001b[42;1m"
        b_yellow = "\u001b[44;1m"
        b_blue = "\u001b[44;1m"
        b_magenta = "\u001b[45;1m"
        b_cyan = "\u001b[46;1m"
        b_white = "\u001b[47;1m"

        access = {
            "black": black,
            "red": red,
            "green": green,
            "yellow": yellow,
            "blue": blue,
            "magenta": magenta,
            "cyan": cyan,
            "white": white,
            "b_black": b_black,
            "b_red": b_red,
            "b_green": b_green,
            "b_yellow": b_yellow,
            "b_blue": b_blue,
            "b_magenta": b_magenta,
            "b_cyan": b_cyan,
            "b_white": b_white
            }

    class dec:
        """decorator formatting"""

        bold = "\u001b[1m"
        underline = "\u001b[4m"
        reverse = "\u001b[7m"

        access = {
            "bold": bold,
            "underline": underline,
            "reverse": reverse
            }

    reset = "\u001b[0m"
    access = {"fg": fg, "bg": bg, "reset": reset}


class Cursor:
    """provide controls for terminal cursor"""

    def left(self, num):
        """move cursor num times left"""
        sys.stdout.write(f"\u001b[{num}D")
        sys.stdout.flush()

    def right(self, num):
        """move cursor num times right"""
        sys.stdout.write(f"\u001b[{num}C")
        sys.stdout.flush()

    def up(self, num):
        """move cursor num times up"""
        sys.stdout.write(f"\u001b[{num}A")
        sys.stdout.flush()

    def down(self, num):
        """move cursor num times down"""
        sys.stdout.write(f"\u001b[{num}B")
        sys.stdout.flush()

    def clear_screen(self, num):
        """clear screen"""
        if num not in [0, 1, 2]:
            raise ValueError("Cursor.clear_screen only takes (0, 1, 2)")
        sys.stdout.write(f"\u001b[{num}J")
        sys.stdout.flush()

    def clear_line(self, num):
        """clear current line"""
        if num not in [0, 1, 2]:
            raise ValueError("Cursor.clear_line only takes (0, 1, 2)")
        if num == 2:
            sys.stdout.write(f"\u001b[{num}K\n")
            sys.stdout.flush()
            self.up(1)
        else:
            sys.stdout.write(f"\u001b[{num}K")
            sys.stdout.flush()

    access = {
        "left": left,
        "right": right,
        "up": up,
        "down": down,
        "clear_screen": clear_screen,
        "clear_line": clear_line
        }
