#! /usr/bin/env python
 

##############################################################################################################################################
#															METHODS
##############################################################################################################################################

def build_dictionary(filename):
	dictionary = {}
	file = open(filename)
	
	for line in file:
		
		line = line.rstrip("\n")
		fields = line.split("\t")

		HPO = fields[1]
		PMID =fields[3]
		
		if HPO not in dictionary and len(PMID) > 1:
			dictionary[HPO] = [PMID]
			
		elif HPO in dictionary and len(PMID) > 1:
			dictionary[HPO].append(PMID)
			

	return dictionary


##############################################################################################################################################
#															OPTPARSE
##############################################################################################################################################
import optparse

parser = optparse.OptionParser()

parser.add_option("-f", "--comention", dest="comention_data",
                  help="Input file comention", metavar="FILE")

parser.add_option("-n", "--network", dest="network",
                  help="Input network", metavar="FILE")

(options, args) = parser.parse_args()

###############################################################################################################################################
# 															MAIN
###############################################################################################################################################
dictionary = build_dictionary(options.comention_data)
network = open(options.network)
	
#for each line in network file

for line in network:
	line = line.rstrip("\n")
	HPOA, HPOB = line.split("\t")
	

	if HPOA in dictionary :		#Look for PMID of HPO A
		uniq_A_PMID = ",".join(dictionary[HPOA]).split(",")
		uniq_A_PMID = sorted(set(uniq_A_PMID))		#get a set of PMID
	else :
		uniq_A_PMID = []
	
	
	if HPOB in dictionary:		#Look for PMID of HPO A
		uniq_B_PMID = ",".join(dictionary[HPOB]).split(",")
		uniq_B_PMID = sorted(set(uniq_B_PMID))	#get a set of PMID
	else: 
		uniq_B_PMID = []
 
	union_PMID = sorted(set(uniq_A_PMID + uniq_B_PMID))	#Get union PMID of both HPOs

	print(HPOA, HPOB, len(union_PMID), sep="\t")
	



