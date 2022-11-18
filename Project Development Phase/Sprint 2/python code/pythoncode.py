import json
import wiotp.sdk.device
import time
myConfig={
"identity":{
"orgId":"qo45cf",
"typeId": "NODERED",
"deviceId":"12345"
 },
"auth":{
"token":"123456789"
}
}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while True:
    name="smartbridge"
    #in area location
    #latitude=17.4219272
    #longitude=78.5488783
    #out area location
    latitude=17.4219272
    longitude=78.5488783
    myData={'name':name,'lat':latitude,'log':longitude}
    client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0)
    print("Data published to IBM IOT platform:",myData)
    time.sleep(5)
client.disconnect()
