import socket

HOST = "127.0.0.1"
PORT = 9090

def handle_client(conn):
    request = conn.recv(1024).decode()
    headers = request.split("\r\n")
    
    cookie = None
    for h in headers:
        if h.startswith("Cookie:"):
            cookie = h.split(":", 1)[1].strip()
            break

    if cookie:
        body = f"<html><body><h1>Welcome back! Your cookie: {cookie}</h1></body></html>"
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + body
    else:
        body = "<html><body><h1>Welcome, new user!</h1></body></html>"
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Set-Cookie: User=User123\r\n\r\n" + body
        )

    conn.sendall(response.encode())
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Cookie server running at http://{HOST}:{PORT}")
    while True:
        conn, _ = s.accept()
        handle_client(conn)
