import socket

def main():
    host = "127.0.0.1"  
    port = 6000         

    client_name = "Alice"

    # Take integer input
    while True:
        try:
            num = int(input("Enter an integer (1–100): "))
            if 1 <= num <= 100:
                break
            else:
                print("Number must be between 1 and 100.")
        except ValueError:
            print("Please enter a valid integer.")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = f"{client_name},{num}"
    client_socket.send(message.encode())

    data = client_socket.recv(1024).decode()
    server_name, server_num_str = data.split(",")
    server_num = int(server_num_str.strip())

    total = num + server_num

    print("\n--- Client Side ---")
    print(f"Client Name: {client_name}")
    print(f"Server Name: {server_name}")
    print(f"Client Integer: {num}")
    print(f"Server Integer: {server_num}")
    print(f"Sum: {total}")

    client_socket.close()

if __name__ == "__main__":
    main()
