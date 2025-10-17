import random
import matplotlib.pyplot as plt

def tcp_congestion_control(rounds=30, loss_probability=0.2):
    cwnd = 1
    ssthresh = 16
    cwnd_history = []

    for r in range(rounds):
        print(f"Round {r+1} → cwnd = {cwnd}")

        cwnd_history.append(cwnd)

        if random.random() < loss_probability:
            print("Packet loss detected → Timeout → Multiplicative Decrease")
            ssthresh = max(cwnd // 2, 1)
            cwnd = 1
        else:
            if cwnd < ssthresh:
                cwnd *= 2
            else:
                cwnd += 1

    plt.plot(cwnd_history, marker='o')
    plt.title("TCP Congestion Control (cwnd vs rounds)")
    plt.xlabel("Transmission Rounds")
    plt.ylabel("Congestion Window (cwnd)")
    plt.savefig("cwnd_plot.png")
    print("\n📊 Plot saved as 'cwnd_plot.png'")

if __name__ == "__main__":
    print("=== TCP Congestion Control Simulation ===")
    tcp_congestion_control(rounds=30, loss_probability=0.2)
