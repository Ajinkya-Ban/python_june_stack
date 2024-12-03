import pymysql as pysql

name = input("Enter the name = ")
pancarad = input("Enter pan details = ")
email = input("Enter the email = ")
salary = float(input("Enter the salary ="))
sid = int(input("Enter the Id to update the above fields="))

try:
    conn = pysql.connect(host="localhost", user="root", passwd="admin123", database="stud")
    cur = conn.cursor()
    sql_update_query = "update info set sname=%s, pancard=%s, email=%s, salary=%s where sid=%s"
    values = (name,pancarad,email,salary,sid)
    cur.execute(sql_update_query,values)
    conn.commit()
    print(cur.rowcount," =row updated")
except Exception as err:
    print(err)
finally:
    cur.close()
    conn.close()
