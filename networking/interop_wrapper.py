import interop
import concurrent.futures

class Client:
    def __init__(self, host, user, password):
        if not (host or user or password):
            raise Exception("Must specify all of host, username, password")
        
        try:
            self.client = interop.AsyncClient(host, user, password, timeout=10, workers=8)

        except:
            raise Exception("Unable to connect.")


    def upload_telemetry(self, latitude, longitude, altitude_msl, uas_heading):
        try:
            self.client.post_telemetry(
                interop.Telemetry(
                    latitude = latitude, 
                    longitude = longitude, 
                    altitude_msl = altitude_msl, 
                    uas_heading = uas_heading
                )
            )
            return True

        except:
            return False


    def upload_object_and_image(self, path, typ, latitude, longitude, orientation, shape, background_color, alphanumeric, alphanumeric_color):
        try:
            odlc = interop.Odlc(
                type = typ, 
                latitude = latitude, 
                longitude = longitude, 
                orientation = orientation, 
                shape = shape, 
                background_color = background_color, 
                alphanumeric = alphanumeric, 
                alphanumeric_color = alphanumeric_color
            )
            odlc = self.client.post_odlc(odlc)

            with open(path, 'rb') as f:
                image_data = f.read()
                self.client.put_odlc_image(odlc.id, image_data)

            return True

        except:
            return False


    def get_missions(self):
        return self.client.get_missions()


    def get_obstacles():
        return self.client.get_obstacles()


def main():
    # Run mission script here
    client = Client('10.10.130.10:80', 'harvard', '6581969384')

    futures = []
    futures.append(client.get_missions())
    futures.append(client.get_obstacles())

    for future in concurrent.futures.as_completed(futures):
        try:
            # Logic here, use above functions
            print(future.result())

        except Exception as exc:
            print('%r generated exception %s' %(url, exc))

if __name__ == "__main__":
    main()
