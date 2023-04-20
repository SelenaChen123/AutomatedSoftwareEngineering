"""
Contains the help text, a dictionary of the global option values from the command line, and a global random seed value.
"""

Is = {}
help = """
xpln.py : multi-goal semi-supervised explanation
Copyright (c) 2023 MIT
Tim Menzies <timm@ieee.org>
Selena Chen <schen53@ncsu.edu>
Arun Ramesh <arames25@ncsu.edu>
Andrew Sauerbrei <amsauerb@ncsu.edu>

USAGE: xpln.py  [OPTIONS] [-g ACTION]

OPTIONS:
  -a  --all       run all datasets                 = false
  -b  --bins      initial number of bins           = 16
  -B  --bootstrap bootstrap samples                = 512
  -c  --cliffs    cliff's delta threshold          = .147
  -co --conf      confidence                       = .05
  -cl --cliff     cliff's delta threshold v2       = .4
  -C  --cohen     cohen's constant                 = .35
  -d  --d         different is over sd*d           = .35
  -f  --file      data file                        = ../../etc/data/auto93.csv
  -F  --Far       distance to distant              = .95
  -g  --go        start-up action                  = nothing
  -h  --help      show help                        = false
  -H  --Halves    search space for clustering      = 512
  -m  --min       size of smallest cluster         = .5
  -M  --Max       numbers                          = 512
  -p  --p         dist coefficient                 = 2
  -r  --rest      how many of rest to sample       = 4
  -R  --Reuse     child splits reuse a parent pole = true
  -s  --seed      random number seed               = 937162211
  -w  --width     plot width                       = 40

ACTIONS:
"""


seed = 937162211


datasets = [
    "auto2.csv",
    "auto93.csv",
    "china.csv",
    "coc1000.csv",
    "coc10000.csv",
    "healthCloseIsses12mths0001-hard.csv",
    "healthCloseIsses12mths0011-easy.csv",
    "nasa93dem.csv",
    "pom.csv",
    "SSM.csv",
    "SSN.csv"
]
