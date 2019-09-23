#! /usr/bin/env python

##############################################################################################################################################
#															METHODS
##############################################################################################################################################


def build_dictionary(filename, key_col, value_col, omim):
	dictionary = {}
	file = open(filename)
	
	for line in file:
		line = line.rstrip("\n")
		fields = line.split("\t")
		if omim == 1 :
			key_id = "OMIM:" + fields[key_col]
		else:
			key_id = fields[key_col]
		
		value_name = fields[value_col]

		if key_id not in dictionary:
			dictionary[key_id] = [value_name]
		
		else :
			if value_name not in dictionary[key_id]:
				dictionary[key_id].append(value_name)


	return dictionary


##############################################################################################################################################
#															OPTPARSE
##############################################################################################################################################
import optparse

parser=optparse.OptionParser()

parser.add_option("-c", "--data_file", dest="cluster_file", 
                  help="cluster_data_file", metavar="FILE")
parser.add_option("-d", "--dictionary file", dest="dictionary_file", 
				  help="system file", metavar="FILE")
parser.add_option("-g", "--genes file", dest="genes_file", 
				  help="genes file", metavar="FILE")
parser.add_option("-A", "--key cluster id", dest="cluster_id", 
                  help="column which have clusters identificators", type='int')
parser.add_option("-a", "--third_column", dest="third_column", 
                  help="third_column", type='int')
parser.add_option("-B", "--key dictionary id", dest="dictionary_id", 
                  help="column of dictionary id", type='int')
parser.add_option("-F", "--key genes dictionary id", dest="genes_id", 
                  help="column of genes dictionary id", type='int')
parser.add_option("-x", "--cluster data", dest="cluster_value", 
                  help="column with HPO terms", type='int')
parser.add_option("-y", "--dictionary data", dest="dictionary_value", 
                  help="column with name of data", type='int')
parser.add_option("-z", "--genes dictionary data", dest="genes_value", 
                  help="column with gene symbol", type='int')
parser.add_option("-C", "--omim data", dest="omim_cluster", 
                  help="indicates if we want to look for OMIM data", type='int')
parser.add_option("-D", "--omim", dest="omim_dictionary", 
                  help="indicates if we want to look for OMIM data in de dictionary", type='int')
parser.add_option("-t", "--analysis_type", dest="analysis_type", 
                  help="analysis_type", type='str')

(options, arg) = parser.parse_args()

#######################################################################################################################################
#														MAIN
#######################################################################################################################################

cluster_file = open(options.cluster_file)
names_dictionary = build_dictionary(options.dictionary_file, options.dictionary_id, options.dictionary_value, options.omim_dictionary)

#If the file to analyse don't have systems or diseases
if options.analysis_type != "systems" and options.analysis_type != "diseases":
	
	print("Cluster" + "\t" + "Term" + "\t" + "Name")		#output file header
	
	#for each line in clusters file
	for line in cluster_file:
		lines = line.rstrip("\n")
		fields = line.split("\t")

		cluster_id = fields[options.cluster_id].rstrip("\n")
		value = fields[options.cluster_value].rstrip("\n")
		
		if value in names_dictionary:		#if the value is in names dictionary
			
			print(cluster_id, value, "".join(names_dictionary[value]), sep="\t")

#If the file to analyse have systems
elif options.analysis_type == "systems": 

	genes_dictionary = build_dictionary(options.genes_file, options.genes_id, options.genes_value, options.omim_dictionary)

	print("Cluster" + "\t" + "Term" + "\t" + "Name" + "\t" + "Genes" + "\t" + "Percentage_of_nodes_with_funsys")		#output file header
	
	#for each line in clusters file
	for line in cluster_file:
		lines = line.rstrip("\n")
		fields = line.split("\t")

		cluster_id = fields[options.cluster_id].rstrip("\n")
		value = fields[options.cluster_value].rstrip("\n")
		coherence_score = fields[options.third_column].rstrip("\n")
		
		if value in names_dictionary and value in genes_dictionary: 		#if the value is in both dictionaries
			
			print(cluster_id, value, "".join(names_dictionary[value]), ", ".join(genes_dictionary[value]), coherence_score, sep="\t")

#If the file to analyse have diseases
elif options.analysis_type == "diseases":

	print("Cluster" + "\t" + "Term" + "\t" + "Name" + "\t" + "HPOs_in_clusters")

	#for each line in clusters file
	for line in cluster_file:
		lines = line.rstrip("\n")
		fields = line.split("\t")

		cluster_id = fields[options.cluster_id].rstrip("\n")
		value = fields[options.cluster_value].rstrip("\n")
		coherent_hpos = fields[options.third_column].rstrip("\n")
		
		if value in names_dictionary:			#if the value is in names dictionaries
			
			print(cluster_id, value, "".join(names_dictionary[value]), coherent_hpos, sep="\t")


