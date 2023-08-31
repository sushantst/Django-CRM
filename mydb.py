import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'ME5048@1'
    
    )

cursorObject = dataBase.cursor()
cursorObject.execute('CREATE DATABASE stdb')
print("All done")
