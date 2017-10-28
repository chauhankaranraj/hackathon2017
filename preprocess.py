from scapy.all import *
from datasketch import MinHash

# read in raw pcaps
packet1 = rdpcap("./test.pcap")
packet2 = rdpcap("./test2.pcap")

# instantiate object
foo = MinHash()
bar = MinHash()

# convet to strings, encode in utf8, and update the hash
for packet in packet1:
	foo.update((str(packet).encode('utf8')))

for packet in packet1:
	bar.update((str(packet).encode('utf8')))

print("similarity = ", foo.jaccard(bar))
