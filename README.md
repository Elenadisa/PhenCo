# PhenCo Version 1.0


## Requeriments

* Python 3. 
* Ruby 2.4.1. 
* R version 3.3.1 or higher. 
* Bioconductor 3.4 or higher. 
* R Markdown. 


### Instalation

**I** Clone this repository:
``
git clone https://github.com/Elenadisa/PhenCo
``   
**II** Install [Ruby](https://rvm.io/) We recommend to use the RVM manager.  
**III** Install [AutoFlow](https://github.com/seoanezonjic/autoflow).   
**IV** Install [NetAnalyzer](https://github.com/ElenaRojano/NetAnalyzer).   
**V** Install [Python 3](https://www.python.org/downloads/) and install the following librarys:  
``
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   
``  
``
python3 get-pip.py   
``. 
``
pip3 install optparse-pretty numpy os.path2
``  
**VI** Instal [R](https://cloud.r-project.org/) and the following R packages:  
``
install.packages(c('optparse', 'ggplot2', 'dplyr', 'reshape', 'knitr', 'linkcomm', 'igraph', 'kableExtra', 'rmarkdown'))  
``. 
``
BiocManager::install(c("clusterProfiler", "ReactomePA", "org.Hs.eg.db", "DOSE"))  
`` 

## Usage

### Defining PATHS. 

**I** In launch_build_networks.sh introduce the path to the input data.  
**II** In launch_build_networks.sh introduce the path to the directory where to save the results.  

### Execution

The templetes have to be executed in a certain order.  
**I** ./launch_build_networks.sh. 
**II** ./launch_analyse_networks.sh. 
**III** ./get_comparative_results.sh. 

