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
    name="CHILD"
    #in area location

    latitude=13.051945
    longitude=80.073990

    #out area location
    #latitude=13.044020
    #longitude=80.085481
    myData={'name':name,'lat':latitude,'lon':longitude}
    client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0)
    print("Data published to IBM IOT platform:",myData)
    time.sleep(5)
client.disconnect()
