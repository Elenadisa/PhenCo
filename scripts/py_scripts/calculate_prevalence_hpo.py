#! /usr/bin/env python
##############################################################################################################################################
#															METHODS
##############################################################################################################################################
def count_patients_and_calculate_prevalence_hpo(filename): 
	filename = open(filename)
	patients = []
	hpo_patients ={}
	
	for line in filename:
		line = line.rstrip("\n")
		fields = line.split("\t")
		
		if fields[0] not in patients:
			patients.append(fields[0])
		
		hpo = fields[1]
		patient = fields[0]
		
		if hpo not in hpo_patients:
			hpo_patients[hpo] = [patient]
		
		else:
			hpo_patients[hpo].append(patient)
	
	number_patients = len(patients)
	
	return number_patients, hpo_patients

##############################################################################################################################################
#															OPTPARSE
##############################################################################################################################################
import optparse

parser = optparse.OptionParser()
parser.add_option("-f", "--file", dest="phen2pat",
                  help="Input file DECIPHER network", metavar="FILE")
parser.add_option("-t", "--threshold", dest="threshold",
                  help="Frecuency threshold", type='float')

(options, args) = parser.parse_args()

###############################################################################################################################################
# 															MAIN
###############################################################################################################################################
number_patients, hpo_patients = count_patients_and_calculate_prevalence_hpo(options.phen2pat)	# return the number of patient and the hpo-patient/disease dictionary

#For every hpo in the dictionary count the number of items for the key and calculate the percentage of patients/diseases that have this hpo -> prevalence
for hpo in hpo_patients:
	hpo_prevalence= len(hpo_patients[hpo])/number_patients*100
	
	if hpo_prevalence > options.threshold:		#if the prevalence is greater than a certain threshold it print the pair hpo-prevalence
		print(hpo, hpo_prevalence, sep="\t")