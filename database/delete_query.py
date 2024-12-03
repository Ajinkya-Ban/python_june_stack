import pymysql as pysql

sid = int(input("Enter the Id to delete record="))
conn = pysql.connect(host="localhost", user="root", passwd="admin123", database="stud")
try:
    cur = conn.cursor()
    sql_update_query = "delete from info where sid = %s"
    values = (sid)
    cur.execute(sql_update_query,values)
    conn.commit()
    print(cur.rowcount," =row deleted")
except Exception as err:
    print(err)
finally:
    cur.close()
    conn.close()
