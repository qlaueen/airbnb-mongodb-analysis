import pymongo

connection = pymongo.MongoClient("class-mongodb.cims.nyu.edu", 27017,
                                username="lml9279",
                                password="AFxt9JNf",
                                authSource="lml9279")
collection = connection["lml9279"]["listings"]

# the collection variable will be a reference to your collection
docs = collection.find({}).limit(10) # get the first 10 documents
print(docs)
