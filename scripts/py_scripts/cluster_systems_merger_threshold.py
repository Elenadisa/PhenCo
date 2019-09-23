#! /usr/bin/env python

def build_clusters_dictionary(filename, hpo1_col, hpo2_col, id_col, key):
	dictionary = {}
	file = open(filename)
	if key == "cluster":
		for line in file:
			line = line.rstrip("\n")
			fields = line.split(" ")
			hpo1 = fields[hpo1_col]
			hpo2 = fields[hpo2_col]
			value = hpo1 + "-" + hpo2
			id_value = fields[id_col]
			
			if id_value not in dictionary:
				dictionary[id_value] = [value]
			else :
				if value not in dictionary[id_value]:
					dictionary[id_value].append(value)

	elif key == "hpo":
		for line in file:
			line = line.rstrip("\n")
			fields = line.split("\t")
			hpo1 = fields[hpo1_col]
			hpo2 = fields[hpo2_col]
			id_value = hpo1 + "-" + hpo2
			value = fields[id_col]
			
			if id_value not in dictionary:
				dictionary[id_value] = [value]
			else :
				if value not in dictionary[id_value]:
					dictionary[id_value].append(value)



	return dictionary

def load_pair_files(filename, key_col, value_col):
	dictionary = {}
	file = open(filename)
	
	for line in file:
		line = line.rstrip("\n")
		fields = line.split("\t")
		key_id = fields[key_col]
		value = fields[value_col]
		
			
		if key_id not in dictionary:
			dictionary[key_id] = [value]
		else :
			if value not in dictionary[key_id]:
				dictionary[key_id].append(value)

	return dictionary




########################################################################################################################################
#														OPTPARSE
########################################################################################################################################
import optparse

parser=optparse.OptionParser()

parser.add_option("-c", "--cluster_file", dest="cluster_file_for_cytoscape", 
                  help="clustering.R output", metavar="FILE")
parser.add_option("-A", "--hpo1_cytoscape", dest="hpo1_cytoscape", 
                  help="column which have hpo 1 in cytoscape file", type='int')
parser.add_option("-a", "--hpo_2_cytoscape", dest="hpo2_cytoscape", 
                  help="column which have hpo 2 in cytoscape file", type='int')
parser.add_option("-x", "--cluster_id", dest="cluster_id", 
                  help="column which have cluster id in cytoscape file", type='int')
parser.add_option("-d", "--dictionary file", dest="pathway_file", 
				  help="Enrichment dictionary", metavar="FILE")
parser.add_option("-B", "--hpo1_pathways", dest="hpo1_pathways", 
                  help="column which have hpo 1 in pathways file", type='int')
parser.add_option("-b", "--hpo_2_pathways", dest="hpo2_pathways", 
                  help="column which have hpo 2 in pathways file", type='int')
parser.add_option("-y", "--system_id", dest="system_id", 
                  help="column which have system id in pathways file", type='int')
parser.add_option("-s", "--single enrichment file", dest="single_file", 
				  help="Single Enrichment dictionary", metavar="FILE")
parser.add_option("-E", "--hpo_single_enrichment", dest="hpo_single", 
                  help="column which have hpo ", type='int')
parser.add_option("-e", "--hpo_pathways_single", dest="pathway_single", 
                  help="column which have pathways ", type='int')
parser.add_option("-o", "--output file", dest="output", 
				  help="output file", metavar="FILE")
parser.add_option("-t", "--threshold", dest="threshold", 
                  help="threshold", type='int')




(options, arg) = parser.parse_args()

#######################################################################################################################################
#														MAIN
#######################################################################################################################################
import numpy

cluster_dictionary = build_clusters_dictionary(options.cluster_file_for_cytoscape, options.hpo1_cytoscape, options.hpo2_cytoscape, options.cluster_id, key="cluster")
pathway_dictionary = build_clusters_dictionary(options.pathway_file, options.hpo1_pathways, options.hpo2_pathways, options.system_id, key ="hpo")
single_pathways_dictionary = load_pair_files(options.single_file, options.hpo_single, options.pathway_single)

o_file = open(options.output, 'w')


for cluster, HPO_pairs in cluster_dictionary.items():
	cluster_hpo_dictionary = dict()
	for hpos in HPO_pairs:
		if hpos in pathway_dictionary:
			pair_systems = pathway_dictionary[hpos]
			pair = hpos.split("-")
			
			for node in pair:

				if node not in cluster_hpo_dictionary:
					cluster_hpo_dictionary[node] = []
					for system in pair_systems:
						cluster_hpo_dictionary[node].append(system)

					if node in single_pathways_dictionary:
						single_systems = single_pathways_dictionary[node]
						for single_system in single_systems:
							if single_system not in cluster_hpo_dictionary[node]:
								cluster_hpo_dictionary[node].append(single_system)

				else:
					for system in pair_systems:
						if system not in cluster_hpo_dictionary[node]:
							cluster_hpo_dictionary[node].append(system)

	all_keys = list(cluster_hpo_dictionary.keys())
	all_values = list(cluster_hpo_dictionary.values())
	values = sum(all_values, [])
	unique_values = set(values)
	for element in unique_values:
		times = values.count(element)
		coherence_score = (times * 100) / len(all_keys)
		if coherence_score >= options.threshold:
			o_file.write(cluster + "\t" + element + "\t" + str(coherence_score) +"\n")
			for term in all_keys:
				print(term, cluster, sep="\t")

