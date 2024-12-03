import pymysql as pysql
try:
    conn = pysql.connect(host="localhost",user="root",passwd="admin123",database="stud")
    if conn:
        print("Successfully connected")
    else:
        print("Not connected")
except Exception as err:
    print(err)