import ServerApplication
import time


api_url = "api.collectapi.com"
api_key = "apikey 2rKqR4V0x4lMMxIO9m1I8d:4dWxzEPquJ9ffSjwp9Pl1a"
firestore_credentials_resource = "Resources/serviceAccountKey.json"

server_app = ServerApplication.ServerApplication(firestore_credentials_resource, api_url,
                                                 api_key)

var = 1
while var == 1:  # This constructs an infinite loop
    server_app.run()
    time.sleep(1200)
