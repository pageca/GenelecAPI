from pythonosc import udp_client, dispatcher, osc_server
import argparse
import requests
import json
import base64
import threading
import os
import re

speakers = {}

def send_command(ip, endpoint, method="GET", message=None):
    url = f"http://{ip}:9000/public/v1/{endpoint}"
    headers = {
        "Accept": "application/json",
        "Connection": "close",
        "Authorization": base64.b64encode(b"admin:admin").decode(),
    }

    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "PUT":
            headers["Content-Type"] = "application/json"
            response = requests.put(url, headers=headers, json=json.dumps(message))
        else:
            print(f"Unsupported HTTP method: {method}")
            return

        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def scan_network(sender_ip, sender_port, *args):
    global speakers

    speakers = {}  # Reset the speakers dictionary

    # Speaker Scanner
    devices = [re.findall('^[\w\?\.]+|(?<=\s)\([\d\.]+\)|(?<=at\s)[\w\:]+', i) for i in os.popen('arp -a')]
    devices = [dict(zip(['IP', 'LAN_IP', 'MAC_ADDRESS'], i)) for i in devices]
    devices = [{**i, **{'LAN_IP': i['LAN_IP'][1:-1]}} for i in devices]

    for device in devices:
        ip = device['LAN_IP']

        #check if the device is  speaker
        response = send_command(ip, "device/id", "GET")
        if response and "barcode" in response:
            speakers[ip] = response

    # Create OSC client dynamically
    client = udp_client.SimpleUDPClient(sender_ip, sender_port)

    # Send scan results back to the sender via OSC
    client.send_message("/scan_results", [json.dumps(speakers)])

def osc_to_http(*args):
    ip, option, message = args

    return send_command(ip, option, "PUT", message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OSC to HTTP Wrapper")
    parser.add_argument("--ip", default="127.0.0.1", help="The IP to listen on for OSC server")
    parser.add_argument("--port", type=int, default=5005, help="The port to listen on for OSC server")
    args = parser.parse_args()

    # Initialize OSC server
    osc_dispatcher = dispatcher.Dispatcher()
    osc_dispatcher.map("/set", osc_to_http, "http_response")
    osc_dispatcher.map("/scan", scan_network, "scan_network")

    osc_server_thread = osc_server.ThreadingOSCUDPServer((args.ip, args.port), osc_dispatcher)
    osc_server_thread_thread = threading.Thread(target=osc_server_thread.serve_forever)
    osc_server_thread_thread.start()
