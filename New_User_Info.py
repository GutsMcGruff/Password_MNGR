#New site login creation tool
def new_info(user_name, destination, password, salt):
    from password_creator import new_pass
    from PasswordVal import PWVal
    import json
    import SPBE
    from cryptography.fernet import Fernet
    
    web_name = input("Website name: ")
    
    ex_user_name = input("Username/email: ")
    
    pass_option = input("Would you like to auto create password? 1. Yes  2. No: ")
    
    if pass_option == "1":
    	try:
    		char_no = int(input("Password length (must be greater than 10):"))
    	except:
    		print("Please enter integer value")
    	else:
    		ex_password = new_pass(char_no)
    		
    elif pass_option == "2":
    	rep = False
    	while rep == False:
    		ex_password = input("Enter password:")
    		rep = PWVal(ex_password) 
    
    else:
    	print("Please specify 1. Yes or 2. No")
        
    #ex_pass_bits = ex_password.encode() #converts to bits ready for encryption
    key = SPBE.key_gen(password, salt)
    s = Fernet(key)
    ex_pass_crypt = s.encrypt(ex_password.encode()).decode() #Encrypts and converts bits to string

    with open(destination, 'r') as f:
        user_vault_data = json.load(f)
    try:#exception handeling for the case where new user is storing passwords
        user_vault_data[user_name][web_name] = [ex_user_name, ex_pass_crypt] #[ex_user_name, site_password]
    except:
        user_vault_data[user_name] = {web_name: [ex_user_name, ex_pass_crypt]} #[ex_user_name, site_password]}
        
    with open(destination, 'w') as f:
        json.dump(user_vault_data, f)
    
    del user_vault_data, ex_password, web_name, ex_user_name
