import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user =  'root',
    passwd = 'inter@972',
    auth_plugin='mysql_native_password'
)

# prepare a cursor object

cursorObject = database.cursor()

# Create a database

cursorObject.execute("CREATE DATABASE crmdb")

print('Database created')