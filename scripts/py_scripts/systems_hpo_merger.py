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

parser.add_option("-c", "--cluster_file", dest="cluster_file", 
                  help="clustering.R output", metavar="FILE")
parser.add_option("-s", "--system file", dest="system_file", 
				  help="cluster system file", metavar="FILE")
parser.add_option("-A", "--key_hpo_id", dest="cluster_hpo_id", 
                  help="column which have clusters identificators", type='int')
parser.add_option("-B", "--key_system_id", dest="cluster_system_id", 
                  help="column which have clusters identificators", type='int')
parser.add_option("-x", "--hpo", dest="hpo", 
                  help="column with HPO terms", type='int')
parser.add_option("-y", "--system", dest="system", 
                  help="column with system terms", type='int')

(options, arg) = parser.parse_args()

#######################################################################################################################################
#														MAIN
#######################################################################################################################################
hpo_dictionary = fn.build_dictionary(options.cluster_file, options.cluster_hpo_id, options.hpo)
systems_dictionary = fn.build_dictionary(options.system_file, options.cluster_system_id, options.system)


for cluster_id, systems in systems_dictionary.items():
	
	if cluster_id in hpo_dictionary:
		all_systems = systems[:]
		first_system = all_systems.pop(-1)
		
		print(first_system, ','.join(hpo_dictionary[cluster_id]), sep="\t")
		
		while len(all_systems) > 0:
			second_system = all_systems.pop(-1)
			
			print(second_system, ','.join(hpo_dictionary[cluster_id]), sep="\t")





