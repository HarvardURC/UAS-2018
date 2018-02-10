import sys
sys.path.insert(0, 'interop/client')

import interop
import concurrent.futures

def main():
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
			print future.result()
		except Exception as exc:
			print('%r generated exception %s' %(url, exc))

if __name__ == "__main__":
	main()
