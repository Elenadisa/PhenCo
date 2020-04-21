#! /usr/bin/env python

import functions as fn

def load_dictionary(filename, key_col, value_col):
	file = open(filename)
	dictionary = dict()

	for line in file:
		line=line.rstrip("\n")
		fields = line.split("\t")

		key = fields[key_col]
		value = fields[value_col]
		hpo_l = value.split(", ")

		if key not in dictionary:
			dictionary[key] = []

			for hpo in hpo_l:
				if hpo not in dictionary[key]:
					dictionary[key].append(hpo)
		else:
			for hpo in hpo_l:
				if hpo not in dictionary[key]:
					dictionary[key].append(hpo)
	
	return(dictionary)


def search_in_dictionary(dictionary, key):
	if key in dictionary:
		l = dictionary[key]
	else:
		l = []
	return(l)


########################################################################################################################################
#														OPTPARSE
########################################################################################################################################
import optparse

parser=optparse.OptionParser()

parser.add_option("-p", "--patient_file", dest="patient_file", 
                  help="patient file", metavar="FILE")
parser.add_option("-A", "--key_pat_col", dest="key_patient", 
                  help="column with key in file", type='int')
parser.add_option("-a", "--value_pat_col", dest="value_patient", 
                  help="column with value in file", type='int')

parser.add_option("-g", "--go_cluster_file", dest="go_cluster_file", 
                  help="go cluster file", metavar="FILE")
parser.add_option("-k", "--kegg_cluster_file", dest="kegg_cluster_file", 
                  help="kegg_cluster file", metavar="FILE")
parser.add_option("-r", "--reactome_cluster_file", dest="reactome_cluster_file", 
                  help="reactome_cluster file", metavar="FILE")
parser.add_option("-B", "--key_col", dest="key_cluster", 
                  help="column with key in file", type='int')
parser.add_option("-b", "--value_col", dest="value_cluster", 
                  help="column with value in file", type='int')
parser.add_option("-D", "--gene_col", dest="gene_col", 
                  help="column with genes in file", type='int')

parser.add_option("-o", "--output_file", dest="output_file", 
                  help="output file", metavar="FILE")

parser.add_option("-f", "--gene_file", dest="gene_file", 
                  help="gene file", metavar="FILE")
parser.add_option("-C", "--key_gene_col", dest="key_gene", 
                  help="column with key in gene file", type='int')
parser.add_option("-c", "--value_gene_col", dest="value_gene", 
                  help="column with value in gene file", type='int')


(options, arg) = parser.parse_args()

#######################################################################################################################################
#														MAIN
#######################################################################################################################################
go_hpos = load_dictionary(options.go_cluster_file, options.key_cluster, options.value_cluster)
go_gene = load_dictionary(options.go_cluster_file, options.key_cluster, options.gene_col)

kegg_hpos = load_dictionary(options.kegg_cluster_file, options.key_cluster, options.value_cluster)
kegg_gene = load_dictionary(options.kegg_cluster_file, options.key_cluster, options.gene_col)

reactome_hpos = load_dictionary(options.reactome_cluster_file, options.key_cluster, options.value_cluster)
reactome_gene = load_dictionary(options.reactome_cluster_file, options.key_cluster, options.gene_col)

pat2gene_dict = load_dictionary(options.gene_file, options.key_gene, options.value_gene)


#print(patient_hpos_overlap_in_cluster)
patient_profile_dict = fn.build_dictionary(options.patient_file, options.key_patient, options.value_patient)

output_file = open(options.output_file, 'w')
patient_hpo_file = open(options.patient_file)

output_file.write("Patient" + "\t" + "Metric" + "\t" + "Number" + "\n")

patient_l = []

for line in patient_hpo_file:

	line = line.rstrip("\n")
	fields = line.split("\t")

	patient = fields[options.key_patient]
	hpo = fields[options.value_patient]

	go_hpo_l = search_in_dictionary(go_hpos, patient)
	kegg_hpo_l = search_in_dictionary(kegg_hpos, patient)
	reactome_hpo_l = search_in_dictionary(reactome_hpos, patient)

	
	go_gene_l = search_in_dictionary(go_gene, patient)
	kegg_gene_l = search_in_dictionary(kegg_gene, patient)
	reactome_gene_l = search_in_dictionary(reactome_gene, patient)

	predicted_gene_l = set(go_gene_l + kegg_gene_l + reactome_gene_l)

	
	cluster_hpo_l = set(go_hpo_l + kegg_hpo_l + reactome_hpo_l)
	
	if hpo in cluster_hpo_l:
		print(fields[0], fields[1], fields[2], sep="\t")

	if patient not in patient_l:
		patient_l.append(patient)
		output_file.write(patient + "\t" + "Total number of HPOs" + "\t" + str(len(patient_profile_dict[patient])) + "\n")
		output_file.write(patient + "\t" + "Total HPOs overlapping clusters" + "\t" + str(len(cluster_hpo_l)) + "\n")
		if patient in pat2gene_dict:
			output_file.write(patient + "\t" + "Number of genes in patient's CNV" + "\t" + str(len(pat2gene_dict[patient])) + "\n")
			output_file.write(patient + "\t" + "Number of possible patogenic genes" + "\t" + str(len(predicted_gene_l)) + "\n")

		