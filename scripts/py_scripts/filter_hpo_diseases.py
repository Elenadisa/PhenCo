#! /usr/bin/env python

def load_pairs(filename, threshold):
	file = open(filename)
	for line in file:
		line = line.rstrip("\n")
		HPOA, HPOB, diseases_number = line.split("\t")

		if int(diseases_number) >= threshold:
			print(HPOA, HPOB, sep ="\t")


########################################################################################################################################
#														OPTPARSE
########################################################################################################################################
import optparse

parser=optparse.OptionParser()

parser.add_option("-i", "--pairs_number_diseases", dest="pairs_number_diseases",
				help="pairs_number_diseases", metavar="FILE")
parser.add_option("-t", "--threshold", dest="threshold", 
                  help="hpo_percentage", type='float')

(options, arg) = parser.parse_args()

#######################################################################################################################################
pairs = load_pairs(options.pairs_number_diseases, options.threshold)