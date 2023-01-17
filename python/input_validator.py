#input_Validator
def input_validator(*input_types):
    def decorator(func):
        def executor(*inputs):
            if len(input_types) != len(inputs):
                print("ERROR - Check decorator/function params")
                return
            for iterator in range(0, len(inputs)):
                if type(inputs[iterator]) != input_types[iterator]:
                    print("INVALID Input")
                    return
            func(*inputs)
        return executor
    return decorator

@input_validator(str)
def print_name(name):
	print(f"I'm {name}")

print_name("Balaji") 

# The below line will do the same
# input_validator(str)(print_name)("Balaji")
