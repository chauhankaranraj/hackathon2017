from scapy.all import *
from datasketch import MinHash
from sklearn.metrics.pairwise import *

# read in raw pcaps
packet1 = rdpcap("./normal1.pcap")
packet2 = rdpcap("./normal2.pcap")

# instantiate object
foo = MinHash()
bar = MinHash()

# convet to strings, encode in utf8, and update the hash
for packet in packet1:
	foo.update((str(packet).encode('utf8')))

for packet in packet2:
	bar.update((str(packet).encode('utf8')))

print("similarity = ", foo.jaccard(bar))

# cosine similarity between packets
cos_sim = cosine_similarity(foo, bar)
print("cosine similarity =", cos_sim)

#linear kernel
lin_kernel = linear_kernel(foo, bar)
print("linear kernel =", lin_kernel)

