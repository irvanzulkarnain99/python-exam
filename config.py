import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="webhook_integration"
)

if db.is_connected():
  print("Success connect to database")