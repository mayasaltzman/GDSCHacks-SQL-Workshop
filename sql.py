#need to import for this to work
import sqlite3
import os

#we are going to use this class to perform operations on our database
class Database:
    
    #create database connection to store it as class attributes
    def __init__(self, reset = True):
        #if database already exists remove it
        if (reset == True):
            if os.path.exists('orders.db'):
                os.remove('orders.db')  
                
        #creates database connection to the database we are going to work with
        self.conn = sqlite3.connect('orders.db')
    
    #creating tables
    def create_tables(self):
        #Customers Table
        self.conn.execute("""CREATE TABLE IF NOT EXISTS Customers 
                 ( CUSTOMER_ID     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                   CUSTOMER_NAME   VARCHAR NOT NULL,
                   CUSTOMER_EMAIL  VARCHAR NOT NULL,
                   CUSTOMER_COUNTRY VARCHAR(3) NOT NULL );""" )
        
        #Products Table
        self.conn.execute("""CREATE TABLE IF NOT EXISTS Products 
                 ( PRODUCT_CODE     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                   PRODUCT_NAME   VARCHAR NOT NULL );""" )
        
        #Orders Table
        self.conn.execute("""CREATE TABLE IF NOT EXISTS Orders 
                 ( ORDER_ID     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                   CUSTOMER_ID   INTEGER NOT NULL,
                   PRODUCT_CODE  INTEGER NOT NULL,
                   FOREIGN KEY (CUSTOMER_ID) REFERENCES Customers,
                   FOREIGN KEY (PRODUCT_CODE) REFERENCES Products);""" )
        
        
        
    #inserting into customer table
    def insert_customer(self, name, email, country):
        cursor = self.conn.cursor()
        query = "INSERT INTO Customers (CUSTOMER_NAME,CUSTOMER_EMAIL,CUSTOMER_COUNTRY) VALUES (?,?,?)"
        params = (name, email, country)
        cursor.execute(query,params)
        cursor.execute("COMMIT")
        
    
    #insert into products table
    def insert_product(self, name):
        cursor = self.conn.cursor()
        query = "INSERT INTO Products (PRODUCT_NAME) VALUES (?)"
        params = (name,)
        cursor.execute(query,params)
        cursor.execute("COMMIT")
    
    #insert into orders table
    def insert_orders(self, customer_id, product_code):
        cursor = self.conn.cursor()
        query = "INSERT INTO Orders (CUSTOMER_ID, PRODUCT_CODE) VALUES (?,?)"
        params = (customer_id,product_code)
        cursor.execute(query,params)
        cursor.execute("COMMIT")
        
    
    #querying data
    #select, where, >=, 
    
    #advanced querys and joins
    
    #data aggregation
    
    #our main for testing sake
if __name__ == "__main__":
    db = Database() 
    
    #creating tables
    db.create_tables()
    
    #inserting customers
    db.insert_customer("Maya Saltzman", "mayasaltzman3@gmail.com", "CAN")
    db.insert_customer("Poppy Shepherd", "poppy_awesome_dawg@gmail.com", "CAN")
    
    #inserting products
    db.insert_product("Dyson Vaccum")
    
    db.insert_orders(1,1)