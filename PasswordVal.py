def PWVal(password):
	import string
	error = False

	if not any(x.isupper() for x in password):
		print("Must contain at least 1 capital letter.")
		error = True
			    
	if not any(x.isdigit() for x in password):
		print("Must contain at least 1 digit")
		error = True
	if len(password) < 8:
	    print("Must be at least 8 chars.")
	    
	if " " in password:
		print("May not contain spaces.")
		error = True

	if not any(x in string.punctuation for x in password):
		print("needs special char")
		error = True
	
	if error == False:
		print("Valid Password")
		return True
	else:
		return False

