#! /usr/bin/env python

import functions as fn


########################################################################################################################################
#														OPTPARSE
########################################################################################################################################
import optparse

parser=optparse.OptionParser()

parser.add_option("-p", "--patients_file", dest="patient_file", 
                  help="clustering.R output", metavar="FILE")
parser.add_option("-s", "--system file", dest="system_file", 
				  help="system file", metavar="FILE")
parser.add_option("-A", "--key_hpo_id", dest="patient_id", 
                  help="column which have clusters identificators", type='int')
parser.add_option("-B", "--key_system_id", dest="system_id", 
                  help="column which have systems", type='int')
parser.add_option("-x", "--hpo", dest="hpo_patients", 
                  help="column with HPO terms", type='int')
parser.add_option("-y", "--system", dest="hpo_system", 
                  help="column with hpo terms", type='int')
parser.add_option("-t", "--threshold", dest="threshold", 
                  help="hpo_percentage", type='float')
parser.add_option("-q", "--number_hpo_patient", dest="number_hpo_patient", 
                  help="Threshold Number hpo per patient", type='float')
parser.add_option("-n", "--number_hpo_cluster", dest="number_hpo", 
                  help="threshold number of HPO per cluster", type='float')
parser.add_option("-c", "--number_cluster", dest="number_cluster", 
                  help="threshold number cluster", type='float')
(options, arg) = parser.parse_args()

#######################################################################################################################################
#														MAIN
#######################################################################################################################################
import numpy as np

patient_dictionary = fn.build_dictionary(options.patient_file, options.patient_id, options.hpo_patients)	#dictionary with patients as keys and hpos as values
systems_dictionary = fn.build_dictionary(options.system_file, options.system_id, options.hpo_system)		#dictionary with hpos of a cluster as keys and systems as values

print("Pat_id", "Prof_length", "Profile", "Number_of_HPO_explained", "Percetage_of_HPO_explained", "Nº_coincedence_clusters", "Cluster", "Avarage_HPO_per_cluster", "Higher_cluster_size", "Affected_HPO", "Systems", sep="\t")		#output file's header

#for each patient and their hpo in patient dictionary:
for patient, HPO_patient in patient_dictionary.items():

	if len(HPO_patient) > options.number_hpo_patient:		#If HPO profile of a patient is greater than a threshold

		intersection = []
		clusters_length = []
		uniq_hpo = []
		systems_list = []
		cluster = []
		cluster_number = 0
		higher_cluster_size = 0

		#For each cluster and systems in systems dictionary
		for HPO_cluster, cluster_systems in systems_dictionary.items():

				all_cluster_hpo = HPO_cluster[:].split(",")
				
				hpo_list = list(set(all_cluster_hpo) & set(HPO_patient))		#Get common HPOs of clusters and patients
				shared_hpo = ",".join(hpo_list)
				systems = ",".join(cluster_systems)
				cluster_hpo= ",".join(all_cluster_hpo)
								
				if len(hpo_list) >= options.number_hpo:						#If the number of common HPOs is greater than a threshold
					intersection.append(shared_hpo)							# Append shared HPOs to a list 
					clusters_length.append(len(hpo_list))					#Append cluster size to a list
					systems_list.append(systems)							#Append systems to a list
					cluster_number = cluster_number + 1						#Count one cluster that overlap with a patient
					cluster.append(cluster_hpo)								#Append hpos of the cluster to a list

					if len(hpo_list) > higher_cluster_size:
						higher_cluster_size = len(hpo_list)					#Get the highest number of common hpos with a cluster for the patient
					
					for hpo in hpo_list:
						
						if hpo not in uniq_hpo:
							uniq_hpo.append(hpo)							#Append the unic hpo to a list


		hpo_percentage = (len(uniq_hpo) * 100) / len(HPO_patient)			#Get the HPO percetage that overlap with clusters of a patient
		
		
		if hpo_percentage > options.threshold:								#If the percentage of hpo of a patient that overlap with clusters in greater than a threshold
			
			if cluster_number > options.number_cluster:						#If a patient overlap with a number of clusters greater than a threshold
				
				#output is a line per patient, if a patient overlap with more than one patient every data of a cluster is separated by ;
				print(patient, len(HPO_patient), ";".join(HPO_patient), len(uniq_hpo), str(hpo_percentage),  str(cluster_number), ";".join(cluster), str(np.mean(clusters_length)), str(higher_cluster_size), ";".join(intersection), ";".join(systems_list), sep ="\t")

