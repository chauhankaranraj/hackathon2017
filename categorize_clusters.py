import pickle
import numpy as np


def main():
    with open('assignments.obj', 'rb') as fHandler:
        assignments = pickle.load(fHandler)
    with open('centroids.obj', 'rb') as fHandler:
        centroids = pickle.load(fHandler)
    categorize_clusters(assignments)

def categorize_clusters(assignments):
    number_of_normal_packets = 9
    clusters = dict()

    # find number of normal packets per cluster
    for i in range(0,number_of_normal_packets):
        if assignments[i] in clusters.keys():
            (clusters[assignments[i]])["normal"] += 1 
        else:
            number_of_pcaps = dict()
            number_of_pcaps["mal"] = 0
            number_of_pcaps["normal"] = 1
            clusters[assignments[i]] = number_of_pcaps

    # find number of malware packets per cluster
    for i in range(number_of_normal_packets, len(assignments)):
        if assignments[i] in clusters.keys():
            if "mal" in (clusters[assignments[i]]).keys():
                (clusters[assignments[i]])["mal"] += 1 
            else:
                (clusters[assignments[i]])["mal"] = 1 
        else:
            number_of_pcaps = dict()
            number_of_pcaps["mal"] = 1
            number_of_pcaps["normal"] = 0
            clusters[assignments[i]] = number_of_pcaps

    # find probability 
    # (divide number of packets per cluster by total number of type packets)
    for cluster in clusters:
        for category in clusters[cluster]: 
            # get number of mal packets in cluster
            if category == "mal":
                num_mal_packets = (clusters[cluster])[category]
            # get number of normal packets in cluster
            if category == "normal":
                num_normal_packets = (clusters[cluster])[category]

        # calculate total packets in cluster
        total_packets_in_cluster = num_mal_packets + num_normal_packets

        # find probability of mal and normal packets in cluster
        (clusters[cluster])["mal"] = num_mal_packets/total_packets_in_cluster
        (clusters[cluster])["normal"] = num_normal_packets/total_packets_in_cluster

    return clusters
    
if __name__ == '__main__':
    main()
