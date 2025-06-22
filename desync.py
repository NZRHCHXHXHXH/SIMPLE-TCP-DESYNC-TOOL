#!/usr/bin/env python3

import argparse
import sys
from attacks import overlap, split, smuggle

def banner():
    print(r"""
███╗   ██╗███████╗██████╗ ██╗  ██╗██╗  ██╗██╗  ██╗ 
████╗  ██║╚══███╔╝██╔══██╗╚██╗██╔╝██║  ██║╚██╗██╔╝ 
██╔██╗ ██║  ███╔╝ ██████╔╝ ╚███╔╝ ███████║ ╚███╔╝  
██║╚██╗██║ ███╔╝  ██╔══██╗ ██╔██╗ ██╔══██║ ██╔██╗  
██║ ╚████║███████╗██║  ██║██╔╝ ██╗██║  ██║██╔╝ ██╗ 
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ 
                                                   
██████╗ ███████╗███████╗██╗   ██╗███╗   ██╗ ██████╗
██╔══██╗██╔════╝██╔════╝╚██╗ ██╔╝████╗  ██║██╔════╝
██║  ██║█████╗  ███████╗ ╚████╔╝ ██╔██╗ ██║██║     
██║  ██║██╔══╝  ╚════██║  ╚██╔╝  ██║╚██╗██║██║     
██████╔╝███████╗███████║   ██║   ██║ ╚████║╚██████╗
╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝
                                                   
TCP Desynchronization Automation Tool - By NZRXHX
    """)

def parse_args():
    parser = argparse.ArgumentParser(
        description='NZRXHX - Automating TCP Desynchronization Attacks')
    
    parser.add_argument(
        '--target', '-t', required=True,
        help='Target IP and port in the format IP:PORT (e.g., 192.168.1.100:80)'
    )

    parser.add_argument(
        '--attack', '-a', required=True,
        choices=['overlap', 'split', 'smuggle'],
        help='Attack type: overlap, split, smuggle'
    )

    args = parser.parse_args()

    # Validate target
    if ':' not in args.target:
        parser.error("Invalid target format. Use IP:PORT")
    
    return args

def main():
    banner()
    args = parse_args()
    target_ip, target_port = args.target.split(":")
    
    try:
        target_port = int(target_port)
    except ValueError:
        print("[-] Error: Port must be an integer.")
        sys.exit(1)

    print(f"[+] Target: {target_ip}:{target_port}")
    print(f"[+] Attack: {args.attack}")

    # Dispatch to correct module
    if args.attack == 'overlap':
        overlap.run(target_ip, target_port)
    elif args.attack == 'split':
        split.run(target_ip, target_port)
    elif args.attack == 'smuggle':
        smuggle.run(target_ip, target_port)
    else:
        print("[-] Unknown attack method.")
        sys.exit(1)

if __name__ == "__main__":
    main()
