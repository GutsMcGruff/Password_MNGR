#Password Creator

def new_pass(no_chars):
	import string
	import random
	
	if no_chars < 10:
		return('Must contain more than 10 characters')

	char_import = string.ascii_letters + string.digits + string.punctuation
	
	pass_chars = random.choices(char_import, k = no_chars)
	
	password = ""
	for l in pass_chars:
		password += l
	
	return password