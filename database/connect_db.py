import mysql.connector

connection = mysql.connector.connect(
  host='localhost',
  user='root',
  password='password',
  database='stock_analysis'
)

if connection.is_connected():
  print('Connected to MySQL database')
