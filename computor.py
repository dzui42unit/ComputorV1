#!/usr/bin/env python3

import sys
from collections import Counter
from parser import trim_string, trim_array, generate_left_right_part, parse_equation_part_into_tokens, create_tokens, sort_dict_by_keys

# several examples to try

# "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
# "5 * X^0 + 4 * X^1 = 4 * X^0"
# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"


# function that will create reduced form and prints it
def create_reduced_form(left_part, right_part):
	
	reduced_form = {}
	for key_l, value_l in left_part.items():
		if key_l in right_part.keys():
			reduced_form[key_l] = left_part[key_l] + (-1.0 * right_part[key_l])
		else:
			reduced_form[key_l] = left_part[key_l]
	return (reduced_form)

# function to print a reduced form
def print_reduced_form(reduced_form):
	reduced_string = "Reduced form: "
	i = 0
	for key, val in reduced_form.items():
		reduced_string += str(str(val) + " * X^" + str(key))
		if (val < 0.0):
			reduced_string += str(" - " + str(val * -1.0))
		if (val >= 0.0):
			if i != 0:
				reduced_string += " + "
			reduced_string +=  str(val)
		reduced_string += (" * X^" + str(key) + " ")
		i += 1
	print(reduced_string)


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
		# create left and right parts of equation
		left_part, right_part = generate_left_right_part(equation)
	except:
		raise BaseException("Ivalid equation: '=' is missing.")
	# parse left and right part of equation
	# first argument is part of equation, second is change argument or not
	left_part = parse_equation_part_into_tokens(left_part)
	right_part = parse_equation_part_into_tokens(right_part)
	print(left_part)
	# create tokens from both parts
	left_part = create_tokens(left_part)
	right_part = create_tokens(right_part)
	print(left_part)
	print(right_part)
	# creating of a reduced form
	reduced_form = create_reduced_form(left_part, right_part)
	print(reduced_form)
	# print reduced form
	print_reduced_form(reduced_form)


# start a main function
if __name__ == "__main__":
	try:
		main(sys.argv)
	except BaseException as e:
		print(str(e))


