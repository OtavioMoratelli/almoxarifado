import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'adminroot'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE Almoxarifado")

print('criado')
