import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")
print(conn.list_database_names())

if "testdb" in conn.list_database_names():
    print("Database already present")
else:
    mydb = conn["testdb"] #database created
    mycoll = mydb["customer"] # create the collection
    data = {"name":"abc", "city":"pune"} #create the data in json format.
    myValue = mycoll.insert_one(data)
    print(myValue)




