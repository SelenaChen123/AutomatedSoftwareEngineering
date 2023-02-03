global the
global help

the = {}
help = """
cluster.py : an example csv reader script
Copyright (c) 2023 MIT
Tim Menzies <timm@ieee.org>
Selena Chen <schen53@ncsu.edu>
Arun Ramesh <arames25@ncsu.edu>
Andrew Sauerbrei <amsauerb@ncsu.edu>

USAGE:   cluster.py  [OPTIONS] [-g ACTION]

OPTIONS:
  -d  --dump    on crash, dump stack   = false
  -f  --file    name of file           = ../../etc/data/auto93.csv
  -F  --Far     distance to "faraway"  = .95
  -g  --go      start-up action        = data
  -h  --help    show help              = false
  -m  --min     stop clusters at N^min = .5
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211
  -S  --Sample  sampling data size     = 512

ACTIONS:
"""
