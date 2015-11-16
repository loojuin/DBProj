# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 21:53:37 2015

@author: loojuin
"""

import dao

BookIn_Attrs = [
    ("ts", "CHAR(18) PRIMARY KEY"),
    ("name", "VARCHAR(32)")
]

def initDatabase():
    dao.executeSQL("testDB", "init.sql")

def createTable_BookIn():
    dao.createTable("testDB", "BookIn", BookIn_Attrs, True)
    
def createAllTables():
    createTable_BookIn()
    
def selectAllBookIns():
    return dao.select("testDB", "BookIn", "*", "")
    
def selectBookInsByName(name):
    return dao.select("testDB", "BookIn", "*", "WHERE name == '%s'"%name)