from pymongo import MongoClient

MONGO_USERNAME = 'luyza519'
MONGO_PASSWORD = 'xUm6IFIFgtrZMbxJ'  # Substitua pela sua senha real
MONGO_CLUSTER_URL = 'pi5.m6jciwx.mongodb.net'

connection_string = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER_URL}/?retryWrites=true&w=majority&appName=PI5"

client = MongoClient(connection_string)
db = client['User']  # Substitua pelo nome do banco de dados que deseja usar
