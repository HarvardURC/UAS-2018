import interop
import concurrent.futures

def main():
	user = 'harvard'
	password = '6581969384'
	client = interop.AsyncClient("http://10.10.130.10:80", \
								 user, password, \
								 timeout=10, workers = 8)
	
    futures = []
	futures.append(client.get_missions())
	futures.append(client.get_obstacles())

	for future in concurrent.futures.as_completed(futures):
		try:
            # Here's the futures as they come in
			print future.result()
		except Exception as exc:
			print('%r generated exception %s' %(url, exc))

if __name__ == "__main__":
	main()
