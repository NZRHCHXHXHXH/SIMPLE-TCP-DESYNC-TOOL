from scapy.all import IP, TCP, sr1, send

def tcp_handshake(dst_ip, dst_port, src_port):
    ip = IP(dst=dst_ip)
    syn = TCP(sport=src_port, dport=dst_port, flags='S', seq=1000)
    synack = sr1(ip/syn, timeout=2)
    if not synack:
        raise Exception("No SYN-ACK received")
    ack = TCP(sport=src_port, dport=dst_port, flags='A', seq=synack.ack, ack=synack.seq + 1)
    send(ip/ack)
    return synack.ack, synack.seq + 1
