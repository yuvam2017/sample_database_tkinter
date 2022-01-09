import pymongo
from pymongo.common import partition_node
from pymongo.ssl_support import _load_wincerts
# myclient = pymongo.MongoClient("mongodb://localhost:9999/")
# mydb = myclient["mydatabase"]

if __name__ == "__main__":
  print("Welcome to PyMongo")
  client = pymongo.MongoClient("mongodb://localhost:27017/")
  print(client)
  db = client['harry']
  collection = db['mySampleCollection']
  mydict = [
    {"name":"john","add":"sahima colony"},
    {"name":"mahima","add":"vastra colony"},
    {"name":"manish","add":"dubhasd colony"},
    {"name":"sam","add":"seherala colony"}
  ]
  # collection.insert_many(mydict)

  # one = collection.find_one({'name':'john'})
  # print(one)

  find_many = collection.find({'name':'john'})
  for item in find_many:
    print("ITEMS Are : " , item)
  print(list(collection.find({'name':'john'})))
  print(_load_wincerts)  
