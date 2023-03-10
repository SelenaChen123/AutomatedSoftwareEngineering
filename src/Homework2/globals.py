global the
global help

"""
Contains the help text and a dictionary of the global option values from the command line.
"""

the = {}
help = """
data.py : an example csv reader script
Copyright (c) 2023 MIT
Tim Menzies <timm@ieee.org>
Selena Chen <schen53@ncsu.edu>
Arun Ramesh <arames25@ncsu.edu>
Andrew Sauerbrei <amsauerb@ncsu.edu>

USAGE:   data.py  [OPTIONS] [-g ACTION]

OPTIONS:
  -d  --dump  on crash, dump stack = false
  -f  --file  name of file         = ../../etc/data/auto93.csv
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211

ACTIONS:
"""
