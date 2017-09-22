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

access_point=dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
access_point[0]['MonitoredVehicleJourney']['VehicleLocation']
buses = []
for i in range(len(access_point)):
    name = access_point[i]['MonitoredVehicleJourney']['PublishedLineName']
    location = access_point[i]['MonitoredVehicleJourney']['VehicleLocation']
    buses.append((name, location))

print('Bus Line : {}'.format(line))
print("Number of active buses: %d" % len(buses))
for i in range(len(buses)):
    print("Bus {0} is at latitude {1} and longitude {2}".format(i, buses[i][1]['Latitude'], buses[i][1]['Longitude']))    