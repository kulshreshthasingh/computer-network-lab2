import cv2
import socket
import numpy as np

ip = "127.0.0.1"
port = 5000
addr = (ip, port)

print(f"Binding socket to {addr}...")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)
print("Socket bound successfully.")

buf = b""
print("Waiting for packets...")
while True:
    pkt, _ = sock.recvfrom(65535)
    print(f"Received packet of size {len(pkt)} bytes.")
    m = pkt[0]
    d = pkt[1:]
    buf += d

    if m == 1:
        print("End of frame detected. Decoding image...")
        arr = np.frombuffer(buf, dtype=np.uint8)
        buf = b""
        img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        if img is not None:
            print("Image decoded successfully. Displaying image.")
            cv2.imshow("Stream", img)
            if cv2.getWindowProperty("Stream", cv2.WND_PROP_VISIBLE) < 1:
                print("Window closed by user.")
                break
        else:
            print("Failed to decode image.")
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Exit requested by user.")
            break

print("Closing socket and destroying windows.")
sock.close()
cv2.destroyAllWindows()
