#Login/Login Creation
from PasswordVal import PWVal
import Salt_Shaker
import json
import hashlib
import sys


#Fetch user login info
with open('UserData.json', 'r') as f:
    user_data = json.load(f)
with open('SaltData.json', 'r') as f:
    salt_data = json.load(f)

Login = False
#Login or Create User
while True:
    if Login == True:
        break
    else:
        log_option = input("1. Login 2. Login Creation (enter b to exit):")
        if log_option == 'b':
            sys.exit('Goodbye')
        elif log_option == "1": #Log in
            while True:
                user_name = input('Username (enter b to return to menu):')
                if user_name == 'b':
                    break
                elif user_name in user_data:
                    password = input('Password:')
                    #Compares hashed passwords 
                    if (hashlib.md5((password+(salt_data[user_name])).encode())).hexdigest() == user_data[user_name]:
                        Login = True
                        print('Login Sucessful')
                        del log_option
                        break
                    else:
                        print('Username/password mismatch')
                else: print('Username/password mismatch')
          
        elif log_option == "2": #Create user
            while True:
                new_user = input("New username (enter b to return to menu):")
                print(new_user)
                if new_user == 'b':
                    break
                elif len(new_user) < 4:
                    print('Username too short (must be > 4 characters)')
                elif new_user in user_data:
                    print("Username already taken")
                else:
                    while True:  #New user password validation
                        new_pass1 = input("New password:")
                        new_pass2 = input("Retype password:")
                        if new_pass1 == new_pass2:
                            pw_test = PWVal(new_pass1)
                            if pw_test == True: #Encrypt new user password
                                new_salt = Salt_Shaker.salt(10)
                                crypt_pass = (hashlib.md5((new_pass1+new_salt).encode())).hexdigest()
                                del new_pass1
                                del new_pass2
                                user_data[new_user] = crypt_pass #Write new user to database
                                with open('UserData.json', 'w+') as f:
                                    json.dump(user_data, f)
                                salt_data[new_user] = new_salt
                                with open('SaltData.json', 'w') as f:
                                    json.dump(salt_data, f)
                                print('New user created')
                                del log_option
                                break
#%%
from New_User_Info import new_info
from cryptography.fernet import Fernet
import SPBE
                            
print('Password Vault')
with open('Password_Vault.json', 'r') as f:
    vault_data = json.load(f)
option_1 = None
while True:
    if option_1 == 'b':
            break
    while True:
        option_1 = input('1. View passwords 2.Add a new password (press b to exit): ')
        if option_1 == 'b':
            break
        elif option_1 == '1': #Prints stored profiles and asks user which password they want to access
            try:
                print('Stored profiles: \n')
                for x in vault_data[user_name].keys():
                    print(x)
            except:
                print('No password data stored yet')
                break
            
            while True:   
                profile_option = input('Type the name of the profile you wish to access (b to return): ')
                if profile_option == 'b':
                    break
                elif profile_option in vault_data[user_name]: #Decrypts the profile password and prints the stored profile
                    key = SPBE.key_gen(password, salt_data[user_name])
                    s = Fernet(key)
                    ex_pass_crypt = vault_data[user_name][profile_option][1]
                    ex_pass = s.decrypt(ex_pass_crypt.encode()).decode()
                    print(vault_data[user_name][profile_option][0],'-', ex_pass)
                    del ex_pass
                
                else:
                    print('Please choose from options')
                
        elif option_1 == '2': #calls New_User_Info.new_info to add a new profile
            new_info(user_name, 'Password_Vault.json', password, salt_data[user_name])
        with open('Password_Vault.json', 'r') as f:
            vault_data = json.load(f)
    else:
        print('Please choose from options')
        
del password, user_data, salt_data, vault_data, Login, option_1
    
    