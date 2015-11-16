# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 21:53:26 2015

@author: loojuin
"""

from django.conf import settings
import sqlite3

def dbPath(dbname):
    return settings.DATABASES[dbname]['NAME']
    
def executeSQL(dbname, filepath):
    appender = ""
    for line in open(filepath, "r"):
        appender += line + " "
    queries = appender.split(";")
    results = []
    con = sqlite3.connect(dbPath(dbname))
    cur = con.cursor()
    for q in queries:
        res = cur.execute(q)
        retval = []
        for row in res:
            retval.append(row)
        results.append(retval)
    cur.close()
    con.commit()
    con.close()
    return results
    
def createTable(dbname, tablename, attrAndTypes, ifnotexists):
    query = "CREATE TABLE %s%s ("%("IF NOT EXISTS " if ifnotexists else "", tablename)
    attrs = []
    for attr in attrAndTypes:
        attrs.append(attr[0] + " " + attr[1])
    query += ", ".join(attrs) + ")"
    con = sqlite3.connect(dbPath(dbname))
    cur = con.cursor()
    cur.execute(query)
    cur.close()
    con.commit()
    con.close()
    
def dropTable(dbname, tablename, ifexists):
    query = "DROP TABLE %s%s"%("IF EXISTS " if ifexists else "", tablename)
    con = sqlite3.connect(dbPath(dbname))
    cur = con.cursor()
    cur.execute(query)
    cur.close()
    con.commit()
    con.close()
    
def select(dbname, tablename, columns, params):
    wherequery = "" if (len(params) == 0 or params == None) else " %s"%params
    query = "SELECT %s FROM %s%s"%(columns, tablename, wherequery)
    con = sqlite3.connect(dbPath(dbname))
    cur = con.cursor()
    res = cur.execute(query)
    retval = []
    for row in res:
        retval.append(row)
    cur.close()
    con.close()
    return retval
    