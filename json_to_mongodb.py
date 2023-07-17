import json
from pymongo import MongoClient

# Load the JSON data from the file
with open('jsondata.json', encoding='utf-8') as file:
    json_data = json.load(file)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
database = client['jsondata']  # Replace 'your_database_name' with your actual database name
collection = database['data']  # Replace 'your_collection_name' with your actual collection name

# Insert the JSON data into the MongoDB collection
collection.insert_many(json_data)

# Close the MongoDB connection
client.close()
