#! /usr/bin/env python

#############################################################################################################################################################################
#																		FUNCTIONS																								#
#############################################################################################################################################################################

import functions as fn

#############################################################################################################################################################################
#																		OPTPARSE																							#	
#############################################################################################################################################################################
import optparse

parser=optparse.OptionParser()

parser.add_option("-c", "--clusters_file", dest="clusters_file",
					help="File with clusters and HPO clustering.R output", metavar="FILE")
parser.add_option("-p", "--patients_file", dest="patients_file",
					help="File with patients and HPO", metavar="FILE")
parser.add_option("-A", "--key_cluster_id", dest="cluster_id", 
                  help="column which have clusters identificators", type='int')
parser.add_option("-B", "--key_patient_id", dest="patient_id", 
                  help="column which have systems", type='int')
parser.add_option("-x", "--cluster_value", dest="cluster_value", 
                  help="column with HPO terms", type='int')
parser.add_option("-y", "--patient_value", dest="patient_value", 
                  help="column with hpo terms", type='int')
parser.add_option("-l", "--length_hpo_profile", dest="length_hpo_profile",
				help="minimun length of the hpo profile", type='int')
parser.add_option("-s", "--length_shared_hpo", dest="number_of_shared_hpo",
				help="minimun number of shared hpo with the cluster", type='int')


(options, arg) = parser.parse_args()
#############################################################################################################################################################################
#																		MAIN																								#
#############################################################################################################################################################################

patient_dictionary = fn.build_dictionary(options.patients_file, options.patient_id, options.patient_value) #dictionary with patients as keys and hpos as values
cluster_dictionary = fn.build_dictionary(options.clusters_file, options.cluster_id, options.cluster_value) #dictionary with clusters_ids as keyas and hpos as values

print("Cluster" + "\t" + "Patient" + "\t" + "Shared_hpo" + "\t" + "Patient_profile")		#output file's header

#for each patient and their hpos
for patient, HPO_patient in patient_dictionary.items() :

	if len(HPO_patient) > options.length_hpo_profile:		#If patients profile is greater than a certain threshold

		#for each cluster and their hpos
		for cluster, HPO_cluster in cluster_dictionary.items():

			shared_hpo = list(set(HPO_cluster) & set(HPO_patient))		#Get the common hpos for the patient and the cluster

			not_in_cluster = [x for x in HPO_patient if x not in shared_hpo]	#Get the hpos of the patient that isn't in the cluster

			if len(shared_hpo) >= options.number_of_shared_hpo:
				print(cluster, patient, ", ".join(shared_hpo), ", ".join(not_in_cluster), sep="\t")
