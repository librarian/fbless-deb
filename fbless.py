#!/usr/bin/env python2.5
# -*- mode: python; coding: UTF-8; -*-
# (c) Con Radchenko mailto:lankier@gmail.com

import sys
import locale
from io import StringIO
import curses
from fbless_lib.main import MainWindow

stdout = sys.stdout
sys.stdout = StringIO()

## stderr = sys.stderr
## sys.stderr = StringIO()
locale.setlocale(locale.LC_ALL, '')

try:
    MainWindow().main_loop()
finally:
    try:
        curses.endwin()
    except:
        pass

value = sys.stdout.getvalue()
if value:
    print >> stdout, value

## value = sys.stderr.getvalue()
## if value:
##     print >> stderr, value
