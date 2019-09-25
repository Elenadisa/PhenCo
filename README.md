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
``.   
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

### Defining input/output paths. 

User have to define input/output paths in launch scripts:
**I launch_build_networks.sh**. 
*Input*. 
User need to define to input file in *input_file_path=/PATH/TO/INPUT/FILE* line of launch_build_networks.sh. 
Input file must be in XX format.  
*Output*. 
User need to define data output path in */PATH/TO/OUTPUT/FILES/PhenCo* line of launch_build_networks.sh. 
**II launch_analyse_networks.sh**   
*Input*. 
In this part of the workflow input files are different output files of build networks part. Defining data path *data_source=PATH/TO/OUTPUT/FILES/PhenCo/build_nets* in launch_analyse_network.sh all needed files are accesibles.  
*Output*. 
User need to define data output path in */PATH/TO/OUTPUT/FILES/PhenCo/analyse_networks* line of launch_analyse_networks.sh. 
**get_comparative_results.sh**. 
*Input*. 
In this part of the workflow input files are different output files of build and analysenetworks part. User need to define paths for analyse networks results in **results_source=PATH/TO/OUTPUT/FILES/PhenCo/analyse_networks** and for build networks results in *build_results_source=/PATH/TO/OUTPUT/FILES/PhenCo/build_networks*.  
Markdown template to generate html reports are available in reports_template directory.
*Output*
The output of this part of the workflow are different html reports with the results of the workflow.

### Execution

The templetes have to be executed in a certain order.  
**I** ./launch_build_networks.sh. 
**II** ./launch_analyse_networks.sh. 
**III** ./get_comparative_results.sh. 

