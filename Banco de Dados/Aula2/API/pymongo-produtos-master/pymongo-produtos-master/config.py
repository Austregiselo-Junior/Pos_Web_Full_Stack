from pymongo import MongoClient

# Conetando com MySQL local
SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1:3306/banco_web'

# Conectando com Mongodb local
cliente = MongoClient('mongodb://localhost:27017')
mongodb = cliente['banco_web']
pedidos_collection = mongodb['pedidos']

