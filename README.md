# PhenCo

PhenCo consists of a workflow with two templates, built in autoflow. This workflow analyse comorbidity relations of phenotype from patients of a cohort: 
I. Building networks: get the phenotype pairs lists from a cohort of patients.
II. Analyzing networks: analyse the pairs list and clustering analysis.
III. Get results: obtain graphs and tables with results.

## Software Instalation

To use PhenCo it is needed to follow the next requirements:
I. Clone this repository. Code:
II. Install ruby.
III. Install AutoFlow. Code: gem install autoflow
IV Install NetAnalyser: https://github.com/ElenaRojano/NetAnalyzer
VI. Install python 3 and import librarys: optparse, numpy, os.path

V. Instal R and the following R packages: install.packages(c('optparse', 'ggplot2', 'dplyr', 'reshape', 'knitr', 'linkcomm', 'igraph')) and BiocManager::install(c("clusterProfiler", "ReactomePA", "org.Hs.eg.db"))

## Defining PATHS
I. In launch_build_networks.sh introduce the path to the input data.
II. In launch_build_networks.sh introduce the path to the directory where to save the results.


## Usage

## Execution

The templetes have to be executed in a certain order. 
I. ./launch_build_nets.sh
II. ./launch_analyse_networks.sh
III. ./get_comparative_results.sh