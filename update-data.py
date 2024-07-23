import config

shop_id    = input("Input Shop Name : ")
to_shop_id = input("Update Shop Name to : ")
val        = (shop_id,)
db         = config.db.cursor()

sql = "SELECT * FROM webhook_integration.webhookconfiguration WHERE shop_id = %s"

db.execute(sql, val)

results = db.fetchall()
if db.rowcount == 0: 
    print("Data Not Found")
else:
    for data in results:
        id = data[0]
        val_update = (to_shop_id, id)
        sql_update = "UPDATE webhook_integration.webhookconfiguration SET shop_id = %s WHERE webhook_configuration_id = %s"
        db.execute(sql_update, val_update)

        config.db.commit()

        print("Success update Shop Name")