import socket
import random
def main():
    host = "0.0.0.0"  
    port = 6000    

    server_name = " Smith"
    server_number = random.randint(1, 100)  

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server started on port {port}. Waiting for connection...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024).decode()
    if not data:
        conn.close()
        server_socket.close()
        return

    try:
        client_name, client_num_str = data.split(",")
        client_num = int(client_num_str.strip())
    except ValueError:
        print("Invalid message format. Closing connection.")
        conn.close()
        server_socket.close()
        return

    if client_num < 1 or client_num > 100:
        print("Received number outside 1–100. Terminating server.")
        conn.close()
        server_socket.close()
        return

    total = client_num + server_number

    print("\n--- Server Side ---")
    print(f"Client Name: {client_name}")
    print(f"Server Name: {server_name}")
    print(f"Client Integer: {client_num}")
    print(f"Server Integer: {server_number}")
    print(f"Sum: {total}")

    reply = f"{server_name},{server_number}"
    conn.send(reply.encode())

    conn.close()
    server_socket.close()
    print("Server terminated.")

if __name__ == "__main__":
    main()
