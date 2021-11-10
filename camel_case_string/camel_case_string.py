
def camel_case_string(string):
	new_string = string.replace('_', ' ')
	new_string = new_string.split(' ')
	for i in (1, len(new_string) -1):
		new_string[i] = new_string[i].capitalize()
	return "".join(new_string)

def screaming_case_string(string):
	new_string = string.replace('_', " ").split(' ')
	screaming_case  = "".join([string.capitalize() for string in new_string])
	return screaming_case


