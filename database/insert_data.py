import pymysql as pysql

name = input("Enter the name = ")
pancarad = input("Enter pan details = ")
email = input("Enter the email = ")
salary = float(input("Enter the salary ="))

try:
    conn = pysql.connect(host="localhost", user="root", passwd="admin123", database="stud")
    cur = conn.cursor()
    sql_insert_query = "insert into info(sname, pancard,email,salary) values(%s,%s,%s,%s)"
    values = (name,pancarad,email,salary)
    cur.execute(sql_insert_query,values)
    conn.commit()
    print(cur.rowcount,"=row inserted")
except Exception as err:
    print(err)
finally:
    cur.close()
    conn.close()



