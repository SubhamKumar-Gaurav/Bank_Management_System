# User registration - SignIn/SignUp 

from database import * 

def SignUp() :
    username=input("Create Username: ") 
    temp=db_query(f"SELECT username FROM customers where username = '{username}';") 
    print(temp) 

SignUp() 