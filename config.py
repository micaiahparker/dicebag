import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

class Config:
    DEBUG=os.environ.get('FLASK_DEBUG')
    SECRET_KEY=os.environ.get('SECRET_KEY')
