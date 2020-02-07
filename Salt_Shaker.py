#Salt Shaker

def salt(length):
	import string
	import random

	char_import = string.ascii_letters + string.digits + string.punctuation
	
	salt_chars = random.choices(char_import, k = length)
	
	salt = ""
	for l in salt_chars:
		salt += l
	
	return salt