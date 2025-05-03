class Sender:
    def __init__(self, window_size):
        self.window_size = window_size
        self.unacknowledged_packets = list(range(1, window_size + 1))

    def receive_ack(self, ack_number):
        self.unacknowledged_packets = [packet for packet in self.unacknowledged_packets if packet > ack_number]

class Receiver:
    def __init__(self):
        self.next_expected_ack = 1

    def send_ack(self, ack_number):
        self.next_expected_ack = ack_number + 1
        return ack_number

def simulate_sliding_window(sender, receiver, packets):
    for packet in packets:
        ack = receiver.send_ack(packet)
        sender.receive_ack(ack)

# Example usage:
sender = Sender(window_size=8)
receiver = Receiver()
packets_received = [1, 2, 3, 4, 5, 6, 7, 8]  # Simulated received packets
simulate_sliding_window(sender, receiver, packets_received)
