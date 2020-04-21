#! /usr/bin/env python

#######################################################################################################################################
#														METHODS
######################################################################################################################################
import functions as fn



########################################################################################################################################
#														OPTPARSE
########################################################################################################################################
import optparse

parser=optparse.OptionParser()

parser.add_option("-p", "--patient_file", dest="patient_file", 
                  help="patient", metavar="FILE")

parser.add_option("-d", "--dictionary_file", dest="dictionary_file", 
                  help="dictionary file", metavar="FILE")
parser.add_option("-A", "--key_id", dest="key_id", 
                  help="column which have keys id", type='int')
parser.add_option("-a", "--value_patient_id", dest="value_id", 
                  help="column which have values identificators", type='int')

parser.add_option("-o", "--output_file", dest="output_file", 
                  help="output", metavar="FILE")

(options, arg) = parser.parse_args()

#######################################################################################################################################
#														MAIN
#######################################################################################################################################
gene_dict = fn.build_dictionary(options.dictionary_file, options.key_id, options.value_id)

file = open(options.patient_file)

output_file = open(options.output_file, 'w')

pat2gene_dict = dict()
for line in file:
	line = line.rstrip("\n")

	patient, gene = line.split("\t")

	if patient not in pat2gene_dict:
		def_gene = "".join(gene_dict[gene])
		pat2gene_dict[patient] = [def_gene]
	else:
		if gene not in pat2gene_dict[patient]:
			def_gene = "".join(gene_dict[gene])
			pat2gene_dict[patient].append(def_gene)

	print(patient, "".join(gene_dict[gene]), sep="\t")




for patient, genes in pat2gene_dict.items():
	output_file.write(patient + "\t" +  str(genes) + "\n")
