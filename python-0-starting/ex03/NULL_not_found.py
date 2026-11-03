def NULL_not_found(object: any) -> int:
    null_type = type(object)
    match null_type.__name__:
        case "NoneType":
            print(f"Nothing: {object} {null_type}")
        case "float":
            print(f"Cheese: {object} {null_type}")
        case "int":
            print(f"Zero: {object} {null_type}")
        case "str" if object == "":
            print(f"Empty: {object} {null_type}")
        case "bool":
            print(f"Fake: {object} {null_type}")
        case _:
            print("Type not Found")
            return 1
    return 0
