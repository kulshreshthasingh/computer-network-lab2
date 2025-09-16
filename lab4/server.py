import cv2
import socket
import math
import time

ip = "127.0.0.1"
port = 5000
addr = (ip, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cam = cv2.VideoCapture(0)
fps = int(cam.get(cv2.CAP_PROP_FPS))
interval = 1 / fps
chunk = 65535

print("Server started... Streaming video")
print(f"IP: {ip}, Port: {port}")
print(f"FPS: {fps}, Interval: {interval}, Chunk size: {chunk}")

while cam.isOpened():
    ret, frm = cam.read()
    print(f"Frame read: {ret}")
    if not ret:
        print("Failed to read frame. Exiting.")
        break
    frm = cv2.resize(frm, (640, 480))
    _, buf = cv2.imencode(".jpg", frm)
    dat = buf.tobytes()
    total = math.ceil(len(dat) / chunk)
    print(f"Total packets to send: {total}")
    for i in range(total):
        st = i * chunk
        en = st + chunk
        part = dat[st:en]
        mark = 1 if i == total - 1 else 0
        pkt = bytes([mark]) + part
        sock.sendto(pkt, addr)
        print(f"Sent packet {i+1}/{total}")
    time.sleep(interval)

cam.release()
sock.close()
print("Streaming stopped. Resources released.")
