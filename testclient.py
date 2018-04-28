import sys
sys.path.insert(0, 'interop/client')

import time
import zmq
import interop
import concurrent.futures
import json

def toJSON(mission):
	lst = list()
	for el in mission:
		lst.append(json.dumps(el, default=lambda o: o.__dict__, sort_keys=True, indent = 4))
	return json.dumps(lst)

def main():
	if (len(sys.argv) < 3):
		print("Usage: testclient.py username password")
		exit()

	user = sys.argv[1]
	password = sys.argv[2]
	client = interop.AsyncClient("http://localhost:8000", \
								 user, password, \
								 timeout=10, workers = 8)
	context   = zmq.Context()
	publisher = context.socket(zmq.PUSH)
	publisher.bind("tcp://*:5563")

	futures = list()
	futures.append(client.get_missions())

	for future in concurrent.futures.as_completed(futures):
		try:
			while True:
				mission = toJSON(future.result())
				publisher.send_json(mission)
				print 
				time.sleep(1)
		except Exception as exc:
			print('generated exception %s' %(exc))

if __name__ == "__main__":
	main()
