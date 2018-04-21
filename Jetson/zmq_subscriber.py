# from dronekit import connect, Command, LocationGlobal
# from pymavlink import mavutil
# import time, sys, argparse, math

import zmq

def main():
    # Prepare our context and publisher

    # print "Connecting"
    # connection_string = '/dev/ttyTHS2'
    # vehicle=connect(connection_string, wait_ready=True,heartbeat_timeout=30, baud=921600)

    context    = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5563")
    subscriber.setsockopt(zmq.SUBSCRIBE, "Latitude")

    while True:
        # Read envelope with address
        [address, contents] = subscriber.recv_multipart()
        print("[%s] %s" % (address, contents))

        # print "Type: %s" %vehicle._vehicle_tupe
        # print "Armed:%s" %vehicle.armed
        # print "System status: %s" %vehicle.system_status.state
        # print "GPS: %s" % vehicle.gps_0
        # print "Alt: %s" % vehicle.location.global_relative_frame.alt

    # We never get here but clean up anyhow
    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
