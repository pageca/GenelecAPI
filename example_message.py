import requests
import json
import base64

# rxa

# Define the API endpoint URL
api_url = "http://192.168.0.79:9000/public/v1/audio/volume"

# Define the message body as a JSON object
message_body = {
    "level": -15.0,
    "mute": False
}
message_length = len(json.dumps(message_body).encode("utf-8"))

# Define the request headers
headers = {
    "Host": "192.168.0.79:9000",
    "Accept": "application/json",
    "Connection": "close", #keep-open is default
    "Authorization": "Basic " + base64.b64encode(b"admin:admin").decode(),
    "Content-Length": str(message_length)
}

print(len(json.dumps(message_body)))

request = requests.Request("PUT", api_url, headers=headers, json=message_body)
prepared_request = request.prepare()

# Send the PUT request with the specified headers and message body
print(prepared_request.body)
print("Full HTTP Request:")
print(f"{prepared_request.method} {prepared_request.url}")
print("\n".join(f"{k}: {v}" for k, v in prepared_request.headers.items()))
print("\n" + prepared_request.body.decode('utf-8'))

# Check the response
""" response = requests.put(api_url, headers=headers, json=message_body)

if response.status_code == 200:
    print("Request was successful.")
else:
    print(f"Request failed with status code {response.status_code}: {response.text}") """
