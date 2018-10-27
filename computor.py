#!/usr/bin/env python3

import sys
from math import sqrt
from collections import Counter
from parser import trim_string, trim_array, generate_left_right_part, parse_equation_part_into_tokens, create_tokens, sort_dict_by_keys

# function that will create reduced form and prints it
def create_reduced_form(left_part, right_part):
	
	reduced_form = {}
	reduced_form_without_zero_coefs = {}
	for key_l, value_l in left_part.items():
		if key_l in right_part.keys():
			reduced_form[key_l] = left_part[key_l] + (-1.0 * right_part[key_l])
		else:
			reduced_form[key_l] = left_part[key_l]
	for key, value in reduced_form.items():
		if value != 0.0:
			reduced_form_without_zero_coefs[key] = value
	return (reduced_form_without_zero_coefs)

# function to print a reduced form
def print_reduced_form(reduced_form):
	reduced_string = "Reduced form: "
	i = 0
	for key, val in reduced_form.items():
		if (val < 0.0):
			reduced_string += str(" - " + str(val * -1.0))
		if (val >= 0.0):
			if i != 0:
				reduced_string += " + "
			reduced_string +=  str(val)
		reduced_string += (" * X^" + str(key) + " ")
		i += 1
	reduced_string += "= 0"
	print(trim_string(reduced_string))


# function gets a key and if it is present returns a value by it
def check_key(reduced_form, key):
	if key not in reduced_form.keys():
		return (0.0)
	return reduced_form[key]

# function that performs computing
def compute(reduced_form):
	# find the degree of polynom and print it
	polynom_degree =max(reduced_form.keys())
	print("Polynomial degree: {}".format(polynom_degree))
	# if a degree is greater than 2 -> raise an exception
	if polynom_degree > 2:
		raise BaseException("The polynomial degree is stricly greater than 2, I can't solve.")
	if polynom_degree == 2:
		# assign a, b, c
		a = check_key(reduced_form, 2)
		b = check_key(reduced_form, 1)
		c = check_key(reduced_form, 0)
		# find discriminant
		d = b * b - 4 * a * c
		# if it is positive -> find solutions
		if d > 0.0:
			print("Discriminant is strictly positive, the two solutions are:")
			x1 = (-1.0 * b - sqrt(d)) / (2 * a)
			x2 = (-1.0 * b + sqrt(d)) / (2 * a)
			print("%.6f" % x1)
			print("%.6f" % x2)
		if d == 0.0:
			print("Discriminant is strictly zero, the one solution is:")
			x = (-1.0 * b) / (2 * a)
			print(x)
		if d < 0.0:
			print("Discriminant is strictly negative, the two solutions are:")
			d = d * -1.0;
			x1 = (-1.0 * b - sqrt(d)) / (2 * a)
			x2 = (-1.0 * b + sqrt(d)) / (2 * a)
			print("{0:0.6f} + {1:0.6f} * i".format(x1, x2))
			print("{0:0.6f} - {1:0.6f} * i".format(x1, x2))
			pass
	if polynom_degree == 1:
		b = check_key(reduced_form, 1)
		c = check_key(reduced_form, 0)
		print("The solution is:")
		x = (-1.0 * c) / b
		print(x)
	if polynom_degree == 0:
		print("There is no solution")


# main function that start the whole process
def main(argv):
	
	# check or number of arguments passed to the program
	if len(argv) != 2:
		print("Invalid number of arguments.")
		print("usage: {0} <equation>".format(argv[0]))
		return

	# trim string
	equation = trim_string(argv[1])
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
	# create tokens from both parts
	left_part = create_tokens(left_part)
	right_part = create_tokens(right_part)
	# creating of a reduced form
	reduced_form = create_reduced_form(left_part, right_part)
	# print reduced form
	if len(reduced_form.keys()) == 0:
		print('All the real numbers are solution')
		return 
	print_reduced_form(reduced_form)
	# compute the equation
	compute(reduced_form)


# start a main function
if __name__ == "__main__":
	try:
		main(sys.argv)
	except BaseException as e:
		print(str(e))


