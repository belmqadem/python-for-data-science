def all_thing_is_obj(object: any) -> int:
	obj_type = type(object)
	match obj_type.__name__:
		case "tuple":
			print(f"Tuple : {obj_type}")
		case "list":
			print(f"List : {obj_type}")
		case "set":
			print(f"Set : {obj_type}")
		case "dict":
			print(f"Dict : {obj_type}")
		case "str":
			print(f"{object} is in the kitchen : {obj_type}")
		case _:
			print("Type not found")
	return 42
