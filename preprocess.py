from datasketch import MinHash
import os
import pandas
import pickle
from scapy.all import *

#  TODO: CHANGE THE NORMAL AND MALWARE DIRECTORIES BEFORE YOU RUN THIS SCRIPT

if __name__ == '__main__':
	
	# directories where the pcap files are saved
	normal_pcap_dir = "/Users/karanraj/Documents/normal-traffic/"
	malware_pcap_dir = "/Users/karanraj/Documents/regin-malware/"

	# dataframes for storing hashes
	normal_hashes_df = pandas.DataFrame()
	malware_hashes_df = pandas.DataFrame()


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
		normal_hashes_df.append(pcap_hash)


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
		malware_hashes_df.append(pcap_hash)


	# save processed data into a pickled object
	with open("normal_hashes.obj","wb") as filehandler
		pickle.dump(normal_hashes_df, filehandler)

	with open("malware_hashes.obj","wb") as filehandler
		pickle.dump(malware_hashes_df, filehandler)
