#! /usr/bin/env bash

source ~soft_bio_267/initializes/init_autoflow

current_dir=`pwd`

data_source=/mnt/scratch/users/bio_267_uma/elenads/PhenCo/build_nets

networks_source=$data_source"/ln_0000/working_networks"
term2gene_dictionary=$data_source"/NetAnalyzer.rb_0000/phen2gene"
entrez2gene_symbol=$data_source"/NetAnalyzer.rb_0000/entrez2gene_symbol"

disease_to_genes_to_phenotypes=$current_dir'/external_data/ALL_SOURCES_FREQUENT_FEATURES_diseases_to_genes_to_phenotypes.txt'
enrichment_files=$data_source"/ln_0001/enrichments"
hpo_prevalence_file=$data_source"/shuf_0000/all_hpo_prevalence"

phen2pat_file=$current_dir'/processed_data/patient2hpo_unenriched'

pat2gene=$data_source"/NetAnalyzer.rb_0000/pat2gene"

HPO_table=$current_dir'/processed_data/HPO_without_synonyms'

OMIM_diseases=$current_dir'/processed_data/omim_dictionary'


HPO2pubmed_file=$current_dir'/processed_data/HPO2pubmed'


source ~soft_bio_267/initializes/init_autoflow


ls $networks_source > working_nets

## PATH TO THE DIRECTORY WHERE TO SAVE THE RESULTS
mkdir $SCRATCH'/PhenCo/analyse_networks'

#\\$p_values=0.05/0.001/0.00001,

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

	#For KEGG and REACTOME ENRICHMENT ANALYSIS	
	#AutoFlow -w analyse_networks.af -o $SCRATCH'/PhenCo/analyse_networks/'$NETWORK -V $variables $1 -m 8gb -t '7-00:00:00' -n 'cal'
	
	#For GO ENRICHMENT ANALYSIS
	#AutoFlow -w analyse_networks.af -o $SCRATCH'/PhenCo/analyse_networks/'$NETWORK -V $variables $1 -m 16gb -t '7-00:00:00' -n 'cal'
	
	#AutoFlow -w analyse_networks.af -o $SCRATCH'/PhenCo/analyse_networks/'$NETWORK -V $variables $1 -m 2gb -t '7-00:00:00' -n 'cal'
	
	
done < working_nets
