import os
import sys
import json
import urllib2
import numpy as np

key = sys.argv[1]
line = sys.argv[2]
fout = open(sys.argv[3], "w")

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + \
   "&VehicleMonitoringDetailLevel=calls&LineRef=" + line 

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

access_point=dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
buses = []
for i in range(len(access_point)):
	if len(access_point[i]['MonitoredVehicleJourney']['OnwardCalls']) == 0:
		name = "N/A"
		status = "N/A"
	else:
		name = access_point[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
		location = access_point[i]['MonitoredVehicleJourney']['VehicleLocation']
		status = access_point[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
	buses.append((location, name, status))

fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
for i in range(len(buses)):
    fout.write("{},{},{},{}\n".format(buses[i][0]['Latitude'], buses[i][0]['Longitude'], buses[i][1], buses[i][2]))  