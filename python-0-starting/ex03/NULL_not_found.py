def NULL_not_found(object: any) -> int:
	null_type = type(object)
	if object is None:
		print(f"Nothing: {object} {null_type}")
	elif null_type is float:
		print(f"Cheese: {object} {null_type}")
	elif null_type is int:
		print(f"Zero: {object} {null_type}")
	elif null_type is str and object == "":
		print(f"Empty: {object} {null_type}")
	elif null_type is bool:
		print(f"Fake: {object} {null_type}")
	else:
		print("Type not Found")
		return 1
	return 0