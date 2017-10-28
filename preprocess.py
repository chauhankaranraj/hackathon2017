from scapy.all import *
from datasketch import MinHash

# read in raw pcaps
normal1 = rdpcap("./normal1.pcap")
normal2 = rdpcap("./normal2.pcap")

mal1 = rdpcap("./mal1.pcap")
mal2 = rdpcap("./mal2.pcap")

# instantiate object
hash1 = MinHash()
hash2 = MinHash()
hash3 = MinHash()
hash4 = MinHash()

# convet to strings, encode in utf8, and update the hash
for packet in normal1:
	hash1.update((str(packet).encode('utf8')))

for packet in normal2:
	hash2.update((str(packet).encode('utf8')))

for packet in mal1:
	hash3.update((str(packet).encode('utf8')))

for packet in mal2:
	hash4.update((str(packet).encode('utf8')))

print("norm-norm similarity = ", hash1.jaccard(hash2))
print("norm-mal similarity = ", hash1.jaccard(hash3))
print("mal-mal similarity = ", hash3.jaccard(hash4))
