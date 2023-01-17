#input_Validator
def input_validator(input_type):
	def decorator(func):
		def executor(input):
			if type(input) == input_type:
				func(input)
			else:
				print("INVALID Input")
		return executor	
	return decorator

@input_validator(str)
def print_name(name):
	print(f"I'm {name}")

print_name("Balaji") 

# The below line will do the same
# input_validator(str)(print_name)("Balaji")
