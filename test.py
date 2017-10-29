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
		cent = pkl.load(fHandler)

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


	graph = tf.Graph()
 
	with graph.as_default():

		sess = tf.Session()

		#Find out the dimensionality
		dim = 128

		#Placeholders for input
		v1 = tf.placeholder("float", [dim])
		v2 = tf.placeholder("float", [dim])
		euclid_dist = tf.sqrt(tf.reduce_sum(tf.pow(tf.subtract(
			v1, v2), 2)))

		input_hash_vals = tf.constant(input_hash_vals, shape=(1, 128))

		##initialized to one of the vectors from the available data points
		centroids = [tf.Variable((cent[i])) for i in range(np.shape(cent)[0])]

		print("\n\n\n\ninitialized centroids\n\n\n\n\n\n")

		##These nodes will assign the centroid Variables the appropriate
		##values
		centroid_value = tf.placeholder("float64", [dim])
		cent_assigns = []
		for centroid in centroids:
			cent_assigns.append(tf.assign(centroid, centroid_value))

		print("\n\n\n\n\ncreated constants\n\n\n\n\n\n")

		##INITIALIZING STATE VARIABLES
 
		##This will help initialization of all Variables defined with respect
		##to the graph. The Variable-initializer should be defined after
		##all the Variables have been constructed, so that each of them
		##will be included in the initialization.
		init_op = tf.global_variables_initializer()
 
		#Initialize all variables
		sess.run(init_op)

		print("\n\n\n\n\ncalculating distasnces\n\n\n\n\n\n")
		#Compute Euclidean distance between this vector and each
		#centroid. Remember that this list cannot be named
		#'centroid_distances', since that is the input to the
		#cluster assignment node.
		distances = [sess.run(euclid_dist, feed_dict={
			v1: input_hash_vals, 
			v2: sess.run(centroid)}) for centroid in centroids]

		nearest_centroid = tf.argmin(distances)

	return nearest_centroid


if __name__ == "__main__":
	
	pred = getNearestCentroid("/media/nvidia/windows/normal-traffic/normal9.pcap")



