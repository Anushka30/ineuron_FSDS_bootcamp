import pymongo

client = pymongo.MongoClient("mongodb+srv://mongodbtest:1008@cluster0.djt6c.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name": "Anushka",
    "email": "abc@gmail.com",
    "class": "FSDS"
}

db1 = client['mongotest']
col = db1['test']
col.insert_one(d)
