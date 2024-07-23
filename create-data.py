import config

shop_id = input("Input Shop Name : ")
created_by = input("Input Your Name : ")
val = (shop_id, created_by, created_by)
db = config.db.cursor()
sql = "INSERT INTO webhook_integration.webhookconfiguration (shop_id,is_active,created_date,modified_date,cerated_by,modified_by) VALUES(%s,1,NOW(),NOW(),%s,%s)"
db.execute(sql, val)

config.db.commit()

print(format(db.rowcount))