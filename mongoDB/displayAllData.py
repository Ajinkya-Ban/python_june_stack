import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = conn["testdb"] #database created
mycoll = mydb["customer"]

for x in mycoll.find():
    print(x)