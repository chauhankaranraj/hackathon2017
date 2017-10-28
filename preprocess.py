from datasketch import MinHash
import pandas
from scapy.all import *
from sklearn.metrics.pairwise import *


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
print("similarity = ", foo.jaccard(bar))

# cosine similarity between packets
cos_sim = cosine_similarity(foo, bar)
print("cosine similarity =", cos_sim)

#linear kernel
lin_kernel = linear_kernel(foo, bar)
print("linear kernel =", lin_kernel)

# X for malware
hashes = pandas.DataFrame([hash1, hash2, hash3, hash4])
labels = pandas.DataFrame([1, 1, 0, 0])

