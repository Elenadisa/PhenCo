#! /usr/bin/env python

##############################################################################################################################################
#															METHODS
##############################################################################################################################################
import functions as fn

##############################################################################################################################################
#															OPTPARSE
##############################################################################################################################################
import optparse

parser=optparse.OptionParser()

parser.add_option("-p", "--pat2loci", dest="pat2loci_file", 
                  help="pat2loci_file", metavar="FILE")
parser.add_option("-A", "--key pat id", dest="pat_id", 
                  help="pat_id", type='int')
parser.add_option("-a", "-- loci value", dest="pat_loci_value", 
                  help="pat_loci_value", type='int')


parser.add_option("-l", "--loci2phen file", dest="loci2phen_file", 
				  help="loci2phen file", metavar="FILE")
parser.add_option("-B", "--key loci id", dest="loci_id", 
                  help="loci id", type='int')
parser.add_option("-b", "--gene value", dest="gene_value", 
                  help="column of genes", type='int')


(options, arg) = parser.parse_args()

##############################################################################################################################################
#															MAIN
##############################################################################################################################################
pat2loci_dictionary = fn.build_dictionary(options.pat2loci_file, options.pat_id, options.pat_loci_value)
loci2gene_dictionary = fn.build_dictionary(options.loci2phen_file, options.loci_id, options.gene_value)

#for each patient associated to a number of locis
for patient, locis in pat2loci_dictionary.items():
	
	for loci in locis:		#for each loci associated to a patient
		
		if loci in loci2gene_dictionary:	#get the genes for each loci
			genes = loci2gene_dictionary[loci]
			
			for gene in genes:
				
				print(patient, gene, sep ="\t") #print genes related to the patient
