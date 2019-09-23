#! /usr/bin/env python

import functions as fn


#############################################################################################################################################################################
#																		OPTPARSE																							#	
#############################################################################################################################################################################
import optparse

parser=optparse.OptionParser()

parser.add_option("-c", "--clusters_file", dest="clusters_hpo_file",
					help="File with clusters and HPO clustering.R output", metavar="FILE")
parser.add_option("-A", "--key_cluster_id", dest="cluster_hpo_id", 
                  help="column which have clusters identificators", type='int')
parser.add_option("-a", "--cluster_value", dest="cluster_hpo_value", 
                  help="column with HPO terms", type='int')
parser.add_option("-p", "--patients_hpo_file", dest="patients_hpo_file",
					help="File with patients and their hpos", metavar="FILE")
parser.add_option("-B", "--key_patients_hpo_id", dest="patients_hpo_id", 
                  help="column which have patients identificators", type='int')
parser.add_option("-b", "--patiens_hpo_value", dest="patients_hpo_value", 
                  help="column with HPO", type='int')
parser.add_option("-s", "--cluster_system_file", dest="cluster_system_file",
					help="File with clusters and their coincidence system", metavar="FILE")
parser.add_option("-D", "--key_cluster_systems_id", dest="cluster_system_id", 
                  help="column which have cluster id", type='int')
parser.add_option("-d", "--cluster_system_value", dest="cluster_system_value", 
                  help="column with systems", type='int')
parser.add_option("-S", "--system_gene_file", dest="system_gene_file",
					help="File with clusters and their coincidence system", metavar="FILE")
parser.add_option("-E", "--key_system_gene_id", dest="system_gene_id", 
                  help="column which have system id", type='int')
parser.add_option("-e", "--system_gene_value", dest="system_gene_value", 
                  help="column with genes", type='int')
parser.add_option("-P", "--patient_gene_file", dest="patient_gene_file",
					help="File with patients and their genes", metavar="FILE")
parser.add_option("-F", "--key_patient_gene_id", dest="patient_gene_id", 
                  help="column which have patient id", type='int')
parser.add_option("-f", "--patient_gene_value", dest="patient_gene_value", 
                  help="column with genes in patients", type='int')
parser.add_option("-g", "--gene_symbol_file", dest="gene_symbol_file",
					help="File with genes their symbols", metavar="FILE")
parser.add_option("-I", "--key_gene_symbol_id", dest="gene_symbol_id", 
                  help="column which have genes id", type='int')
parser.add_option("-i", "--gene_symbol_value", dest="gene_symbol_value", 
                  help="column with symbols", type='int')

parser.add_option("-t", "--shared_hpo_threshold", dest="shared_hpo_threshold", 
                  help="shared_hpo_threshold", type='int')
parser.add_option("-n", "--gene_number_threshold", dest="gene_number_threshold", 
                  help="gene_number_threshold", type='int')

(options, arg) = parser.parse_args()
#############################################################################################################################################################################
#																		MAIN																								#
#############################################################################################################################################################################
clusters_hpo_dictionary = fn.build_dictionary(options.clusters_hpo_file, options.cluster_hpo_id, options.cluster_hpo_value)				#return dictionary
patients_hpo_dictionary = fn.build_dictionary(options.patients_hpo_file, options.patients_hpo_id, options.patients_hpo_value)				#return dictionary
clusters_systems_dictionary = fn.build_dictionary(options.cluster_system_file, options.cluster_system_id, options.cluster_system_value)	#return dictionary
systems_genes_dictionary = fn.build_dictionary(options.system_gene_file, options.system_gene_id, options.system_gene_value)				#return dictionary
patients_genes_dictionary = fn.build_dictionary(options.patient_gene_file, options.patient_gene_id, options.patient_gene_value)			#return dictionary
genes_symbol_dictionary = fn.build_dictionary(options.gene_symbol_file, options.gene_symbol_id, options.gene_symbol_value)					#return dictionary

print("Patient" + "\t" + "Cluster" + "\t" + "Shared_hpos" + "\t" + "Patient_profile" + "\t" + "Systems" + "\t" + "Genes")

#For each patient and hpos in patient_hpo dictionary
for patient, hpos in patients_hpo_dictionary.items():
	patient_profile = set(hpos)										#get a set of the patient profile
	if patient in patients_genes_dictionary:						#look for the genes associated to the patient
		patient_genes = patients_genes_dictionary[patient]
		patient_genes_symbol = []

		for gene in patient_genes:
			if gene in genes_symbol_dictionary:
				patient_genes_symbol.append("".join(genes_symbol_dictionary[gene]))		#Translate each gene entrez id to gene symbol and save them in a list

		patient_genes_symbol = set(patient_genes_symbol)			#Get a set of patient's genes 
		


	#For each cluster and systems in cluster_systems dictionary
	for cluster, systems in clusters_systems_dictionary.items():
		cluster_profile = set(clusters_hpo_dictionary[cluster])		#get a set of hpos in the cluster

		shared_hpos = patient_profile.intersection(cluster_profile)	# look for common hpos between the patient profile and the clusters hpos

		if len(shared_hpos) >= options.shared_hpo_threshold:		#If the number of common hpos is greater than a threshold
			
			for element in systems:	 								#look for the genes related to the system		
				
				if element in systems_genes_dictionary:
					
					system_genes = set(systems_genes_dictionary[element])	#get the set of systems genes

				gene_intersection = patient_genes_symbol.intersection(system_genes) # look for common genes between patient and systems

				if len(gene_intersection) >= options.gene_number_threshold:		#If there are a number of common genes greater than a threshold it print:
					
					print(patient, cluster, ", ".join(shared_hpos), ", ".join(patient_profile), element, ", ".join(gene_intersection), sep="\t")