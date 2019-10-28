#! /usr/bin/env bash

#Initialize autoflow
source ~soft_bio_267/initializes/init_autoflow
current_dir=`pwd`

module load python/anaconda-3_440

framework_dir=`dirname $0`
export CODE_PATH=$(readlink -f $framework_dir )
export PATH=$CODE_PATH'/sys_bio_lab_scripts:'$PATH
export PATH=$CODE_PATH'/scripts/py_scripts:'$PATH

#DOWNLOAD EXTERNAL FILES 

mkdir external_data

wget 'ftp://ftp.ncbi.nih.gov/genomes/Homo_sapiens/GRCh37.p13_interim_annotation/interim_GRCh37.p13_top_level_2017-01-13.gff3.gz' -O external_data/genome.gz
gunzip -d  external_data/genome.gz
wget 'http://compbio.charite.de/jenkins/job/hpo.annotations.monthly/lastSuccessfulBuild/artifact/annotation/ALL_SOURCES_ALL_FREQUENCIES_phenotype_to_genes.txt' -O external_data/hpo_db.txt
tail -n +2 external_data/hpo_db.txt | cut -f 1,3 > external_data/hpo_db_phen2gene.txt  
wget http://compbio.charite.de/jenkins/job/hpo.annotations/lastStableBuild/artifact/misc/phenotype_annotation.tab -O external_data/phenotype_annotation.tab
wget -O external_data/hp.obo http://purl.obolibrary.org/obo/hp.obo --no-check-certificate

curl http://compbio.charite.de/jenkins/job/hpo.annotations.monthly/lastStableBuild/artifact/annotation/ALL_SOURCES_FREQUENT_FEATURES_diseases_to_genes_to_phenotypes.txt > external_data/ALL_SOURCES_FREQUENT_FEATURES_diseases_to_genes_to_phenotypes.txt
curl https://data.omim.org/downloads/B8yyAwLuSOyA5G3vHOIfIg/mimTitles.txt > external_data/mimTitles.txt 
cut -f 2,3 external_data/mimTitles.txt | sed -e '/^#/d' > processed_data/omim_dictionary




mkdir processed_data

# THE INPUT
# Each record in the input file should represent a different mutation per patient, and should consist of the following (separated by tabs:) patient id, chromosome, genomic position start, genomic position end, list of HPO phenotypes.

# Here we include code to parse an input file from DECIPHER and obtain the correct input file for the  workflow
input_file_path=/PATH/TO/INPUT/FILE
echo -e  "Total_of_patients\t`cut -f 1 $decipher_file_path | sort -u | wc -l ` " > processed_data/build_metrics
echo -e "HP:0000001\nHP:0000118" > processed_data/list_of_hpo_to_exclude.txt
# Convert DECIPHER format to our processing format
 #[1] : Patient [2]: Chr [3]: Start [4]: End [5]: HPO_Name/Code
awk 'BEGIN { FS = "\t" } {if ($9 != "" && $6 ~ /De novo/ ) { print $1 "\t" $2 "\t" $3 "\t" $4 "\t" $9}}' $decipher_file_path  > processed_data/patient_data.txt

# Create HPOs dictionary
parse_hpo_file.rb external_data/hp.obo > processed_data/hpo2name.txt
get_table_ontology.rb external_data/hp.obo name,synonym | cut -f 1,2  > processed_data/HPO_table.txt 

source ~soft_bio_267/initializes/init_pets

# About parental enrichment
#	-r 'none' => no enrichment, -r 'root' => enrichment
node_character='A'
get_network_nodes.rb -p external_data/hp.obo -e processed_data/list_of_hpo_to_exclude.txt -i processed_data/patient_data.txt -m $node_character -o processed_data/tripartite_network_unenriched.txt -c processed_data/cluster_coords_unenriched.txt -r 'none'
get_network_nodes.rb -p external_data/hp.obo -e processed_data/list_of_hpo_to_exclude.txt -i processed_data/patient_data.txt -m $node_character -o processed_data/tripartite_network_enriched.txt -c processed_data/cluster_coords_enriched.txt -r 'root'

# Pat-Phen pairs for Phen-Phen generation
grep "HP:" processed_data/tripartite_network_unenriched.txt | awk '{print $2 "\t" $1}' > processed_data/patient2hpo_unenriched
# Now either with no cut-off
#cp processed_data/temp processed_data/patient2hpo_unenriched
# Or minimum 2 patients have an HPO
# awk 'FNR==NR{a[$2]++;next} a[$2]>1'  temp temp > processed_data/patient2hpo_unenriched
#rm temp

# Pat-Phen pairs for other parts - enriched and with no cut-off
grep "HP:" processed_data/tripartite_network_enriched.txt | awk '{print $2 "\t" $1}' > processed_data/patient2hpo_enriched

# Network for Phen-SOR generation - enriched and with cut-off
NUMBER=1
conn_filter=2 # At least two patients must validate the tuple <Hpo,Pheno>
merge_pairs.rb -i processed_data/tripartite_network_enriched.txt -k 'HP:' -o "processed_data/fr_" -n $NUMBER -m $conn_filter
cut -f 1,2 processed_data/fr_1.txt | sort -u > processed_data/net.txt
cut -f 2,3 processed_data/fr_1.txt | sort -u >> processed_data/net.txt 


cut -f 2 processed_data/patient2hpo_unenriched | sort -u > processed_data/HPO_list
create_hpo_dictionary.py -l processed_data/HPO_list -d external_data/hp.obo > processed_data/HPO_without_synonyms

# Filter the HPO table with relevant HPOs that are in the processed patient to HPO data
cut -f 2  processed_data/patient2hpo_unenriched | sort -u  > processed_data/relevant_HPOs
grep -Fwf processed_data/relevant_HPOs processed_data/HPO_table.txt > processed_data/filtered_HPO_table.txt

#Calculate single HPO prevalence in DECIPHER patients
mkdir results
calculate_prevalence_hpo.py -f $patient2hpo_unenriched  -t 0 > results/all_hpo_prevalence

#COMENTION ANALYSIS

module unload libyaml
module unload openssl
module purge
module load ruby/2.4.1
rm processed.temp processed_data/HPO2pubmed processed_data/failed_queries
pubmedIdRetriever.rb processed_data/filtered_HPO_table.txt >> processed_data/HPO2pubmed 2> processed_data/failed_queries
module purge


source ~soft_bio_267/initializes/init_autoflow


#PATH TO THE DIRECTORY WHERE TO SAVE THE RESULTS
mkdir /PATH/TO/OUTPUT/FILES/PhenCo
mkdir /PATH/TO/OUTPUT/FILES/PhenCo/build_networks

# PREPARE VARIABLES NEEDED IN build_networks.af

#\\$p_values=0.05/0.001/0.00001

variables=`echo -e "
	\\$patients_file=$current_dir'/processed_data/patient_data.txt',
	\\$hpo_dict=$current_dir'/processed_data/hpo2name.txt',
	\\$genome_annotation=$current_dir'/external_data/genome',
	\\$number_of_random_models=50,
	\\$association_thresold=2,
	\\$association_low_thresold=2,
	\\$metric_type=hypergeometric,
	\\$p_values=0.05,
	\\$patient2hpo_unenriched=$current_dir'/processed_data/patient2hpo_unenriched',
	\\$patient2hpo_enriched=$current_dir'/processed_data/patient2hpo_enriched',
	\\$hpo_obo=$current_dir'/external_data/hp.obo',
	\\$current_dir=$current_dir,
	\\$net=$current_dir'/processed_data/net.txt', 
	\\$cluster_coords_enriched=$current_dir'/processed_data/cluster_coords_enriched.txt',
	\\$fr_1=$current_dir'/processed_data/fr_1.txt',

" | tr -d [:space:]`


#AutoFlow -w build_networks.af -o PATH/TO/OUTPUT/FILES/PhenCo/build_nets -V $variables -m 2gb $1 -n cal -t '10:00:00'

#For enrichment analysis
#AutoFlow -w build_networks.af -o PATH/TO/OUTPUT/FILES/PhenCo/build_nets -V $variables -m 16gb $1 -n cal -t '10:00:00'



