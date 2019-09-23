#! /usr/bin/env Rscript

#############################################################################################################################################################################
#																METHODS 																									#
#############################################################################################################################################################################

require(optparse)
require(igraph)


# Prepare input commands
#############################################################################################################################################################################
#																OPTPARSE 																									#
#############################################################################################################################################################################
option_list <- list(
  make_option(c("-i", "--input"), type="character",
              help="Network input file"),
  make_option(c("-o", "--output"), type="character",
              help="output file")
)

opt <- parse_args(OptionParser(option_list=option_list))



#############################################################################################################################################################################
#																MAIN 																										#
#############################################################################################################################################################################


#Input network
datos  <- read.table(opt$input, sep = "\t") 
#Convert to a graph object
g <- graph.data.frame(datos, directed = FALSE)

#Topological parameters
cat(paste('Clustering coef', transitivity(g), sep="\t"), "\n")
cat(paste('Connected Component', components(g)$no, sep="\t"), "\n")
cat(paste('Diameter', diameter(g), sep="\t"), "\n")
cat(paste('Radious', radius(g), sep="\t"), "\n")
cat(paste('Network centralization', centr_degree(g)$centralization, sep="\t"), "\n")
cat(paste('Average minimum path', average.path.length(g), sep="\t"), "\n")
cat(paste('Number of nodes', gorder(g), sep="\t"), "\n")
cat(paste('Network Density', edge_density(g), sep="\t"), "\n")

#HPO frequecy table
write.table(table(degree(g)), opt$output, sep="\t", row.names = FALSE, col.names=c("Connections", "Number of HPOs"), quote = FALSE)
#scale free
#deg.dist.fyi <- degree.distribution(g)
#plot(deg.dist.fyi, xlab="k", ylab="P(k)", main="Scale-free network")
