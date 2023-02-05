global the
global help

"""
Contains the flags for the command line args
Contains a dictionary that is used to help parse and use
  the flags that the command line specifies
"""

the = {}
help = """
script.py : an example script with help text and a test suite
Copyright (c) 2023 MIT
Tim Menzies <timm@ieee.org>
Selena Chen <schen53@ncsu.edu>
Arun Ramesh <arames25@ncsu.edu>
Andrew Sauerbrei <amsauerb@ncsu.edu>

USAGE:   script.py  [OPTIONS] [-g ACTION]

OPTIONS:
  -d  --dump    on crash, dump stack = false
  -g  --go      start-up action      = data
  -h  --help    show help            = false
  -s  --seed    random number seed   = 937162211

ACTIONS:
"""
