



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


	
	def build_list(filename, col, tab, duplicate):
	l = list()
	file = open(filename)
	
	for line in file:
		line = line.rstrip("\n")
		fields = line.split(tab)
		element = fields[col]

		if duplicate == False:
			if element not in l:
				l.append(element)
		else:
			l.append(element)

	return(l)



def load_list_from_a_file(filename):
	l = list()
	file = open(filename)
	for line in file:
		line = line.rstrip("\n")
		l.append(line)

	return(l)