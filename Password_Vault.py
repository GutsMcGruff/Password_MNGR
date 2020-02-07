#Password Vault
from password_creator import new_pass

web_name = input("Website name:")

user_name = input("Username/email:")

try:
	char_no = int(input("Password length (must be greater than 10):"))

except:
	print("Please enter integer value")

else:
	password= new_pass(char_no)

print("Website:", web_name)
print("Username/Email:", user_name)
print("Password:", password)

login_bundle=[web_name]+ [user_name] + [password]

print(login_bundle)

#f = open("Plain_txt_pass", "a+")

#f.write(login_bundle)



