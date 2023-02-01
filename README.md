# AutomatedSoftwareEngineering

[![Test](https://github.com/SelenaChen123/AutomatedSoftwareEngineering/actions/workflows/tests.yml/badge.svg)](https://github.com/SelenaChen123/AutomatedSoftwareEngineering/actions/workflows/tests.yml)
[![Repo Size](https://img.shields.io/github/repo-size/SelenaChen123/AutomatedSoftwareEngineering)](https://github.com/SelenaChen123/AutomatedSoftwareEngineering)
[![Code Size](https://img.shields.io/github/languages/code-size/SelenaChen123/AutomatedSoftwareEngineering)](https://github.com/SelenaChen123/AutomatedSoftwareEngineering)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/589330639.svg)](https://zenodo.org/badge/latestdoi/589330639)

Coursework for NCSU's Spring 2023 CSC 591 021 course, based on the instructor's semi-supervised, multi-objective, model-based explanation system written in Lua.

## Repo Structure

```
├── .github
│   └── workflows
│       └── tests.yml       # Runs tests on each push and reports failures
├── docs                    # HTML documentation files for each homework
│   ├── Homework1
│   |   └── ...
│   ├── Homework2
│   |   └── ...
│   └── Homework3
│       └── ...
├── etc
│   ├── data                # Input data files for the scripts
│   |   └── ...
│   └── out                 # Output of the scripts
│       └── ...
├── src                     # Python source code for each homework
│   ├── Homework1
│   |   └── ...
│   ├── Homework2
│   |   └── ...
│   └── Homework3
│       └── ...
├── .gitignore              # List of files to never commit
├── CITATION.cff            # Bibliography information
├── LICENSE.md              # MIT license
└── README.md               # Top-level repo documentation

```

## Installation Instructions

1. Download and install the latest [Python](https://www.python.org/downloads/) version (Python 3.11). Check your Python version using: 

    `python --version`

2. Clone the repository from:

    `https://github.com/SelenaChen123/AutomatedSoftwareEngineering`

## How to Run the Scripts

1. Navigate to the scripts by running:

    `cd src/[folder]`

    where `folder` is the name of the folder containing the scripts.

2. Run the script by calling:
  
    `python main.py [OPTIONS] [-g ACTION]`

3. To get the list of options and actions, run:
   
    `python main.py -h`
  
4. To run all tests, run:
  
   `python main.py -g all`

5. To run a specific test, run:
  
   `python main.py -g [TEST]`

## Contributors

- <a href="https://github.com/SelenaChen123" target="_blank">Selena Chen</a>
- <a href="https://github.com/Arun152k" target="_blank">Arun Kumar Ramesh</a>
- <a href="https://github.com/amsauerb" target="_blank">Andrew Sauerbrei</a>
