from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.hubs import MoveHub

hub = MoveHub()
cds = ColorDistanceSensor(Port.D)

# Print some basic information
print("LEGO Move Hub")
print("Battery: " + str(hub.battery.voltage()) +"mV")
print("Name: " + hub.system.name())
print("Ambient light: " + str(cds.ambient()) + "%")
wait(400)

# simple colour detection loop
while True:
    print("Colour: " + str(cds.color()) + ", " + str(cds.hsv()))
    print("Distance: " + str(cds.distance()) + "%")
    wait(400)
