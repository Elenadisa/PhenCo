#! /usr/bin/env Rscript

#############################################################################################################################################################################
#                                                          METHODS                                                                                                          #
#############################################################################################################################################################################

require(optparse)
require(linkcomm)

#############################################################################################################################################################################
#                                                        OPTPARSE                                                                                                           #
#############################################################################################################################################################################
option_list <- list(
  make_option(c("-i", "--input"), type="character",
              help="Network input file"),
  make_option(c("-n", "--nodes"), type="character",
              help="Nodes file output"),
  make_option(c("-t", "--type"), type="character",
              help="Network type"),
  make_option(c("-s", "--summary", type="character",
              help="graph output name")),
  make_option(c("-d", "--top", type="character",
              help="graph output name")),
  make_option(c("-r", "--relationship", type="character",
              help="graph output name")),
    make_option(c("-c", "--cytoscape", type="character",
              help="cytoscape file output"))

 
)

opt <- parse_args(OptionParser(option_list=option_list))

#############################################################################################################################################################################
#                                                         MAIN                                                                                                               #
#############################################################################################################################################################################

network  <- read.table(opt$input, sep = "\t")
lc <- getLinkCommunities(network, plot=FALSE) #load cluster algorithm

write.table(lc$nodeclusters, opt$nodes, sep ="\t", quote = FALSE, row.names = FALSE, col.names = FALSE) #output file with clusters data

linkcomm2cytoscape(lc,  interaction = "phen-phen", ea = opt$cytoscape) #output file with clusters data for cytoscape visualization

#Summary plots of the cluster analysis
if (opt$type == "more_spec"){
	png(opt$summary)
	plot(lc, type = "summary")
	dev.off()

	png(opt$top)
	plot(lc, type = "members")
	dev.off()

	png(opt$relationship)
	cr <- getClusterRelatedness(lc, hcmethod = "ward")
	dev.off()

} 
