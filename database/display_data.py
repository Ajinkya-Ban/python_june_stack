import pymysql as pysql
from tabulate import tabulate
conn = pysql.connect(host="localhost",user="root",passwd="admin123",database="stud")
cur = conn.cursor()
cur.execute("select * from info")
result = cur.fetchall()
columns = ["ID","Student Name","Pancard","Email","Salary"]
print(tabulate(result,tablefmt="rst",headers=columns,missingval="NA"))


