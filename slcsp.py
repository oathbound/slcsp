#python39

# Alexander Mouravieff-Apostol for TTS Engineering

#process:
# load silver plans per "[state] [rate area #]", storing the 2 lowest plans only.  close the file.
# load zipcodes: store "[state] [rate area #]" - the county doesn't matter, only the state-rate#  close the file.
# # if there is a second rate area #, instructions say we return blank results.
# # so replace the rate-area # with blank.

# input slcsp.csv - per line look up zipcode and print either the blank value or the slcsp.
# exit (closes the file)


import csv 


class RateAreaReader():
    def __init__(self, filename=None):
        if filename is None:
            self.filename="plans.csv"
        else:
            self.filename=filename
        self.slsRates = {}

    def loadData(self):
        # only care about: SILVER plans, and we only care about the 2lowest DISTINCT prices. 
        sls = {}
        with open(self.filename) as somecsv:
            csvFile = csv.DictReader(somecsv, delimiter=",", fieldnames=['plan_id','state','metal_level','rate','rate_area'], restkey="extrafieldlist",restval="")
            header = next(csvFile) #skip headers
            for line in csvFile: 
                # line is dict with keys ['plan_id','state','metal_level','rate,rate_area']
                if line['metal_level'].lower() == 'silver': 
                    rc = "{} {}".format(line['state'],line['rate_area'])
                    rate = float(line['rate'])
                    #If this rc is new - we need to set things up
                    if rc not in sls.keys():
                        sls[rc]=[float(line['rate']), ""]
                    elif rate <= sls[rc][0]: 
                        if rate==sls[rc][0]: #ignore duplicate prices!
                            continue
                        sls[rc][1]=sls[rc][0]
                        sls[rc][0]=rate
                    elif sls[rc][1] == "": #the fist rate is smaller than this rate, w no second rate yet?
                        sls[rc][1]=rate 
                    elif rate < sls[rc][1]:  #the first rate is smaller, new slcSP.
                        sls[rc][1]=rate 

        #sls is now full up of {'some rateCode':[lcSP,slcSP], ...}
        for k in sls:
            if sls[k][1] == "":
                self.slsRates[k]=""
            else:
                self.slsRates[k]="{:.2f}".format(sls[k][1])
        #the SLCSPrates dict now has either a 2 digit second lowest price...or a blank string.  

    def getSLCSP(self, ra):
        if ra in self.slsRates.keys():
            return self.slsRates[ra]
        return ""


class ZipRateAreasReader():
    def __init__(self, filename=None):
        if filename is None:
            self.filename="zips.csv"
        else:
            self.filename=filename        
        self.zipAreas = {}

    def loadData(self):
        # only care about: SILVER plans, and we only care about the 2lowest DISTINCT prices.  (do not use >= or <=)
        zips = {}
        with open(self.filename) as somecsv:
            csvFile = csv.DictReader(somecsv, delimiter=",", fieldnames=['zipcode','state','county_code','name','rate_area'], restkey="extrafieldlist",restval="")
            header = next(csvFile) #skip headers
            for line in csvFile: 
                #If the zipcode is new, great, this is the first rateArea we've seen.  this will normally be the case.
                rc = "{} {}".format(line['state'],line['rate_area'])
                zip = line['zipcode']
                if zip in zips.keys():
                    #we have already seen this zip.
                    if rc != zips[zip]: #a different state+rate area pair.  We are to offer no rate on this.
                        zips[zip]="" #there is no rate area to look up.
                    #if rate area is the same, then it's ok despite being in the list twice / different county info.
                else: #not in the keys means a new zipcode, so no need to check for preexisting rates
                    zips[zip]=rc
        
        self.zipAreas=zips       

    def getRateArea(self,zip):
        if zip in self.zipAreas.keys():
            return self.zipAreas[zip]
        else:
            return ""



class slcspLookupTool():
    def __init__(self, filename=None):
        if filename is None:
            self.filename="slcsp.csv"
        else:
            self.filename=filename
        self.rates = RateAreaReader()
        self.zipAreas= ZipRateAreasReader()

    def loadData(self):
        self.rates.loadData()
        self.zipAreas.loadData()

    def doRun(self):
        # Here we go!
         with open(self.filename) as somecsv:
            csvFile = csv.DictReader(somecsv, delimiter=",", fieldnames=['zipcode','rate'], restkey="extrafieldlist",restval="")
            header = next(csvFile) #skip headers
            print("zipcode,rate")
            for line in csvFile: 
                rate = self.getRate(line['zipcode'])
                print ("{},{}".format(line['zipcode'], rate))


    def getRate(self,zip):
        ra = self.zipAreas.getRateArea(zip) #now error catch pls.
        if ra == "":
            return ""
        return self.rates.getSLCSP(ra)
        
        



if __name__ == "__main__":
    lookUp = slcspLookupTool()
    lookUp.loadData()
    lookUp.doRun()


