"""
Contains the help text, a dictionary of the global option values from the command line, and a global random seed value.
"""

the = {}
help = """
xpln.py : multi-goal semi-supervised explanation
Copyright (c) 2023 MIT
Tim Menzies <timm@ieee.org>
Selena Chen <schen53@ncsu.edu>
Arun Ramesh <arames25@ncsu.edu>
Andrew Sauerbrei <amsauerb@ncsu.edu>

USAGE: xpln.py  [OPTIONS] [-g ACTION]

OPTIONS:
  -b  --bins    initial number of bins           = 16
  -c  --cliffs  cliff's delta threshold          = .147
  -d  --d       different is over sd*d           = .35
  -f  --file    data file                        = ../../etc/data/auto93.csv
  -F  --Far     distance to distant              = .95
  -g  --go      start-up action                  = nothing
  -h  --help    show help                        = false
  -H  --Halves  search space for clustering      = 512
  -m  --min     size of smallest cluster         = .5
  -M  --Max     numbers                          = 512
  -p  --p       dist coefficient                 = 2
  -r  --rest    how many of rest to sample       = 4
  -R  --Reuse   child splits reuse a parent pole = true
  -s  --seed    random number seed               = 937162211

ACTIONS:
"""
seed = 937162211
