from scapy.all import *
from datasketch import MinHash

# read in raw pcaps
packet1 = rdpcap("./mal1.pcap")
packet2 = rdpcap("./normal1.pcap")

# instantiate object
foo = MinHash()
bar = MinHash()

# convet to strings, encode in utf8, and update the hash
for packet in packet1:
	foo.update((str(packet).encode('utf8')))

for packet in packet2:
	bar.update((str(packet).encode('utf8')))

print("similarity = ", foo.jaccard(bar))
