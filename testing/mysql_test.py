import mysql.connector
from mysql.connector import Error

print("boo")
def connect():
  print("hey")
  try:
    print("hdwjhsf")
    conn = mysql.connector.connect(host='localhost', user='root', password='Qwerty24')
    if conn.is_connected():
      print('Connected to MySQL database')
 
  except Error as e:
    print(e)
 
  finally:
    conn.close()
    
connect()
