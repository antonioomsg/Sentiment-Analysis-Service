import os
import dotenv
dotenv.load_dotenv()

PORT = os.getenv("PORT")
DBURL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("MONGO_DB_NAME")