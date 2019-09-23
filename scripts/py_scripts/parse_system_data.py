#! /usr/bin/env python

########################################################################################################################################
#														METHODS
########################################################################################################################################

def load_pairs_files(filename, key_col_number, value_col_number):
	dictionary = {}
	file = open(filename)
	
	for line in file:
		line = line.rstrip("\n")
		
		fields = line.split("\t")

		key = fields[key_col_number]
		values = fields[value_col_number].split("/")
		
		if key not in dictionary:
			dictionary[key] = []
			for value in values:
				dictionary[key].append(value)
		else:
			for value in values:
				if value not in dictionary[key]:
					dictionary[key].append(value)

	return dictionary





########################################################################################################################################
#														OPTPARSE
########################################################################################################################################
import optparse

parser=optparse.OptionParser()

parser.add_option("-s", "--single_enrichment_file", dest="single_enrichment_file", 
                  help="single_enrichment_file", metavar="FILE")
parser.add_option("-A", "--key_single", dest="key_single", 
				  help="key_single", type='int')
parser.add_option("-a", "--value single", dest="value_single", 
                  help="value_single", type='int')
parser.add_option("-p", "--pair_enrichment_file", dest="pair_enrichment_file", 
                  help="pair_enrichment_file", metavar="FILE")
parser.add_option("-B", "--key_pair", dest="key_pair", 
				  help="key_pair", type='int')
parser.add_option("-b", "--value pair", dest="value_pair", 
                  help="value_pair", type='int')
parser.add_option("-g", "--gene_symbo_file", dest="gene_symbol_file", 
                  help="pair_enrichment_file", metavar="FILE")
parser.add_option("-C", "--key_gene", dest="key_gene", 
				  help="key_gene", type='int')
parser.add_option("-c", "--value gene", dest="value_gene", 
                  help="value_gene", type='int')
parser.add_option("-e", "--enrichment_type", dest="enrichment_type", 
                  help="enrichment_type", type='str')
parser.add_option("-t", "--analysis_type", dest="analysis_type", 
                  help="analysis_type", type='str')

(options, arg) = parser.parse_args()

#######################################################################################################################################
#														MAIN
#######################################################################################################################################
single_enrichment_dict = load_pairs_files(options.single_enrichment_file, options.key_single, options.value_single) #enrichment dictionary of single hpos
pair_enrichment_dict = load_pairs_files(options.pair_enrichment_file, options.key_pair, options.value_pair)	#enrichment dictionary of hpo pairs
gene_symbol_dict = load_pairs_files(options.gene_symbol_file, options.key_gene, options.value_gene)	#gene-symbol dictionary

keys_in_single = list(single_enrichment_dict.keys()) #get the systems of the single_enrichment_dictionary
keys_in_pairs = list(pair_enrichment_dict.keys())	#get the systems of the pair_enrichment_dictionary

#if we want to parse genes
if options.analysis_type == "genes" :

	#for each system in single_enrichment_dictionary 
	for key in keys_in_single:

		if key in pair_enrichment_dict:		#If the system is in pair_enrichment dictionary
			if key != "ID":
				values = set(single_enrichment_dict[key] + pair_enrichment_dict[key])	#Get the common genes for the systems in single_enrichment and in pair_enrichment
				
				for value in values:
					
					if options.enrichment_type != "kegg":	#If enrichment is != to kegg print the system and gene in a line
						print(key, value, sep="\t")
					
					else:									#If enrichment is == to kegg, translate the gene entrez_id to gene symbol and print the system and gene in a line
						if value in gene_symbol_dict:
							print(key, "".join(gene_symbol_dict[value]), sep ="\t")
		

		else:								#If the system is in single_enrichment but not in pair_enrichment_dictionary
			
			values = single_enrichment_dict[key]	#get the genes for the system
			
			for value in values:

				if options.enrichment_type != "kegg": #If enrichment is != to kegg print the system and gene in a line
					print(key, value, sep="\t")

				else:
					if value in gene_symbol_dict:		#If enrichment is == to kegg, translate the gene entrez_id to gene symbol and print the system and gene in a line
						print(key, "".join(gene_symbol_dict[value]), sep ="\t")

	#for each system in pair_enrichment_dictionary 
	for key in keys_in_pairs:	

		if key not in single_enrichment_dict:			#If the system isn't in single_enrichment
			values = pair_enrichment_dict[key]			#get the genes for the system
			
			for value in values:
				
				if options.enrichment_type != "kegg":	#If enrichment is != to kegg print the system and gene in a line
					print(key, value, sep="\t")
				
				else:									#If enrichment is == to kegg, translate the gene entrez_id to gene symbol and print the system and gene in a line
					
					if value in gene_symbol_dict:
						print(key, "".join(gene_symbol_dict[value]), sep ="\t")


#if we want to parse names
else:

	#for each system in single_enrichment_dictionary 
	for key in keys_in_single:
		
		if key in pair_enrichment_dict:			#if system is in single_enrichment dictionary and in pair_enrichment dictionary
			
			if key != "ID":						
				value = set(single_enrichment_dict[key] + pair_enrichment_dict[key])		#get the name of the system and print system and name in a line
				print(key, "".join(value), sep="\t")
					
		else:									#if system is in single_enrichment dictionary but not in pair_enrichment dictionary

			value = single_enrichment_dict[key]		#get the name of the system and print system and name in a line
			print(key, "".join(value), sep="\t")
				

	#for each system in pair_enrichment_dictionary 
	for key in keys_in_pairs:
		
		if key not in single_enrichment_dict:			#if system not in single_enrichment dictionary
			
			value = pair_enrichment_dict[key]			#get the name of the system and print system and name in a line
			print(key, "".join(value), sep="\t")
				