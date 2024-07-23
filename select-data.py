import config

db = config.db.cursor()
sql = "SELECT * FROM webhookconfiguration"
db.execute(sql)

results = db.fetchall()

for data in results:
  print(data)