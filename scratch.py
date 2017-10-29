from scapy.all import *

packets = sniff(count=5)
wrpcap('sniffsniff.pcap', packets)
