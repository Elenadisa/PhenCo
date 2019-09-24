#! /usr/bin/env bash
#SBATCH --cpu=1
#SBATCH --mem=4gb
#SBATCH --time=1-00:00:00
#SBATCH --error=job.%J.err
#SBATCH --output=job.%J.out

module load ruby/2.4.1
module load python/anaconda-3_440
source ~soft_bio_267/initializes/init_R

results_source=/mnt/scratch/users/bio_267_uma/elenads/test1/analysed_unenriched_networks

build_results_source=/mnt/scratch/users/bio_267_uma/elenads/test1/build_uneriched_nets

PATH=/mnt/home/users/bio_267_uma/elenads/projects/comorbidity_def_test/scripts/rscripts:$PATH
PATH=/mnt/home/users/bio_267_uma/elenads/projects/comorbidity_def_test/scripts/py_scripts:$PATH
export PATH

mkdir results
cat processed_data/build_metrics $build_result_source/build_metrics > results/build_metrics
cp $build_results_source"/NetAnalyzer.rb_0001/phen2phen_net"  results/phen2phen_net

cat $results_source/*/metrics > results/all_metrics
create_metric_table.rb results/all_metrics_renamed 'Name,Type' results/table_metrics.txt

cp $results_source/more_spec/metrics results/more-spec_metrics
create_metric_table.rb results/more-spec_metrics 'Name,Type' results/more-spec_table_metrics.txt

#Create Report
create_report.R -t report_templates/article_figures.Rmd -o results/Article_Figures.html -d results/table_metrics.txt -H t

create_report.R -t report_templates/pairs_report_template.Rmd -o results/pairs_report.html -d results/table_metrics.txt -H t
create_report.R -t report_templates/clustering_report_template.Rmd -o results/clustering_report.html -d results/table_metrics.txt -H t

create_report.R -t report_templates/cluster_details_go_template.Rmd -o results/cluster_details_go.html -d results/more-spec_table_metrics.txt -H t
create_report.R -t report_templates/cluster_details_kegg_template.Rmd -o results/cluster_details_kegg.html -d results/more-spec_table_metrics.txt -H t
create_report.R -t report_templates/cluster_details_reactome_template.Rmd -o results/cluster_details_reactome.html -d results/more-spec_table_metrics.txt -H t

create_report.R -t report_templates/patient_details_template.Rmd -o results/patient_details.html -d results/more-spec_table_metrics.txt -H t


