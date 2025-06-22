simple TCP desync attack tool - NZRXHX

### Features

- TCP segment overlapping
- HTTP header/body splitting
- HTTP request smuggling
- Raw TCP stream manipulation using Scapy
- Support for overlapping TCP segments
- Injecting malformed HTTP requests
- Modular code for future attack techniques

---

### Usage
```bash
python desync.py --target TARGET_IP:PORT --attack {overlap,split,smuggle}
```
! might need sudo permissions to run Scapy’s raw socket features

# Example usage
```bash
python desync.py --target 192.168.1.1:80 --attack overlap
```

## Requirements

- Python 3.8+
- `scapy`
- `argparse`
