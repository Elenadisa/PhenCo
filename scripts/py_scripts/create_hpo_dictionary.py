#! /usr/bin/env python
##############################################################################################################################################
#															METHODS
##############################################################################################################################################
def build_dictionary(filename):
	file = open(filename)
	dictionary = dict()
	
	for line in file:
		line = line.rstrip("\n")
		fields = line.split(": ")
		
		if fields[0] == "id":
			hpo_id = fields[1]
			if hpo_id not in dictionary:
				dictionary[hpo_id] = []
		
		elif fields[0] == "name" :
			hpo_name = fields[1]
			dictionary[hpo_id].append(hpo_name)

		#elif fields[0] == "synonym":
			#hpo_name = fields[1]
			#dictionary[hpo_id].append(hpo_name)

		#elif fields[0] == "alt_id" :
			#alt_hpo_id = fields[1]
			#if alt_hpo_id not in dictionary:
				#dictionary[alt_hpo_id] = []
				#dictionary[alt_hpo_id] = dictionary[hpo_id]

	return(dictionary)
		



##############################################################################################################################################
#															OPTPARSE
##############################################################################################################################################
import optparse
parser = optparse.OptionParser()
parser.add_option("-l", "--file", dest="hpo_list",
                  help="Input file hpo list", metavar="FILE")
parser.add_option("-d", "--dictionary_file", dest="dictionary",
                  help="Input file hpo dictionary", metavar="FILE")

(options, args) = parser.parse_args()

###############################################################################################################################################
# 															MAIN
###############################################################################################################################################

dictionary = build_dictionary(options.dictionary)

hpo_list = open(options.hpo_list)

for line in hpo_list:
	line = line.rstrip("\n")

	if line in dictionary:
		print(line, ", ".join(dictionary[line]), sep ="\t")