from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "25666094"))
API_HASH = environ.get("API_HASH", "5223c65e405cc3f52fa23ddd070f4c35")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "7625630924:AAG4WfmPiomEfFpeVlbDZQV-Y5tUv5SRKcY")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "5983253591")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1002456290797")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://aakash00:<db_password>@cluster0.pqcyxxf.mongodb.net/?retryWrites=true&w=majority")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
