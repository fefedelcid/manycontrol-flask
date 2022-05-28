from pymongo import MongoClient

uri = "mongodb+srv://manycontrol-dev.w0p5vnc.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri, tls=True, tlsCertificateKeyFile='<path_to_certificate>')


db = client['testDB']
collection = db['testCollection']

doc_count = collection.count_documents({})
print(doc_count)
