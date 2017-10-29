from datasketch import MinHash
import pickle as pkl
import tensorflow as tf


def getNearestCentroid(input_pcap, centroids_f_name='centroids.obj'):
"""
Calculates euclidean distances of input pcap from each centroid and returns the closest centroid

@param input_pcap: input pcap file to be classified
@param centroids_f_name: name of pickled num_centroids x 128 np.array file
@return neartest_centroid: id number of nearest centroid

"""
	# load the calculated centroids from k means
	with open(centroids_f_name, 'rb') as fHandler:
		centroids = pkl.load(fHandler)

	# hash for the input pcap file
	pcap_hash = MinHash()

	# update the hash object with each packet in pcap file
	for packet in pcap_obj:
		pcap_hash.update(str(packet).encode("utf8"))

	# create the np array to be used as test point to calculate euclidean distances
	input_hash_vals = np.array((1, 128))
	input_hash_vals[1, :] = pcap_hash.hashvalues

	# TODO
	nearest_centroid = 0
	for centroid in centroids:
		# calculate euclidean distance
		# if < min, min = this

return nearest_centroid
