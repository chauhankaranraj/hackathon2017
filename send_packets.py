from scapy.all import *
from scapy.utils import rdpcap

pcap_obj = rdpcap("/Volumes/windows/regin-malware/00badda4-2f68-4cfb-9d1a-49bcc14c6d2b.pcap")  # could be used like this rdpcap("filename",500) fetches first 500 pkts

pkt_cnt = 0
p_out = []

dst_ip = "10.192.196.122"
for p in pcap_obj:
	pkt_cnt += 1
	new_pkt = p.payload
	new_pkt[IP].dst = dst_ip

	sendp(p)


pcap_obj = rdpcap("/Volumes/windows/regin-malware/00badda4-2f68-4cfb-9d1a-49bcc14c6d2b.pcap")  # could be used like this rdpcap("filename",500) fetches first 500 pkts
# pkt = pcap_obj[2]

# # new_dst_mac = "9C:B6:D0:1C:A5:A9"
# # new_dst_ip = "10.192.196.122"

# # new_src_mac = "a0:99:9b:1c:2d:4b"
# # new_src_ip = "10.192.193.109"

# pkt.sprintf()

# send(IP(src="10.192.193.109", dst="10.192.196.122")/TCP()/pkt.payload)

# sendp(rdpcap("/Volumes/windows/regin-malware/00badda4-2f68-4cfb-9d1a-49bcc14c6d2b.pcap"))

# # for pkt in pcap_obj:


# print("sending...")

# pkt.src = new_src_mac  	# i.e new_src_mac="00:11:22:33:44:55"
# pkt.dst = new_dst_mac

# print(pkt.src)
# print(pkt.dst)

# # pkt["IP"].src = new_src_ip 		# i.e new_src_ip="255.255.255.255"
# # pkt["IP"].dst = new_dst_ip

# sendp(pkt) 						# sending packet at layer 2