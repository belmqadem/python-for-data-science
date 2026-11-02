from sys import exit, argv


try:
	arg_len = len(argv)
	if arg_len < 2:
		exit(0)
	elif arg_len > 2:
		raise AssertionError("more than one argument is provided")
	try:
		number = int(argv[1])
	except ValueError as ve:
		raise AssertionError("argument is not an integer")
	if (number % 2 == 0):
		print("I'm Even.")
	else:
		print("I'm Odd.")
except AssertionError as ae:
	print(f"AssertionError: {ae}")
