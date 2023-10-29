# necessary imports
import secrets
import string


# define the alphabet
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation


alphabet = lowercase_letters + uppercase_letters + digits + special_chars


# fix password length
pwd_length=int(input("Enter length of password required : "))


choice=input("\nWant to set any constraints? (YES/NO) : ")
if choice=='NO':
    # generating password
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    print(pwd)
elif choice=="YES":
    # setting constraints
    print("\nEnter number of -")  
    ucl_n=int(input("uppercase letters : "))
    lcl_n=int(input("lowercase letters : "))
    dig_n=int(input("digits : "))
    splchr_n=int(input("special chars : "))
    # generating password
    if ucl_n+lcl_n+dig_n+splchr_n==pwd_length:
        while True:
            pwd=''
            for i in range(pwd_length):
                pwd+=''.join(secrets.choice(alphabet))


            # checking if generated password matches the constraints
            if (sum(char in special_chars for char in pwd)==splchr_n)and(sum(char in digits for char in pwd)==dig_n)and(sum(char in lowercase_letters for char in pwd)==lcl_n)and(sum(char in uppercase_letters for char in pwd)==ucl_n):
                break
        print("\n"+pwd)
    else:
        print("\nrequired password length and constraints don't match up")




