from datasketch import MinHash
import numpy as np
import pickle as pkl
from scapy.all import *
import tensorflow as tf


def getNearestCentroid(input_pcap_f_name, centroids_f_name='centroids.obj'):
	"""
	Calculates euclidean distances of input pcap from each centroid and returns the closest centroid

	@param input_pcap_f_name: input pcap file to be classified
	@param centroids_f_name: name of pickled num_centroids x 128 np.array file
	@return neartest_centroid: id number of nearest centroid

	"""
	# load the calculated centroids from k means
	with open(centroids_f_name, 'rb') as fHandler:
		centroids = np.array(pkl.load(fHandler))

	# parse pcap into an object
	pcap_obj = rdpcap(input_pcap_f_name)

	# hash for the input pcap file
	pcap_hash = MinHash()

	# update the hash object with each packet in pcap file
	for packet in pcap_obj:
		pcap_hash.update(str(packet).encode("utf8"))

	# # create the np array to be used as test point to calculate euclidean distances
	input_hash_vals = np.zeros((1, 128))
	input_hash_vals[0, :] = pcap_hash.hashvalues

	# initialize nearest centroid and minimum distance
	nearest_centroid = -1
	min_dist = float('inf')

	# calculate euclidean distances of each centroid from input hash, update min_dist and nearest centroid accordingly
	for centroid_num in range(np.shape(centroids)[0]):

		dist = np.sqrt(np.sum(np.subtract(input_hash_vals, centroids[centroid_num, :])**2))

		if dist < min_dist:
			min_dist = dist
			nearest_centroid = centroid_num

	return nearest_centroid


if __name__ == "__main__":
	
	pred = getNearestCentroid("D:\\normal-traffic\\normal9.pcap")

	print(pred)
	
	# with open('prob_dict', 'rb') as fHandler:
	# 	print(prob_dict[pred])



