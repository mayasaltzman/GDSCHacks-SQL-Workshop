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
        
    #inserting tables
    #def insert(self):
        

    #querying data
    #advanced querys and joins
    #data aggregation