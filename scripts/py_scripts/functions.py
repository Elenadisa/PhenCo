



def build_dictionary(filename, key_col_number, value_col_number):
	dictionary = {}
	file = open(filename)
	
	for line in file:
		line = line.rstrip("\n")
		fields = line.split("\t")
		key = fields[key_col_number]
		value = fields[value_col_number]

		if key not in dictionary:
			dictionary[key] = [value]
		else :
			dictionary[key].append(value)

	return dictionary