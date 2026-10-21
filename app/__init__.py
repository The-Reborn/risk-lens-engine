from flask import Flask
from pymongo import MongoClient
import os

# Global database reference so models/services can access it easily
db = None

def create_app():
    global db
    app = Flask(__name__)
    
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/risk_lens_db")
    
    try:
        client = MongoClient(mongo_uri)
        db = client.get_database()
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print(f"Warning: Could not connect to MongoDB: {e}")

    from app.api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app