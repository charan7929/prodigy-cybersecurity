from scapy.all import sniff, IP, TCP, UDP, ICMP

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        # Detect protocol
        protocol = "OTHER"
        if proto == 6:
            protocol = "TCP"
        elif proto == 17:
            protocol = "UDP"
        elif proto == 1:
            protocol = "ICMP"

        print(f"[{protocol}] {src_ip} → {dst_ip}")

        # Optional: Print payload for TCP/UDP
        if protocol in ["TCP", "UDP"] and packet.haslayer(Raw):
            payload = packet[Raw].load
            try:
                print("Payload:", payload.decode('utf-8', errors='ignore'))
            except Exception as e:
                print("Could not decode payload.")

        print("-" * 60)

# Start sniffing (use appropriate interface name)
print("Starting packet capture... Press Ctrl+C to stop.")
sniff(filter="ip", prn=process_packet, store=False)
