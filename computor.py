#!/usr/bin/env python3

import sys
import re

# several examples to try

# "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
# "5 * X^0 + 4 * X^1 = 4 * X^0"
# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

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
def parse_equation_part(part):
	# resulting list of the parts of equation
	result = []
	# split left part of equation by '+'
	part = trim_array(part.split('+'))
	# loop through all the parts of the split by '+' equitaion string
	for elem in part:
		# split the string by '-'
		part_split_by_minus = trim_array(elem.split('-'))
		# loop through the parts of split by '-' equation string
		for split_elem in part_split_by_minus:
			# if the element was not already present in the part list
			# it means that it is a new created token
			# it had a '-' sign in it, we append it and push to array
			if split_elem != "" and split_elem not in part:
				result.append('-' + split_elem)
			# just add this element to array, without chages
			else:
				result.append(split_elem)
	# remove empty string in the array
	result = list(filter(None, result))
	print(result)
	# return the result
	return (result)


# main function that start the whole process
def main(argv):
	
	# check or number of arguments passed to the program
	if len(argv) != 2:
		print("Invalid number of arguments.")
		print("usage: {0} <equation>".format(argv[0]))
		return

	# trim and print the string
	equation = trim_string(argv[1])
	print("Initial equation = |" + equation + "|")

	# split string to define left and right part of the equation
	# and trim its parts and print after all
	# if a '=' is missing, an exception is thrown
	try:
		left_part, right_part = generate_left_right_part(equation)
	except:
		print(r"Ivalid equation: '=' is missing")
		return
	# parse left part of equation
	parse_equation_part(left_part)
	# parse right part of equation
	parse_equation_part(right_part)

	return


# start a main function
if __name__ == "__main__":
	main(sys.argv)

