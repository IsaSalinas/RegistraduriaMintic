import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://jjrios:P4$$w0rd123@misiontic2022.gmr1yap.mongodb.net/backend_results?retryWrites=true&w=majority",
    tlsCAFile=ca
)

db = client.test
print(db)

data_base = client['backend_results']
print(data_base.list_collection_names())


candidate = data_base.get_collection('candidate')
all_candidates = candidate.find({})
