slcsp.py  comments file:

# Introduction
This script will output a csv format to STDOUT containing requested zip codes and their 
LSCSP rate (unless that cannot be determined or does not exist).

# Requirements
PYTHON:
python 3x (tested on python3.9)

## Related Files:
Place the current slcsp.py file in the same directory as the required csv files:
* slcsp.csv,
* zips.csv, and
* plans.csv 
Please ensure the format for these files matches that specified below.

At the CLI run:
#> python slcsp.py 

# Output
The slcsp.csv file will be printed to STDOUT along with the SLCSP for the zipcode, if one 
can be determined from the available data.  If no single rate area can be determined, or no 
slcsp can be determined for the rate area a blank value will output.
If a rate can be found:
'12018',204.60
If no rate can be determined:
'12018',

## Capturing Output to Files
To capture the results to a new file, redirect output to a file:
#> python slcsp.py > results.csv
