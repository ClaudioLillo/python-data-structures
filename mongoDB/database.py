import pymongo

class Database:
    def __init__(self, database_name):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = client[database_name]
        self.tables = {}

    def create_table(self, table_name):
        self.tables[table_name] = self.database[table_name]

    def list_tables(self):
        print(self.database.list_collection_names())

    def insert_one(self, table_name, item):
        self.tables[table_name].insert_one(item)

database = Database('animals')

#database.create_table('gatos')

#database.insert_one('gatos', {'name': 'grett'})

database.list_tables()






# db.name_col.insert_one({"key" : "value"})
# print(client.list_database_names())
