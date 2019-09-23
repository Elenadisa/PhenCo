#! /usr/bin/env Rscript

###################################################################################################################################
#                                            METHODS                                                                              #
###################################################################################################################################

require(optparse)
#optparse is needed to input variables in the console, when the script is running: Disease dictionary, networks and output file


###################################################################################################################################
#                                            OPTPARSE                                                                             #
###################################################################################################################################

option_list <- list(
	make_option(c("-i", "--input"), type="character",
				help="Disease_dictionary"),
	make_option(c("-n", "--network"), type="character",
				help="Netowrk file"),
	make_option(c("-o", "--output"), type="character",
				help="Output file")
)


opt <- parse_args(OptionParser(option_list=option_list))


###################################################################################################################################
#                                            MAIN                                                                            	  #
###################################################################################################################################

#File with the diseases and HPO
dictionary <- read.table(opt$input, stringsAsFactors=FALSE)
#File with the networks
network <- read.table(opt$network, sep="\t", stringsAsFactors=FALSE)

#table -> a data.frame with the HPO pairs and their diseases ids; table1 -> a data.frame with the HPO pairs and their common diseases
table <- data.frame(HPO1 = network$V1, HPO2 = network$V2, ID = character(length(network$V1)), stringsAsFactors=FALSE)
table1 <- data.frame(HPO1 = network$V1, HPO2 = network$V2, Number_common_ids = character(length(network$V1)), stringsAsFactors=FALSE)

for (i in 1:length(table$HPO1)){
	#get the HPO we are looking for
	HPOi <- table$HPO1[i]
	#generarte a vector of the positions of this HPO
	HPO1_index <- which(dictionary$V2 == HPOi)
	#look for the disease ids in the positions we indicate in the previous step
	HPO1_ids <- paste(dictionary$V1[HPO1_index], collapse = ",")
	HPOj <- table$HPO2[i]
	HPO2_index <- which(dictionary$V2 == HPOj)
	HPO2_ids <- paste(dictionary$V1[HPO2_index], collapse = ",")
	
	#Sum of the ids of HPO1 and HPO2
	total_ids <- length(unlist(strsplit(c(HPO1_ids, HPO2_ids), ",")))
	#Unique ids of the previous sum
	unique_ids <- length(unique(unlist(strsplit(c(HPO1_ids, HPO2_ids), ","))))
	#Commom ids between HPO1 and HPO2
	common_ids <- total_ids - unique_ids
	table1$Number_common_ids[i] <- common_ids

	ids <- unique(c(HPO1_ids, HPO2_ids))
	table$ID[i] <- ids
}

write.table(table1, opt$output, sep="\t", quote=FALSE, row.name=FALSE, col.name=FALSE)
