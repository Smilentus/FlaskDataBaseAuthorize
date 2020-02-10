import sqlite3
import hashlib

def connectToDatabase():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    return conn, cursor

def closeConnection(conn):
    conn.close()

def createTable(tableName):
    conn, cursor = connectToDatabase()
    
    query = "CREATE TABLE {} (ID INTEGER PRIMARY KEY, login TEXT, password TEXT)".format(tableName)
    cursor.execute(query)

    conn.commit()
    closeConnection(conn)

def getAllUsersFromTable(tableName):
    conn, cursor = connectToDatabase()

    query = "SELECT * FROM {}".format(tableName)
    cursor.execute(query)

    data = cursor.fetchall()
    print(data)

    conn.commit()
    closeConnection(conn)    

    return data

def getUserDataFromTable(tableName, user):
    conn, cursor = connectToDatabase()

    query = "SELECT * FROM {} WHERE login = '{}'".format(tableName, user)
    cursor.execute(query)

    data = cursor.fetchall()
    print(data)

    conn.commit()
    closeConnection(conn)    

    return data

def isUserExists(user):
    data = getUserDataFromTable('users', user)
    if len(data) == 0:
        return False
    else:
        return True

def insertIntoTable(tableName, login, password):
    conn, cursor = connectToDatabase()

    h = hashlib.md5(password.encode('utf-8'))
    hashPass = h.hexdigest()
    
    query = "INSERT INTO {} (login, password) VALUES ('{}', '{}')".format(tableName, login, hashPass)

    cursor.execute(query)

    conn.commit()
    closeConnection(conn)