import mysql.connector

connection = mysql.connector.connect(
  host='localhost',
  user='root',
  password='bbgun3001',
  database='stock_analysis'
)

if connection.is_connected():
  print('Connected to MySQL database')