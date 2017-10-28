from datasketch import MinHash
import numpy as np
import os
import pickle
from scapy.all import *

#  TODO: CHANGE THE NORMAL AND MALWARE DIRECTORIES BEFORE YOU RUN THIS SCRIPT
def process_raw_data(normal_pcap_dir = "/home/natalia/Desktop/normal-traffic/", malware_pcap_dir = "/home/natalia/Desktop/regin-malware/")
	"""
	Takes in directories of raw data (pcap files) and returns np.array of hashes of ***ALL*** pcap files
	
	:param normal_pcap_dir: directory where normal pcap files are saved
	:param malware_pcap_dir: directory where malware pcap files are saved
	:return: np.array of hashes of normal and malware pcap files combined
	"""

	# directories where the pcap files are saved
	normal_pcap_dir = "/home/natalia/Desktop/normal-traffic/"
	malware_pcap_dir = "/home/natalia/Desktop/regin-malware/"

	# dataframes for storing hashes
	normal_hashes = []
	malware_hashes = []

	print("Hashing normal traffic...", end="")
	# populate the normal hashes dataframe
	for normal_pcap_name in os.listdir(normal_pcap_dir):

		# parse pcap into an object
		pcap_obj = rdpcap(normal_pcap_dir + normal_pcap_name)

		# hash for current pcap file
		pcap_hash = MinHash()

		# create the hash object
		for packet in pcap_obj:
			pcap_hash.update(str(packet).encode("utf8"))

		# add to the dataframe of hashes
		normal_hashes.append(pcap_hash)
	print("done")

	print("Hashing malware traffic...", end="")
	# populate the malware hashes dataframe
	for malware_pcap_name in os.listdir(malware_pcap_dir):

		# parse pcap into an object
		pcap_obj = rdpcap(malware_pcap_dir + malware_pcap_name)

		# hash for current pcap file
		pcap_hash = MinHash()

		# create the hash object
		for packet in pcap_obj:
			pcap_hash.update(str(packet).encode("utf8"))

		# add to the dataframe of hashes
		malware_hashes.append(pcap_hash)
	print("done")

	return np.array(normal_hashes + malware_hashes)
