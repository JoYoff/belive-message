import socket
import json

def get_ip():

	hostname = socket.gethostname()
	local_ip = socket.gethostbyname(hostname)

	keep_ip = {
		"ip": local_ip
	}

	with open('ip_keep.json', 'w') as ip_json:
		json.dump(keep_ip, ip_json)