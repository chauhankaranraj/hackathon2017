from scapy.all import *
from datasketch import MinHash


packets = rdpcap("./test.pcap")

# instantiate object
testHash = MinHash()

# convet to strings, encode in utf8, and update the hash
for packet in packets:
	print(str(packet))
	testHash.update((str(packet).encode('utf8')))

print("here's what the hash looks like", testHash)
