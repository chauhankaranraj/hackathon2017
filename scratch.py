from datasketch import MinHash
from scapy.all import *
import os

# parse pcap into an object
pcap_obj = rdpcap('/media/nvidia/windows/normal-traffic/' + os.listdir('/media/nvidia/windows/normal-traffic/')[2])

# hash for current pcap file
pcap_hash = MinHash()

# create the hash object
for packet in pcap_obj:
	pcap_hash.update(str(packet).encode("utf8"))

print(len(pcap_hash.hashvalues))
