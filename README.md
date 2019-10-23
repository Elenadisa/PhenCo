# PhenCo Version 1.0
  
PhenCo is a workflow built in Autoflow that enables to analyse phenotypic comorbidity of patients cohorts. Rare diseases can have complex phenotypes and be hard to diagnose. Genetic and molecular analysis is made difficult by the small numbers of affected patients. Phenotypic comorbidity analysis can help rectify this by combining information from patients with similar phenotypes and looking for overlap in terms of shared genes and underlying functional systems. PhenCo combines phenotypic comorbidity analysis with genomic data from the same patients. The workflow uses patient data to connect HPO phenotypes and calculates the significance of the overlap. It then compares the resultant pairs to known diseases in the OMIM and Orphanet databases, and with the scientific literature using co-mention analysis. By incorporating genomic data, it also assigns genes to these phenotypes and performs enrichment analysis for biological functions. Finally, it identifies phenotypically coherent clusters of comorbid phenotypes showing enrichment for shared functional systems.
  
## Requirements

* Python 3. 
* Ruby 2.4.1. 
* R version 3.3.1 or higher. 
* Bioconductor 3.4 or higher. 
* R Markdown. 


### Installation in Linux

**I** Clone this repository. Ensure that the option --recurse-submodules is used to download the submodule

``
git clone https://github.com/Elenadisa/PhenCo --recurse-submodules
``

**II** Install [Ruby](https://rvm.io/) We recommend to use the RVM manager.  

**III** Install [AutoFlow](https://github.com/seoanezonjic/autoflow) and [NetAnalyzer](https://github.com/ElenaRojano/NetAnalyzer) using the following code:

``
gem install Autoflow
gem install NetAnalyzer
gem install PETS
``

**V** Install [Python 3](https://www.python.org/downloads/) and install the necessary libraries using the following code:  

``
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   
``.   
``
python3 get-pip.py   
``.   
``
pip3 install optparse-pretty numpy os.path2
``    

**VI** Instal [R](https://cloud.r-project.org/). The following R packages must also be installed:  

``
install.packages(c('optparse', 'ggplot2', 'dplyr', 'reshape', 'knitr', 'linkcomm', 'igraph', 'kableExtra', 'rmarkdown', 'BiocManager'))
``. 

Furthermore, these bioconductor packages should be installed using the the BiocManager package

``
BiocManager::install(c("clusterProfiler", "ReactomePA", "org.Hs.eg.db", "DOSE"))  
`` 

## Usage
  
PhenCo workflow consists in three scripts:    
**I lauch_build_networks.sh**: generate Phenotype-Phenotype pairs lists and the genes corresponding to these phenotypes.    
It execute an autoflow template *build_networks.af*.   
**I launch_analayse_network.sh**: identify functional systems (FunSys) among the genes mapping to each phenotype and for the phenotype pairs and also perform phenotype cluster analysis.   
It execute an autoflow template *analyse_network.af*.   
**II get_comparative_results.sh**: generates html reports with workflow results.   


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


## Citation
