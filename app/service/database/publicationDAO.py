from app.models.Connection import Connection
from bson import ObjectId

class PublicationDAO:
    def __init__(self):
        connection = Connection()
        self.client = connection.connection()
        self.db = self.client['publications_dou']
    
    
        
    def create(self, publication):
        collection = self.db[publication.if_collecion]

        # Construindo o campo a ser adicionado/atualizado
        update = {
            f"months.{publication.month}": {
                "publication":{
                    "type": publication.type,
                    "organ": publication.organ,
                    "content": publication.content,
                    "concierge": publication.concierge,
                    "date": publication.date,
                    "responsible": publication.responsible,
                    "url": publication.url
                }
            }
        }
   
    
        # Atualizando o documento existente ou inserindo um novo
        result = collection.update_many(
            {"year": publication.year},
            {"$push": update},
            upsert=True  # Cria um novo documento se não encontrar nenhum correspondente
        )
        
        return result.upserted_id if result.upserted_id else "Coleção atualizada"
        
    def read(self, coll):
        
        collection = self.db[coll]
        document = collection.find({'year':2018})
        self.client.close()
        return document
    
    def list(self):
        #self.client = self.get()
        n = self.client.list_database_names()
        self.client.close()
        return n
        
    def delete(self, name):
        self.client.drop_database(name)
        self.client.close()
        
    def delete_doc(self):
        
        colecao = self.db["ifac"]
        id = {"_id": ObjectId("666a8b1886a708d806f6c073")}
        colecao.find_one_and_delete(id)
        self.client.close()
        
    def close(self):
        self.client.close()
        
    
        
        
        
        