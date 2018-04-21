import sys
sys.path.insert(0, 'interop/client')

import interop
import concurrent.futures

import time
import zmq

def get_mission_data(publisher):
    if (len(sys.argv) < 3):
        print("Usage: testclient.py username password")
        exit()

    user = sys.argv[1]
    password = sys.argv[2]
    client = interop.AsyncClient("http://localhost:8000", \
                                 user, password, \
                                 timeout=10, workers = 8)
    futures = list()
    futures.append(client.get_missions())
    futures.append(client.get_obstacles())
    for future in concurrent.futures.as_completed(futures):
        try:
            lat = "%d" % futures.Mission.flyzones.boundary_pts.latitude;
            publisher.send_multipart(["Latitude", lat])
            print future.result()
        except Exception as exc:
            print('%r generated exception %s' %(url, exc))

def main():
    get_mission_data()

    # Prepare our context and publisher
    context   = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:5563")

    while True:
        # Write two messages, each with an envelope and content
        time.sleep(1)

    # We never get here but clean up anyhow
    publisher.close()
    context.term()

if __name__ == "__main__":
    main()
