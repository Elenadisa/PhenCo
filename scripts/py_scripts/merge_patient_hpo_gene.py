#! /usr/bin/env python

########################################################################################################################################
#														METHODS
########################################################################################################################################
import functions as fn


########################################################################################################################################
#														OPTPARSE
########################################################################################################################################
import optparse

parser=optparse.OptionParser()

parser.add_option("-p", "--patients_file", dest="patient_hpo_file", 
                  help="pat_phen_file", metavar="FILE")
parser.add_option("-A", "--key_pat_id", dest="patient_id_1", 
                  help="column which have clusters identificators", type='int')
parser.add_option("-a", "--hpo_pat", dest="hpo_patients", 
                  help="column with HPO terms", type='int')
parser.add_option("-f", "--phen_gene_file", dest="phen_gene_file", 
                  help="netanalyser output", metavar="FILE")
parser.add_option("-B", "--key_hpo_gene_id", dest="hpo_id_1", 
                  help="column which have hpo identificators", type='int')
parser.add_option("-b", "--gene_hpo", dest="gene_hpo", 
                  help="column with gene terms", type='int')
parser.add_option("-g", "--pat_gene_file", dest="pat_gene_file", 
                  help="netanalyser output", metavar="FILE")
parser.add_option("-C", "--key_patient_id", dest="patient_id_2", 
                  help="column which have hpo identificators", type='int')
parser.add_option("-c", "--gene_pat", dest="gene_pat", 
                  help="column with gene terms", type='int')
parser.add_option("-n", "--phen_name_file", dest="phen_name_file", 
                  help="netanalyser output", metavar="FILE")
parser.add_option("-D", "--key_hpo_name_id", dest="hpo_id_2", 
                  help="column which have hpo identificators", type='int')
parser.add_option("-d", "--name", dest="name_hpo", 
                  help="column with name terms", type='int')
parser.add_option("-s", "--entrez_2_symbol_file", dest="gene_symbol_file", 
                  help="entrez 2 gene symbol", metavar="FILE")
parser.add_option("-E", "--key_gene_name_id", dest="gene_id", 
                  help="column which have gene identificators", type='int')
parser.add_option("-e", "--symbol", dest="gene_symbol", 
                  help="column with gene symbol", type='int')

(options, arg) = parser.parse_args()

#######################################################################################################################################
#														MAIN
#######################################################################################################################################

patient_hpo_dictionary = fn.build_dictionary(options.patient_hpo_file, options.patient_id_1, options.hpo_patients)
hpo_gene_dictionary = fn.build_dictionary(options.phen_gene_file, options.hpo_id_1, options.gene_hpo)
patient_gene_dictionary = fn.build_dictionary(options.pat_gene_file, options.patient_id_2, options.gene_pat)
hpo_name_dictionary = fn.build_dictionary(options.phen_name_file, options.hpo_id_2, options.name_hpo)
gene_symbol_dictionary = fn.build_dictionary(options.gene_symbol_file, options.gene_id, options.gene_symbol)

print("Patient", "HPO", "Name", "Genes", sep="\t")

#For each patients and their hpos in patient_hpo dictionary and for each hpo

for patient, HPOs in patient_hpo_dictionary.items():

	for HPO in HPOs:

		if HPO in hpo_gene_dictionary and patient in patient_gene_dictionary: #look for hpo genes and patients genes

			gene_intersection = list(set(hpo_gene_dictionary[HPO]) & set(patient_gene_dictionary[patient]))	#get common genes of patients and hpos
			hpo_name = hpo_name_dictionary[HPO]		#get the name of the HPO


			if len(gene_intersection) > 0:		#If there are common genes between patient and hpo
				gene_symbol_l = list()
				for gene in gene_intersection: 	#Translate the gene entrez id to gene symbol

					if gene in gene_symbol_dictionary:
						gene_symbol = gene_symbol_dictionary[gene]
						gene_symbol_l.append("".join(gene_symbol))
					
				print(patient, HPO, "".join(hpo_name), ', '.join(map(str, gene_symbol_l)), sep="\t")

			else:
				print(patient, HPO, "".join(hpo_name), "-", sep="\t")

