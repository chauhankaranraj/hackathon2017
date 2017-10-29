from datasketch import MinHash
import numpy as np
import os
import pickle
from scapy.all import *

#  TODO: CHANGE THE NORMAL AND MALWARE DIRECTORIES BEFORE YOU RUN THIS SCRIPT

if __name__ == '__main__':

	# directories where the pcap files are saved
	normal_pcap_dir = "/media/nvidia/windows/normal-traffic/"
	malware_pcap_dir = "/media/nvidia/windows/regin-malware/"

	# dataframes for storing hashes
	normal_f_names = os.listdir(normal_pcap_dir)	
	malware_f_names = os.listdir(malware_pcap_dir)
	
	normal_hashes = np.zeros((len(normal_f_names), 128))
	malware_hashes = np.zeros((len(malware_f_names), 128))

	print("Hashing normal traffic...", end="")
	# populate the normal hashes dataframe
	for normal_pcap_name_idx in range(len(normal_f_names)):

		# parse pcap into an object
		pcap_obj = rdpcap(normal_pcap_dir + normal_f_names[normal_pcap_name_idx])

		# hash for current pcap file
		pcap_hash = MinHash()

		# create the hash object
		for packet in pcap_obj:
			pcap_hash.update(str(packet).encode("utf8"))
		

		# add to the dataframe of hashes
		normal_hashes[normal_pcap_name_idx, :] = pcap_hash.hashvalues
	print("done")

	print("Hashing malware traffic...", end="")
	# populate the malware hashes dataframe
	for malware_pcap_name_idx in range(len(malware_f_names)):

		# parse pcap into an object
		pcap_obj = rdpcap(malware_pcap_dir + malware_f_names[malware_pcap_name_idx])

		# hash for current pcap file
		pcap_hash = MinHash()

		# create the hash object
		for packet in pcap_obj:
			pcap_hash.update(str(packet).encode("utf8"))

		# add to the dataframe of hashes
		malware_hashes[malware_pcap_name_idx, :] = pcap_hash.hashvalues
	print("done")

	return np.array(normal_hashes + malware_hashes)


if __name__ == "__main__":
	test_array = process_raw_data(normal_pcap_dir="/media/nvidia/windows/normal-traffic/", malware_pcap_dir="/media/nvidia/windows/regin-malware/")
