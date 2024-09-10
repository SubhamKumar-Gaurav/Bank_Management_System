from register import *

print("Welcome to Subham Bank, Paisa hi Paisa hai mere paas !!")

while True :
    try :
        register = int(input("1. SignUp\n" 
                             "2. SignIn"))
        
        if register==1 or register==2 :
            if register==1 : 
                SignUp() 
        else :
            print("Please Enter Valid Input From Options")
    except ValueError :
        print("Invalid Input. Try Again With Numbers")     