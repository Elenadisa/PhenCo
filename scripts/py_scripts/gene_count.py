#! /usr/bin/env python
##############################################################################################################################################
#															METHODS
##############################################################################################################################################
def build_dictionary(filename):
	hp_gene_dictionary = {}
	file = open(filename)
	for line in file:
		line = line.rstrip("\n")
		fields = line.split("\t")
		hp = fields[0]
		gene=fields[1]

		if hp not in hp_gene_dictionary:
			hp_gene_dictionary[hp] = [gene]
		else :
			hp_gene_dictionary[hp].append(gene)

	return hp_gene_dictionary


##############################################################################################################################################
#															OPTPARSE
##############################################################################################################################################
import optparse
parser = optparse.OptionParser()
parser.add_option("-f", "--dictionary", dest="dictionary",
                  help="Input file DECIPHER network", metavar="FILE")
parser.add_option("-n", "--network", dest="network",
                  help="Network to analyse", metavar="FILE")
parser.add_option("-o", "--foutput", dest="output",
                  help="output file", metavar="FILE")
parser.add_option("-m", "--model", dest="model",
                  help="network_type", metavar="str")

(options, args) = parser.parse_args()

###############################################################################################################################################
# 															MAIN
###############################################################################################################################################
import numpy as np

file_output = open(options.output, 'w')
dictionary = build_dictionary(options.dictionary)
network = open(options.network)

union_gene_number = []
intersection_gene_number = []

#For each line in network file
for line in network:
	
	line = line.rstrip("\n")
	hp1, hp2 = line.split("\t") #two or three fields
	
	if hp1 in dictionary:
		rels_1 = dictionary[hp1]		#Get the genes of the first hpo
	else :
		rels_1 = []

	if hp2 in dictionary:
		rels_2 = dictionary[hp2]		#Get the genes of the second hpo
	else :
		rels_2 = []
	
	union_genes = sorted(set(rels_1 + rels_2))	#Get the union genes of first and second hpo
	
	intersection_genes = list(set(rels_1) & set(rels_2))			#Get the intersection genes of first and second hpo
	#print(hp1 + "-" + hp2 + "\t" + str(len(current_rels)))
	
	union_gene_number.append(len(union_genes))
	
	intersection_gene_number.append(len(intersection_genes))
	
	file_output.write(str(hp1) + "\t" + str(hp2) + "\t" + str(len(rels_1)) + "\t" + str(len(rels_2)) + "\t" + str(len(union_genes)) + "\t" + str(len(intersection_genes)) + "\t" + options.model + "\n")

#mean = np.mean(union_gene_number)
#sd =  np.std(union_gene_number)
#print("union_gene_average_per_HPO_pair", mean, sep="\t")
#print("union_gene_sd_per_HPO_pair", sd, sep="\t")