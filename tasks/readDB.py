from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

# Se establece conexión con BD
def readData():
    
    uri = "mongodb+srv://admin:securePassword@dbenvioschallenge.pzxocmx.mongodb.net/?retryWrites=true&w=majority"

    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')
        db = client["dbEnviosChallenge"]
        collection = db["dbEnviosChallenge"]

        shipping_statuses = ["completed", "returned"]
        query = {"shipping_status": {"$in": shipping_statuses}}
        data = collection.find(query)
        queryDataFrame = pd.DataFrame(data)

        return queryDataFrame
    
    except Exception as e:
        print("Error al conectar con la base de datos: ",e)