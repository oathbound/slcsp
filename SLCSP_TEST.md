# Test Instructions for SLCSP.PY

# Test Files
* slcsp_test_in.csv - 5 zipcodes, 4 of which should return no SLCSP
* slcsp_test_out.csv - the correct output when the script determines SLCSP for the zipcodes provided in the slcsp_test_in.csv file.
* SLCSP_TEST.md - this readme file with instructions on testing the script against a small set of known results.

# Testing Against Known Results:
To test code on a known input-output:
* Modify line 136 to provide the test input file.
  * change ```lookUp = slcspLookupTool()``` to ```lookUp = slcspLookupTool("slcsp_test_in.csv")```
  * Should you need to test another set of zipcodes, you may modify this file, or use another - but then you will need to verify your own test outputs.
* Run the script as instructed either leaving output on the console's STDOUT, or redirecting it to another file.
  * python3 slcsp.py > slcsp_test.csv

## Verifying Results and Determining Problems:
* Compare the output with the contents of slcsp_test_out.csv.  The test file is short so this process can be done manually.
  * If the first line (64148) differs, something has caused the tool to be unable to correctly determine the SLCSP when it is available in the input files.
  * If the second line (40813) is not blank, then the tool is unable to detect a rate area has NO Silver Plans.
  * If the third line (07640) is not blank, then the tool is unable to recognize there is only one silver plan rate, and therefore no second lowest costing silver plan.
  * If the fourth line (54923) is not blank, then the tool is unable to recognize that a zipcode belongs to multiple rate areas.
  * If the fifth line (11111) is not blank, then the tool is unable to recognize that the zipcode is not present in the zips.csv file.

## If Results Do Not Match  
It is possible that the input files zips.csv or plans.csv have been modified, or that the script has been compromised in some 
way.  The best way to resolve this is to checkout the latest version of the source code again from the repository located at:  
  * https://github.com/oathbound/slcsp/

If the provided tests still fail while running against the provided input files, there is an error in the host environment.
  
# Returning to normal operation:
  In normal operation, this script will automatically use the slcsp.csv for its control file.  To return to normal 
  operation after testing is complete, modify line 136 in slcsp.py from 
  *  ```lookUp = slcspLookupTool("slcsp_test_in.csv")``` to  ```lookUp = slcspLookupTool()```
  *  This will restore the script to looking up the zip codes in slcsp.py as required by the project specification.
