# AutomatedSoftwareEngineering

[![Test](https://github.com/SelenaChen123/AutomatedSoftwareEngineering/actions/workflows/tests.yml/badge.svg)](https://github.com/SelenaChen123/AutomatedSoftwareEngineering/actions/workflows/tests.yml)
[![Repo Size](https://img.shields.io/github/repo-size/SelenaChen123/AutomatedSoftwareEngineering)](https://github.com/SelenaChen123/AutomatedSoftwareEngineering)
[![Code Size](https://img.shields.io/github/languages/code-size/SelenaChen123/AutomatedSoftwareEngineering)](https://github.com/SelenaChen123/AutomatedSoftwareEngineering)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Coursework for CSC 591

A Python-based command-line parser to read and manipulate .csv files developed based on the lua script shared in class.

## HW1
Implemented NUM and SYM Classes to read Numeric and Symbolic Columns of a .csv file respectively.

## HW2
Implemented COLS and DATA Classes that helps to create and store NUM and SYM objects.

## Step to set-up and run the HW in your local machine

1. Download and install the latest [Python](https://www.python.org/downloads/) version

2. Check your Python version using: 

   `python --version`

3. Clone the repository using:

    `https://github.com/SelenaChen123/AutomatedSoftwareEngineering`

4. Go to the specific Homework folder. For instance if you you want to run tests in HW1, use:
  
    `cd src\docs\Homework1`
   
     All Homework files are in the src folder 

5. To get help:
   
    `python main.py -h` 

6. To run a specific Test:
  
   `python main.py -g <test-case-name>`
  
    To run all Test case:
  
   `python main.py -g all`
