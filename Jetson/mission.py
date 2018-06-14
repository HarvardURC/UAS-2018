import dronekit
from sys import argv

def main():
    if len(argv) != 2:
        print "Usage: mission.py [connection_string]"
        return 1

    print "Connecting to %s" % argv[1]
    vehicle = connect(argv[1], wait_ready=True, heartbeat_timeout=30, baud=921600)

    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()

    

