from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, 
                 userParam = 'aacuser', 
                 passParam = 'SNHU1234',
                 hostParam = 'nv-desktop-services.apporto.com',
                 portParam = 31392,
                 dbParam = 'AAC',
                 collectionParam = 'animals'):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = userParam
        PASS = passParam
        HOST = hostParam
        PORT = portParam
        DB = dbParam
        COL = collectionParam
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)  # data should be dictionary
            if result is not None:
                pprint.pprint(result)
            else:
                print("No records found")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
# Read One Method
    def read_one(self, data):
        if data is not None:
            result = self.database.animals.find_one(data)
            if result is not None:
                for key, value in result.items():
                    formatted_key = key.replace('_', ' ')
                    print(f"{formatted_key}: {value}")
                return True
            else:
                print("No records found")
                return False
        else:
            raise Exception("Nothing to read, data parameter empty")

# Read Many Method
    def read(self, data, limit = -1):
        if data == {}:
            return self.database.animals.find()
        if data is not None:
            if limit == -1:
                result = self.database.animals.find(data)
            else:
                result = self.database.animals.find(data).limit(limit)
            if result is not None:
                return result
            else:
                print("No records found")
                return False
        else:
            raise Exception("Nothing to read, data parameter empty")
            
#Update one method
    def update_one(self, filter_data, data):
        if data is not None:
            result = self.database.animals.update_one(filter_data, {"$set": data})
            if result is not None:
                pprint.pprint(result.raw_result)
            else:
                raise Exception("Failed to update. Check criteria.")
        else:
            raise Exception("Nothing to read, data parameter empty.")
                
#Update many method
    def update_many(self, filter_data, data):
        if data is not None:
            result = self.database.animals.update_many(filter_data, {"$set": data})
            if result is not None:
                pprint.pprint(result.raw_result)
            else:
                raise Exception("Failed to update. Check criteria.")  
        else:
            raise Exception("Nothing to read, data parameter empty.")
                
        
#Delete one method
    def delete_one(self, data):
        if data is not None:
            result = self.database.animals.delete_one(data)
            if result is not None:
                pprint.pprint(result.raw_result)
            else:
                raise Exception("Failed to delete. Check criteria.")
        else:
            raise Exception("Nothing to read, data parameter empty")
                                
#Delete many method                                
    def delete_many(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data)
            if result is not None:
                pprint.pprint(result.raw_result)
            else:
                raise Exception("Failed to delete. Check criteria.")
        else:
            raise Exception("Nothing to read, data parameter empty.")