#! /usr/bin/env python

import functions as fn

########################################################################################################################################
#														OPTPARSE
########################################################################################################################################
import optparse

parser=optparse.OptionParser()

parser.add_option("-l", "--list_file", dest="list_file", 
                  help="file with data for filter", metavar="FILE")

parser.add_option("-i", "--input_file", dest="input_file", 
                  help="file_to_filter", metavar="FILE")
parser.add_option("-c", "--col", dest="col", 
                  help="column with with have values to filter", type='int')

(options, arg) = parser.parse_args()

#######################################################################################################################################
#														MAIN
#######################################################################################################################################

l = fn.load_list_from_a_file(options.list_file)

file = open(options.input_file)

print("Patient","Cluster","Shared_hpos","Systems","Genes", sep="\t")

for line in file:
	line = line.rstrip("\n")
	fields = line.split("\t")

	element = fields[options.col]
	if element in l:
		print(fields[0], fields[1], fields[2], fields[4], fields[5], sep="\t")