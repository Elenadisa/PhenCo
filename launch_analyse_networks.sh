#! /usr/bin/env bash

#source ~soft_bio_267/initializes/init_autoflow

current_dir=`pwd`

export CODE_PATH=$(readlink -f $framework_dir )
export PATH=$CODE_PATH'/sys_bio_lab_scripts:'$PATH
export PATH=$CODE_PATH'/scripts/py_scripts:'$PATH
export PATH=$CODE_PATH'/R_cripts/rscripts:'$PATH


#PATH TO build_networks.sh RESULTS
data_source=PATH/TO/OUTPUT/FILES/PhenCo/build_networks
#PATH TO DIRECTORY WITH PAIRS LISTS
networks_source=$data_source"/ln_0000/working_networks"
#PATH TO GENES DATA
term2gene_dictionary=$data_source"/NetAnalyzer.rb_0000/phen2gene"
entrez2gene_symbol=$data_source"/NetAnalyzer.rb_0000/entrez2gene_symbol"
#PATH TO DISEASES-GENE-PHENOTYPE FILE
disease_to_genes_to_phenotypes=$current_dir'/external_data/ALL_SOURCES_FREQUENT_FEATURES_diseases_to_genes_to_phenotypes.txt'
#PATH TO SINGLE ENRICHMENT RESULTS
enrichment_files=$data_source"/ln_0001/enrichments"
#PATH TO SINGLE PHENOTYPE PREVALENCE
hpo_prevalence_file=$current_dir"/results/all_hpo_prevalence"
#PATH TO PATIENT-PHENOTYPE FILE WITHOUT PARENTAL ENRICHMENT
phen2pat_file=$current_dir'/processed_data/patient2hpo_unenriched'
#PATH TO PATIENT-GENE FILE
pat2gene=$data_source"/NetAnalyzer.rb_0000/pat2gene"
#PATH TO HPO DICTIONARY
HPO_table=$current_dir'/processed_data/HPO_without_synonyms'
#PATH TO OMIM DICTIONARY
OMIM_diseases=$current_dir'/processed_data/omim_dictionary'
#PATH TO HPO-PMID FILE
HPO2pubmed_file=$current_dir'/processed_data/HPO2pubmed'


#source ~soft_bio_267/initializes/init_autoflow


ls $networks_source > working_nets

# PATH TO THE DIRECTORY WHERE TO SAVE THE RESULTS
mkdir PATH/TO/OUTPUT/FILES/PhenCo/analyse_networks

#\\$p_values=0.05/0.001/0.00001,

# PREPARE VARIABLES NEEDED IN analyse_networks.af

while read NETWORK
do
	variables=`echo -e "
		\\$working_net=$networks_source/$NETWORK,
		\\$disease_to_genes_to_phenotypes=$disease_to_genes_to_phenotypes,
		\\$term2gene_dictionary=$term2gene_dictionary,
		\\$p_values=0.05,
		\\$single_enrichments=$enrichment_files,
		\\$hpo_prevalence_file=$hpo_prevalence_file,
		\\$phen2pat=$phen2pat_file,
		\\$HPO2pubmed=$HPO2pubmed_file,
		\\$HPO_table=$HPO_table,
		\\$OMIM_diseases=$OMIM_diseases,
		\\$pat2gene=$pat2gene,
		\\$entrez2gene_symbol=$entrez2gene_symbol,
		\\$current_dir=$current_dir

	" | tr -d [:space:]`

	#SLURM system
		#For KEGG and REACTOME ENRICHMENT ANALYSIS	
	
	#AutoFlow -w analyse_networks.af -o PATH/TO/OUTPUT/FILES/PhenCo/analyse_networks/$NETWORK -V $variables $1 -m 8gb -t '7-00:00:00' -n 'cal'
		
		#For GO ENRICHMENT ANALYSIS
	#AutoFlow -w analyse_networks.af -o PATH/TO/OUTPUT/FILES/PhenCo/analyse_networks/$NETWORK -V $variables $1 -m 16gb -t '7-00:00:00' -n 'cal'
	
		#For other analysys
	#AutoFlow -w analyse_networks.af -o PATH/TO/OUTPUT/FILES/PhenCo/analyse_networks/$NETWORK -V $variables $1 -m 2gb -t '7-00:00:00' -n 'cal'
	
	#Linux system
	#AutoFlow -w analyse_networks.af -o PATH/TO/OUTPUT/FILES/PhenCo/analyse_networks/$NETWORK -V $variables $1 -b
	
	
done < working_nets
