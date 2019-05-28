import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = "saiba",
    passwd = "1110235361",
    database = "priotuli"
    #auth_plugin='mysql_native_password'
    )
myCursor = mydb.cursor()
#myCursor.execute("CREATE database test222")
sql="CREATE TABLE arts(art_id int auto_increment PRIMARY KEY, art_name VARCHAR(300), art_rate FLOAT)"
myCursor.execute(sql)
mydb.commit()
myCursor.close()
mydb.close()
