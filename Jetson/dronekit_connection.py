from dronekit import connect, Command, LocationGlobal
from pymavlink import mavutil
import time, sys, argparse, math


print "Connecting"
connection_string = '/dev/ttyTHS2'
vehicle = connect(connection_string, wait_ready=True, heartbeat_timeout=30, baud=921600)

print "Type: %s" % vehicle._vehicle_tupe
print "Armed:%s" % vehicle.armed
print "System status: %s" % vehicle.system_status.state
print "GPS: %s" % vehicle.gps_0
print "Alt: %s" % vehicle.location.global_relative_frame.alt

