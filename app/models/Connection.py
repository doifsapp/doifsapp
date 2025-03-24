from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://doifaplicacao:65RfPHZHWrZEtf9n@cluster0.lxzu3pv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
class Connection:
    def __init__(self):
        self.client = MongoClient(uri)
        
    def connection(self):
        return self.client
        
        
        
        

