#Higher level design pattern
# This isn;t a concrete example no libaries or frameworks being used

#Breakdown of responsibility

#Model 
class Device:

    ipAddress = ""
    port = ""
    dummy = "12"
    

    @staticmethod
    def findDevices():
        devices = []

#IRL below wouldn't be hardcoded, it is an example of found devices.
#IRL would app layer that has found some devices. or api etc
#Regardless would still do the same thing ( filling in this list )
        d = Device()
        d.ipAddress = "192.168.1.1"
        d.port = "2001"

        devices.append(d)

        d = Device()
        d.ipAddress = "192.168.1.50"
        d.port = "7091"

        devices.append(d)
      
        d = Device()
        d.ipAddress = "192.168.1.100"
        d.port = "80"

        devices.append(d)

        d = Device()
        d.ipAddress = "10.0.1.232"
        d.port = "4098"

        devices.append(d)

        return devices


#View
class DevicesView:

    def showDevices(self,devices):
        for d in devices:
            print("------------")
            print("IP Address:", d.ipAddress)
            print("Port:", d.port)
            print("------------")

#Controller

class DevicesController:

    def __init__(self):
        devices = Device.findDevices()

        v = DevicesView()
        v.showDevices(devices)
      
c = DevicesController()