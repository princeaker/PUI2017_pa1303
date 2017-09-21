import os
import sys
import json
import urllib2 

key = sys.argv[1]
line = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + \
   "&VehicleMonitoringDetailLevel=calls&LineRef=" + line 

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)
print (dataDict)