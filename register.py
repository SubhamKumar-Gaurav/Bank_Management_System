# User registration - SignIn/SignUp 

from database import * 
import random
def SignUp() :
    username=input("Create Username: ") 
    temp=db_query(f"SELECT username FROM customers where username = '{username}';") 
    if temp :
        print("Username Already Exists") 
        SignUp()
    else :
        print("Username is Available Please Proceed")  
        password=input("Enter Your Password ") 
        name = input("Enter Your Name: ") 
        age=input("Enter Your age: ") 
        city=input("Enter your city: ")
        while True :
            account_number=random.randint(10000000,99999999)   
            temp=db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")  
            if temp:
                continue 
            else :
                print(account_number)
                break 
