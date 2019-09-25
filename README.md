# PhenCo Version 1.0

PhenCo is a workflow built in autoflow. This workflow analyse comorbidity relations of phenotype from patients of a cohort:  
**I** Building networks: get the phenotype pairs lists from a cohort of patients.  
**II** Analyzing networks: analyse the pairs list and clustering analysis.  
**III** Get results: obtain graphs and tables with results.  

## Requeriments

* Python 3. 
* R version 3.3.1 or higher. 
* Bioconductor 3.4 or higher. 
* Markdown.
* Ruby 2.4.1. 

### Instalation

**I** Clone this repository.  
``
git clone https://github.com/Elenadisa/PhenCo
``.   
**II** Install [ruby](https://www.ruby-lang.org/en/downloads/).  
**III** Install [AutoFlow](https://github.com/seoanezonjic/autoflow).   
**IV** Install [NetAnalyzer](https://github.com/ElenaRojano/NetAnalyzer).   
**V** Install [Python 3](https://www.python.org/downloads/) and import librarys: optparse, numpy, os.path.  
**VI** Instal [R](https://cloud.r-project.org/) and the following R packages:  
``
install.packages(c('optparse', 'ggplot2', 'dplyr', 'reshape', 'knitr', 'linkcomm', 'igraph', 'kableExtra'))   
``
  
``
BiocManager::install(c("clusterProfiler", "ReactomePA", "org.Hs.eg.db")).  
`` 
   
## Defining PATHS. 

**I** In launch_build_networks.sh introduce the path to the input data.  
**II** In launch_build_networks.sh introduce the path to the directory where to save the results.  


## Usage

## Execution

The templetes have to be executed in a certain order.  
**I** ./launch_build_networks.sh. 
**II** ./launch_analyse_networks.sh. 
**III** ./get_comparative_results.sh. 

