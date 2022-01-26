# Introduction
This script will output a csv format to STDOUT containing requested zip codes (from slcsp.csv) and their 
SLCSP rate (unless that cannot be determined or does not exist).

The rate field will be blank if:
* the zipcode belongs to more than 1 rate-area
* there is no silver plan, or only one price available for silver plans - only unique rates are considered, and if there is no second lowest cost, we cannot return it.

# Requirements
Python:
* python 3x (tested on python 3.5 and python 3.9)

## Related Files:
The script, *slcsp.py*, uses data from 2 input files, *plans.csv* and *zips.csv*.  Rates
are output based on the zipcodes listed in *slcsp.csv*.  
Place the script file, slcsp.py, in the same directory as the required csv files:  
* slcsp.csv,
* zips.csv, and
* plans.csv 

# Running the Script
At the CLI run:

```#> python3 slcsp.py ```

The script may also be executed from the CLI, if given execution and if the system's env is correctly configured for python3.  

# Output
The slcsp.csv file will be printed to STDOUT along with the SLCSP for the zipcode, if one 
can be determined from the available data.  If no single rate area can be determined, or no 
slcsp can be determined for the rate area a blank value will output.  The order of the 
zipcodes will be unchanged.  

If an SLCSP rate can be found:  
12018,204.60

If no rate can be determined the rate field will be left blank:  
12018,

## Capturing Output to Files
To capture the results to a new file, redirect output to a file:  
```#> python slcsp.py > results.csv```
