# DataBase Management 

import mysql.connector as sql 

mydb = sql.connect(
        host="localhost" ,
        user="root" ,
        passwd="localhost.2244202@sql" , 
        database="bank"
) 


cursor = mydb.cursor() 

def create_customer_table() :
        cursor.execute('''
               CREATE TABLE IF NOT EXISTS customers 
             ( username VARCHAR(20),
               password VARCHAR(20), 
               name varchar(20), 
               age INTEGER, 
               city VARCHAR(20), 
               account_number INTEGER, 
               status BOOLEAN       )
''')
        
mydb.commit() 

if __name__=="main" : 
        create_customer_table() 