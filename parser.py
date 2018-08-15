import re


# a function that performs sorting of the dictionary by keys
def sort_dict_by_keys(dict_to_sort, rev):
	return (dict(sorted(dict_to_sort.items(), reverse=rev)))


# function that trims a string
def trim_string(string):
	return ' '.join(string.split())


#trim all strings in the array of them
def trim_array(arr):
	result = []
	for elem in arr:
		result.append(trim_string(elem))
	return (result)


# function that returns left and right part of the equation
# performs a split by '='
# return type is 'tuple'
def generate_left_right_part(equation):
	left_part, right_part = equation.split('=') 
	left_part = trim_string(left_part)
	right_part = trim_string(right_part)
	return left_part, right_part


# function that will split the equation part
# and returns tj list of elements that represent { sign, number, and X^n}
def parse_equation_part_into_tokens(part):
	# resulting list of the parts of equation
	result = []
	# split left part of equation by '+'
	part = trim_array(part.split('+'))

	i = 0
	while i < len(part):
		part[i] = '+'+ part[i]
		i += 1
	print(part)
	# loop through all the parts of the split by '+' equitaion string
	for elem in part:
		# split the string by '-'
		part_split_by_minus = trim_array(elem.split('-'))
		# loop through the parts of split by '-' equation string
		print(part_split_by_minus)
		for split_elem in part_split_by_minus:
			# if the element was not already present in the part list
			# it means that it is a new created token
			# it had a '-' sign in it, we append it and push to array
			# if split_elem not in part:
			if split_elem[0] != '+':
				result.append('-' + split_elem)
			# just add this element to array, without chages
			else:
				result.append(split_elem)
	# remove empty string in the array
	result = list(filter(None, result))
	#create a dictionary from the equation parts
	create_tokens(result)
	# return the result
	return (result)


# function that creates a dictionary from the tokens
def create_tokens(equation_parts):
	# creating an empty dict of the final values
	result = {}
	# go though all parts of equation and check if they are valid or not
	for part in equation_parts:
		# match this pattern
		if re.match(r"(\s)?([-]|[+])(\s)?([0-9]([.][0-9])?)+(\s)?[*](\s)?([X][\^][0-9]+)(\s)?", part):
			# parse the token and extract number near X^N and and power of X
			# split into two parts (1) - number (2) - X^N
			number_and_x = trim_array(part.split('*'))
			# storing a number and converting it into float from string
			number = float(number_and_x[0])
			# extract the power
			power = int(trim_array(number_and_x[1].split('^'))[1])
			# if the X with this power was already present in equation
			# update the value near it
			if power in result.keys():
				result[power] += number
			# else just add a new key to the dict
			else:
				result.update({power: number})
		# if does not match -> throw an exception
		else:
			raise BaseException("Ivalid equation: \"{}\" token has errors in it.".format(part))
	# sort dict by keys in descending order
	sort_dict_by_keys(result, True)
	return (result)
