from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "26899990"))
API_HASH = environ.get("API_HASH", "907b19ed343ff79665bb132d584890f5")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7325735846")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
