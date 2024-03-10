#need to import for this to work
import sqlite3
import os

#we are going to use this class to perform operations on our databse
class Database:
    
    #create database connection to store it as class attributes
    def __init__(self, reset = False):
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
                 ( CUSTOMER_ID     INTEGER NOT NULL AUTOINCREMENT,
                   CUSTOMER_NAME   VARCHAR(MAX) NOT NULL,
                   CUSTOMER_EMAIL  VARCHAR(MAX) NOT NULL,
                   CUSTOMER_COUNTRY VARCHAR(3) NOT NULL,
                   PRIMARY KEY (CUSTOMER_ID) );""" )
        
        #Orders Table
        self.conn.execute("""CREATE TABLE IF NOT EXISTS Orders 
                 ( ORDER_ID     INTEGER NOT NULL AUTO_INCREMENT,
                   CUSTOMER_ID   INTEGER NOT NULL,
                   PRODUCT_CODE  INTEGER NOT NULL,
                   PRIMARY KEY (ORDER_ID),
                   FOREIGN KEY (CUSTOMER_ID) REFERENCES Customers,
                   FORIEGN KEY (PRODUCT_CODE) REFERENCES Products);""" )
        
        #Products Table
        self.conn.execute("""CREATE TABLE IF NOT EXISTS Products 
                 ( PRODUCT_CODE     INTEGER NOT NULL AUTO_INCREMENT,
                   PRODUCT_NAME   VARCHAR(MAX) NOT NULL,
                   PRIMARY KEY (PRODUCT_CODE) );""" )
        
        
    #inserting tables
    #def insert(self):
        

    #querying data
    #advanced querys and joins
    #data aggregation
    
    #our main for testing sake
    if __name__ == "__main__":
        db = 0