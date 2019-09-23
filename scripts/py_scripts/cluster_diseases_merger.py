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

parser.add_option("-a", "--cluster_file", dest="cluster_file", 
                  help="clustering.R output", metavar="FILE")
parser.add_option("-b", "--dictionary file", dest="diseases_dictionary", 
				  help="OMIM/ORPHA-HPO dictionary", metavar="FILE")
parser.add_option("-A", "--cluster_id", dest="cluster_id", 
                  help="column which have clusters identificators", type='int')
parser.add_option("-B", "--disease_id", dest="disease_id", 
                  help="column which have diseases identificators", type='int')
parser.add_option("-x", "--hpo_cluster", dest="hpo_cluster", 
                  help="column with HPO terms", type='int')
parser.add_option("-y", "--hpo_disease", dest="hpo_disease", 
                  help="column with HPO terms", type='int')
parser.add_option("-t", "--thresehold", dest="thresehold", 
                  help="permited errors", type='float')

(options, arg) = parser.parse_args()

#######################################################################################################################################
#														MAIN
#######################################################################################################################################
a_pairs = fn.build_dictionary(options.cluster_file, options.cluster_id, options.hpo_cluster) #return a dictionary
b_pairs = fn.build_dictionary(options.diseases_dictionary, options.disease_id, options.hpo_disease) #return a dictionary

# For each entry (cluster) in the dictionary calculate the number of values (HPO)
for cluster_a in a_pairs:
	a_length = len(a_pairs[cluster_a])

	#For each entry (disease) in the dictionary:
	for disease in b_pairs:
		intersection = list(set(a_pairs[cluster_a]) & set(b_pairs[disease]))	#calculate the intersection of values of both dictionaries (commom elements).
		intersection_length = len(intersection)									#Calculate the length of the intersection.

		if intersection_length >= (a_length - options.thresehold) :				#If the intersection is equal or greater to a certain threshold it print the keys of both dictionarys
			print(cluster_a + "\t" + disease + "\t" + ", ".join(intersection))