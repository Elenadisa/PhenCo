#! /usr/bin/env python
##############################################################################################################################################
#															METHODS
##############################################################################################################################################
def add_pair(hpo_a, hpo_b, dictionary):
	
	if hpo_a not in dictionary:
		dictionary[hpo_a] = [hpo_b]
	
	else:
		dictionary[hpo_a].append(hpo_b)

def load_connected_hpo(filename):
	filename = open(filename)
	connected_HPO = {}
	
	for line in filename:
		line = line.rstrip("\n")
		fields = line.split("\t")
		
		add_pair(fields[0], fields[1], connected_HPO)
		add_pair(fields[1], fields[0], connected_HPO)
	
	return connected_HPO

def exist_pair(hpo_a, hpo_b, dictionary):
	exist = True
	
	if hpo_a not in dictionary or ( hpo_a in dictionary and hpo_b not in dictionary[hpo_a]):
		exist = False
	
	return exist

def get_all_hpo(filename):
	filename = open(filename)
	all_HPO = []
	
	for line in filename:
		line = line.rstrip("\n")
		fields = line.split("\t")
	
		if fields[1] not in all_HPO:
			all_HPO.append(fields[1])
	
	return all_HPO

##############################################################################################################################################
#															OPTPARSE
##############################################################################################################################################
import optparse

parser = optparse.OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="Input file DECIPHER network", metavar="FILE")
parser.add_option("-n", "--network", dest="network",
                  help="NetAnaliyzer network", metavar="FILE")

(options, args) = parser.parse_args()

###############################################################################################################################################
# 															MAIN
###############################################################################################################################################
connected_HPO = load_connected_hpo(options.network) #dictionary with HPO as keys and all posibles pairs as values (in sense and antisense way)
all_HPO = get_all_hpo(options.filename)	#get all HPOs associated to patients

#Non connected HPO
while len(all_HPO) > 1:			#While there are hpos in the list
	hpo_a = all_HPO.pop(0)		#we pick the first hpo in the list
	
	for hpo_b in all_HPO:		#we compare the first hpo with the rest of hpo in the list
		
		if exist_pair(hpo_a, hpo_b, connected_HPO) == False and exist_pair(hpo_b, hpo_a, connected_HPO) == False: # If the first hpo is not in the dictionary or both hpo aren't in the values in the dictionary
			print(hpo_a, hpo_b,  sep = "\t")	#hpo_a and hpo_n are non connected