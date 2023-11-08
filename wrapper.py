import requests
import argparse
from typing import List, Any
from pythonosc import udp_client, osc_server, osc_bundle_builder

import socket
import os, re
import json
import base64


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()


# Speaker Schnüffler

devices = [re.findall('^[\w\?\.]+|(?<=\s)\([\d\.]+\)|(?<=at\s)[\w\:]+', i) for i in os.popen('arp -a')]
devices = [dict(zip(['IP', 'LAN_IP', 'MAC_ADDRESS'], i)) for i in devices]
devices = [{**i, **{'LAN_IP':i['LAN_IP'][1:-1]}} for i in devices]

#send device info request to all IPs in network
port = 9000
headers = {
    "Host": "192.168.0.79:9000",
    "Accept": "application/json",
    "Connection": "close", #keep-open is default
    "Authorization": base64.b64encode(b"admin:admin").decode(),
    "Content-Length": "0"
}
for device in devices:
    ip = device['LAN_IP']
    url = "http://%s:%d/public/v1/device/info"%(ip, port)
    # print(url)
    headers['Host'] = "%s:%d"%(ip,port)
    try:
        response = requests.get(url, headers=headers)
        print("speaker found at %s"%(ip))
        print(response.content)
    except requests.ConnectionError:
        print(response.content)
        continue