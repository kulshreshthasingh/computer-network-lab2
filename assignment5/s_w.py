import random
import time

def stop_and_wait(total_frames=10, loss_probability=0.3):
    frame = 1
    while frame <= total_frames:
        print(f"\nSending Frame {frame}")

        if random.random() < loss_probability:
            print(f" Frame {frame} lost... Timeout! Retransmitting...")
            time.sleep(1)  
            continue
        
        print(f"ACK {frame} received")
        frame += 1
        time.sleep(0.5)

if __name__ == "__main__":
    print(" Stop and Wait ARQ Simulation ")
    stop_and_wait(total_frames=10, loss_probability=0.3)
