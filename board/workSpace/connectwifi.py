import network
import ure
  
def scanNetwork(station, ssid):
  validNetwork = station.scan()
  for net in validNetwork:
#    print(ssid, str(net[0]))
    if ure.search(ssid, str(net[0])):
      return True
  return False
    
  
def connect(ssid, password):
  station = network.WLAN(network.STA_IF)
  if station.isconnected() == True:
    print("Already connected")
    return
  
  station.active(True)
  if scanNetwork(station, ssid) == False:
    print("Without this WiFi")
    return
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print("Connection successful")
  print(station.ifconfig())
  
def disconnect():
  station = network.WLAN(network.STA_IF)
  if station.isconnected() == True:
    station.disconnect()



