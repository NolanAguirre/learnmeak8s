import os
import psycopg
from psycopg_pool import ConnectionPool

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://postgres:postgres@localhost:5431/learnmeak8s')

def get_db_connection():
    return psycopg.connect(DATABASE_URL)

def get_db_pool(minconn=1, maxconn=5):
    return ConnectionPool(DATABASE_URL, min_size=minconn, max_size=maxconn)

def get_threaded_db_pool(minconn=1, maxconn=5):
    return ConnectionPool(DATABASE_URL, min_size=minconn, max_size=maxconn)




