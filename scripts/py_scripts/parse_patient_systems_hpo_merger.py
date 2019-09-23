#! /usr/bin/env python

##############################################################################################################################################
#															METHODS
##############################################################################################################################################


def build_dictionary_without_header(filename, key_col, value_col, omim):
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


def build_dictionary_with_header(filename, key_col, value_col, omim):
	dictionary = {}
	f = open(filename).readlines()
	firstLine = f.pop(0) #removes the first line
	for line in f:

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
parser.add_option("-p", "--patient file", dest="patient_file", 
				  help="patient file", metavar="FILE")
parser.add_option("-A", "--key cluster id", dest="cluster_id", 
                  help="column which have clusters identificators", type='int')
parser.add_option("-B", "--key dictionary id", dest="dictionary_id", 
                  help="column of dictionary id", type='int')
parser.add_option("-C", "--key patient_file id", dest="patient_id", 
                  help="column of dictionary id", type='int')
parser.add_option("-x", "--cluster data", dest="cluster_value", 
                  help="column with HPO terms", type='int')
parser.add_option("-y", "--dictionary data", dest="dictionary_value", 
                  help="column with name of data", type='int')
parser.add_option("-z", "--patiente data", dest="patient_value", 
                  help="column with name of data", type='int')
parser.add_option("-O", "--omim data", dest="omim_cluster", 
                  help="indicates if we want to look for OMIM data", type='int')
parser.add_option("-o", "--omim", dest="omim_dictionary", 
                  help="indicates if we want to look for OMIM data in de dictionary", type='int')


(options, arg) = parser.parse_args()

#######################################################################################################################################
#														MAIN
#######################################################################################################################################

cluster_file = open(options.cluster_file)
names_dictionary = build_dictionary_without_header(options.dictionary_file, options.dictionary_id, options.dictionary_value, options.omim_dictionary)
patient_dictionary = build_dictionary_with_header(options.patient_file, options.patient_id, options.patient_value, options.omim_cluster)

print("Patient" + "\t" + "Cluster" + "\t" + "Term" + "\t" + "Name")	#output file header


#for each line in cluster file
for line in cluster_file:
	line = line.rstrip("\n")
	fields = line.split("\t")

	cluster_id = fields[options.cluster_id].rstrip("\n")
	value = fields[options.cluster_value].rstrip("\n")


	if cluster_id in patient_dictionary:		#if the cluster is in patient dictionary:

		for patient in patient_dictionary[cluster_id]:		#for each patient that overlap with the cluster

			if value in names_dictionary:				#Get the name for the value

				print(patient, cluster_id, value, "".join(names_dictionary[value]), sep = "\t")			