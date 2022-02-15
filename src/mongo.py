from pymongo import MongoClient
# pprint library is used to make the output look more pretty
import json
from pprint import pprint
import os
import constants
print(constants.MONGO_ACCOUNT)

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(constants.MONGO_ACCOUNT)
db=client.public
# Issue the serverStatus command and print the results
collection = db.players

# with open('stat_files/kuri_neon_ops.json') as file:
#     file_data = json.load(file)


# if isinstance(file_data, list):
#     collection.insert_many(file_data)  
# else:
#     collection.insert_one(file_data)

pprint(db.players.find_one({'username': 'Avoxen'}))

#Tx3Mn1FfVqNZxMxNsNHuI4xDNcUf4UzRcHDJnIn6VvGHnEMaZmQme63MOi0r2WRa