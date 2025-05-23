import configparser
import os


parser = configparser.ConfigParser

parser.read(os.path.join(os.path.dirname(__file__),'../config/config.conf'))


CLIENT_ID = parser.get('api_key','reddit_client_id')
CLIENT_SECRET = parser.get('api_key','reddit_secret_key')

DATABASE_HOST = parser.get('database','database_host')
DATABASE_PORT = parser.get('database','database_host')
DATABASE_USERNAME = parser.get('database','database_host')
DATABASE_DATABASE = parser.get('database','database_host')
DATABASE_PASSWORD = parser.get('database','database_host')