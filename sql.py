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
    
    #updating a value
    def update_data(self):
        cursor = self.conn.cursor()
        query = "UPDATE Customers SET CUSTOMER_COUNTRY = (?) WHERE CUSTOMER_ID = (?)" 
        params = ("USA", 1)
        cursor.execute(query,params)
        cursor.execute("COMMIT")
        
    #querying data
    #select, where, >=,
    def query_data(self):
         cursor = self.conn.cursor()
         
         #basic select
        #  query = "SELECT * FROM Customers"
        #  toPrint = cursor.execute(query).fetchall()
        #  print(toPrint)
         
         #select specific column
        #  query = "SELECT PRODUCT_NAME FROM Products"
        #  toPrint = cursor.execute(query).fetchall()
        #  print(toPrint)
         
         #select with a where clause
        #  query = "SELECT * FROM Customers WHERE CUSTOMER_ID >= (?) and CUSTOMER_COUNTRY = (?)"
        #  params = (1,"CAN")
        #  toPrint = cursor.execute(query,params).fetchall()
        #  print(toPrint)
         
         #select with order by
         query = "SELECT * FROM Customers ORDER BY CUSTOMER_ID DESC"
         toPrint = cursor.execute(query).fetchall()
         print(toPrint)
    
    #advanced querys and joins
    def advanced_query(self):
        cursor = self.conn.cursor()
        
        #query that joins orders, products, and customers into one table on their common ID
        query = "SELECT Orders.ORDER_ID, Products.PRODUCT_CODE, Products.PRODUCT_NAME, Customers.CUSTOMER_NAME, Customers.CUSTOMER_EMAIL FROM Orders INNER JOIN Customers ON Customers.CUSTOMER_ID = Orders.CUSTOMER_ID INNER JOIN Products ON Orders.PRODUCT_CODE = Products.PRODUCT_CODE"
        toPrint = cursor.execute(query).fetchall()
        print(toPrint)
    
    #data aggregation
    
    #our main for testing sake
if __name__ == "__main__":
    db = Database() 
    
    #creating tables
    db.create_tables()
    
    #inserting customers
    db.insert_customer("Maya Saltzman", "mayasaltzman3@gmail.com", "CAN")
    db.insert_customer("Poppy Shepherd", "poppy_awesome_dawg@gmail.com", "CAN")
    db.insert_customer("Andrea Luis Gaudet", "aluisgau@gmail.com", "USA")
    
    #inserting products
    db.insert_product("Dyson Vaccum")
    db.insert_product("Dyson Hair Dryer")
    
    #inserting an order
    db.insert_orders(1,1)
    db.insert_orders(3,1)
    db.insert_orders(2,2)
    db.insert_orders(2,1)
    
    
    #updating data in Customers
    #db.update_data()
    
    #db.query_data()
    
    db.advanced_query()
    
    