#! /usr/bin/env python
##############################################################################################################################################
#															METHODS
##############################################################################################################################################
import functions as fn

##############################################################################################################################################
#															OPTPARSE
##############################################################################################################################################
import optparse

parser = optparse.OptionParser()

parser.add_option("-f", "--dictionary", dest="dictionary",
                  help="Input file DECIPHER network", metavar="FILE")
parser.add_option("-A", "--key col", dest="key_col", 
                  help="key_column", type='int')
parser.add_option("-a", "--value_col", dest="value_col", 
                  help="value_column", type='int')

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
dictionary = fn.build_dictionary(options.dictionary, options.key_col, options.value_col)
network = open(options.network)

for line in network:
	line = line.rstrip("\n")
	hp1, hp2 = line.split("\t") #two or three fields
	
	if hp1 in dictionary:
		rels_1 = dictionary[hp1]
	else :
		rels_1 = []

	if hp2 in dictionary:
		rels_2 = dictionary[hp2]
	else :
		rels_2 = []
	
	file_output.write(str(hp1) + "\t" + str(hp2) + "\t" + str(rels_1)[1:-1] + "\t" + str(rels_2)[1:-1] + "\t" + options.model + "\n")
