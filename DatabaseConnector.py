import mysql.connector

def connect():
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='newspaper_analyzer')
    return cnx

def query(cnx, query):
    cursor = cnx.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results
