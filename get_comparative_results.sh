#! /usr/bin/env bash
#SBATCH --cpu=1
#SBATCH --mem=4gb
#SBATCH --time=1-00:00:00
#SBATCH --error=job.%J.err
#SBATCH --output=job.%J.out

module load ruby/2.4.1
module load python/anaconda-3_440
source ~soft_bio_267/initializes/init_R

results_source=PATH/TO/OUTPUT/FILES/PhenCo/analyse_networks

build_results_source=/PATH/TO/OUTPUT/FILES/PhenCo/build_networks

framework_dir=`dirname $0`
export CODE_PATH=$(readlink -f $framework_dir )
export PATH=$CODE_PATH'/sys_bio_lab_scripts:'$PATH
export PATH=$CODE_PATH'/scripts/py_scripts:'$PATH
export PATH=$CODE_PATH'/scripts/R_scripts:'$PATH

mkdir results
cat processed_data/build_metrics $build_result_source/build_metrics > results/build_metrics
cp $build_results_source"/NetAnalyzer.rb_0001/phen2phen_net"  results/phen2phen_net
cp $build_results_source"/shuf_0000/all_hpo_prevalence" results/all_hpo_prevalence

cat $results_source/*/metrics > results/all_metrics
create_metric_table.rb results/all_metrics 'Name,Type' results/table_metrics.txt

cp $results_source/more_spec/metrics results/more-spec_metrics
patient=$results_source"/more_spec/patient_cluster_merger.py_0001/patient_hpo_genes_go_0.05"
go=$result_source"/more_spec/patient_cluster_merger.py_0001/patient_coincidence_with_clusters_and_gene_systems_go_0.05"
kegg=$result_source"/more_spec/patient_cluster_merger.py_0001/patient_coincidence_with_clusters_and_gene_systems_kegg_0.05"
reactome=$result_source"/more_spec/patient_cluster_merger.py_0001/patient_coincidence_with_clusters_and_gene_systems_reactome_0.05"
pat2gene=$build_results_source"/NetAnalyzer.rb_0000/pat2gene_symbol"
pat2gene_l=$build_results_source"/NetAnalyzer.rb_0000/pat2gene_symbol_l"

get_patient_hpo_in_clusters.py -p $patient -A 0 -a 1 -g $go -r $reactome -k $kegg -B 0 -b 2 -D 5 -f $pat2gene -C 0 -c 1 -o results/patient_overlap_summary > results/patient_hpo_coincident_with_clusters
echo -e "more_spec\tmore_spec\tpatient_overlap_summary\t`pwd`/results/patient_overlap_summary" >> results/more-spec_metrics
echo -e "more_spec\tmore_spec\tpatient_hpo_coincident_with_clusters\t`pwd`/results/patient_hpo_coincident_with_clusters" >> results/more-spec_metrics
create_metric_table.rb results/more-spec_metrics 'Name,Type' results/more-spec_table_metrics.txt

#Cluster summary figures
mkdir results/clusters_summary_figures
cp $results_source"/more_spec/clustering.R_0000/summary_dendograme_kegg_0.05.png" results/clusters_summary_figures/summary_dendograme_kegg_0.05.png
cp $results_source"/more_spec/clustering.R_0000/top_connected_nodes_kegg_0.05.png" results/clusters_summary_figures/top_connected_nodes_kegg_0.05.png
cp $results_source"/more_spec/clustering.R_0000/relationship_between_communities_kegg_0.05.png" results/clusters_summary_figures/relationship_between_communities_kegg_0.05.png
cp $results_source"/more_spec/clustering.R_0002/summary_dendograme_reactome_0.05.png" results/clusters_summary_figures/summary_dendograme_reactome_0.05.png
cp $results_source"/more_spec/clustering.R_0002/top_connected_nodes_reactome_0.05.png" results/clusters_summary_figures/top_connected_nodes_reactome_0.05.png
cp $results_source"/more_spec/clustering.R_0002/relationship_between_communities_reactome_0.05.png" results/clusters_summary_figures/relationship_between_communities_reactome_0.05.png
cp $results_source"/more_spec/clustering.R_0001/summary_dendograme_go_0.05.png" results/clusters_summary_figures/summary_dendograme_go_0.05.png
cp $results_source"/more_spec/clustering.R_0001/top_connected_nodes_go_0.05.png" results/clusters_summary_figures/top_connected_nodes_go_0.05.png
cp $results_source"/more_spec/clustering.R_0001/relationship_between_communities_go_0.05.png" results/clusters_summary_figures/relationship_between_communities_go_0.05.png

#Create Report
create_report.R -t report_templates/pairs_report_template.Rmd -o results/S1_Report_pairs_report.html -d results/table_metrics.txt -H t
create_report.R -t report_templates/clustering_report_template.Rmd -o results/S2_Report_clustering_report.html -d results/table_metrics.txt -H t

create_report.R -t report_templates/cluster_details_go_template.Rmd -o results/S3_Report_cluster_details_go.html -d results/more-spec_table_metrics.txt -H t
create_report.R -t report_templates/cluster_details_reactome_template.Rmd -o results/S4_Report_cluster_details_reactome.html -d results/more-spec_table_metrics.txt -H t
create_report.R -t report_templates/cluster_details_kegg_template.Rmd -o results/S5_Report_cluster_details_kegg.html -d results/more-spec_table_metrics.txt -H t

create_report.R -t report_templates/patient_details_template.Rmd -o results/S6_Report_patient_details.html -d results/more-spec_table_metrics.txt -H t

create_report.R -t report_templates/article_figures.Rmd -o results/S7_Report_Article_Figures.html -d results/table_metrics.txt -H t

