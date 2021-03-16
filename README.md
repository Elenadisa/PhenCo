# PhenCo Version 1.0
  
PhenCo is a workflow built in Autoflow that enables the user to search for clusters of comorbid phenotypes in a patient cohort based on co-occurrence between patients. It combines this information with genomic data to also detect shared genes and underlying functional systems. 
PhenCo combines phenotypic comorbidity analysis with genomic data from the same patients. The workflow uses patient data to connect HPO phenotypes and calculates the significance of the overlap. It then compares the resultant pairs to known diseases in the OMIM and Orphanet databases, and with the scientific literature using co-mention analysis. 
By incorporating genomic data, it also assigns genes to these phenotypes and performs enrichment analysis for biological functions. Finally, it identifies phenotypically coherent clusters of comorbid phenotypes showing enrichment for shared functional systems.
  
## Requirements

* Python 3. 
* Ruby 2.4.1. 
* R version 3.3.1 or higher. 
* Bioconductor 3.4 or higher. 
* R Markdown. 


### Installation in Linux

**I** Clone this repository. Ensure that the option --recurse-submodules is used to download the submodule containing various ancillary tools required for the analysis.

``
git clone https://github.com/Elenadisa/PhenCo --recurse-submodules
``

**II** Install [Ruby](https://rvm.io/) We recommend using the RVM manager.  

**III** Install the ruby gems [AutoFlow](https://github.com/seoanezonjic/autoflow), [NetAnalyzer](https://github.com/ElenaRojano/NetAnalyzer) and [PETS](https://rubygems.org/gems/pets) the following code:
  
``
gem install autoflow  
``  
``
gem install NetAnalyzer  
``  
``
gem install pets  
``  

**V** Install [Python 3](https://www.python.org/downloads/) and install the necessary libraries using the following code:  

``
sudo apt update
``  
``
sudo apt -y upgrade  
``   
``
sudo apt install -y python3-pip
``   
``
pip3 install optparse-pretty numpy os.path2
``    

**VI** Instal [R](https://cloud.r-project.org/). The following R packages must also be installed:  

Start R in the terminal and install the packages:    

``
sudo -i R  
``   
``
install.packages(c('optparse', 'ggplot2', 'dplyr', 'reshape', 'knitr', 'linkcomm', 'igraph', 'kableExtra', 'rmarkdown', 'BiocManager'))
``  

Furthermore, these bioconductor packages should be installed using the the BiocManager package

``
BiocManager::install(c("clusterProfiler", "ReactomePA", "org.Hs.eg.db", "DOSE", "KEGG.db", "GO.db"))  
`` 

### Input file format 

A confidentially agreements necessary to use the DECIPHER patient data.  
There is a test file with an example of the format that the input file must have (test_input.txt). With this file only the the first two parts of the workflow can be executed.   

## Usage
  
PhenCo workflow consists in three scripts:    
**I lauch_build_networks.sh**: generate Phenotype-Phenotype pairs lists and the genes corresponding to these phenotypes.    
It execute an autoflow template *build_networks.af*.   
**II launch_analayse_network.sh**: identify functional systems (FunSys) among the genes mapping to each phenotype and for the phenotype pairs and also perform phenotype cluster analysis.   
It execute an autoflow template *analyse_network.af*.   
**III get_comparative_results.sh**: generates html reports with workflow results.   


### Defining input/output paths. 

User have to define input/output paths in launch scripts:  

**I launch_build_networks.sh**.   
*Input*.   
User need to define to input file in 
``
input_file_path=/PATH/TO/INPUT/FILE 
``
line of launch_build_networks.sh. 
Input file must be in XX format.  
*Output*.   
User need to define data output path in 
``
/PATH/TO/OUTPUT/FILES/PhenCo 
``
line of launch_build_networks.sh. 

**II launch_analyse_networks.sh**    
*Input*.   
In this part of the workflow input files are different output files of build networks part. Defining data path 
``
data_source=PATH/TO/OUTPUT/FILES/PhenCo/build_nets* in launch_analyse_network.sh
``
 all needed files are accesibles.  
*Output*.   
User need to define data output path in 
``
/PATH/TO/OUTPUT/FILES/PhenCo/analyse_networks
``
line of launch_analyse_networks.sh. 

**III get_comparative_results.sh**.   
*Input*.   
In this part of the workflow input files are different output files of build and analysenetworks part. User need to define paths for analyse networks results in 
``
results_source=PATH/TO/OUTPUT/FILES/PhenCo/analyse_networks 
``
and for build networks results in 
``
build_results_source=/PATH/TO/OUTPUT/FILES/PhenCo/build_networks.  
``
Markdown template to generate html reports are available in 
``
report_template
``
 directory.  
*Output*.   
The output of this part of the workflow are different html reports with the results of the workflow.

### Execution

The templetes have to be executed in a certain order.    
**I** ./launch_build_networks.sh.   
**II** ./launch_analyse_networks.sh.   
**III** ./get_comparative_results.sh.   

### Run Autoflow  
  
PhenCo can be executed in a SLURM queue system and in linux systems. Use the autoflow code line that suits you.

## Citation

Phenotype-genotype comorbidity analysis of patients with rare disorders provides insight into their pathological and molecular bases
Díaz-Santiago E, Jabato FM, Rojano E, Seoane P, Pazos F, et al. (2020) Phenotype-genotype comorbidity analysis of patients with rare disorders provides insight into their pathological and molecular bases. PLOS Genetics 16(10): e1009054. https://doi.org/10.1371/journal.pgen.1009054
