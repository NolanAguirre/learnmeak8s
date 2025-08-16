import os
import psycopg2
from psycopg2 import pool
from psycopg2.pool import ThreadedConnectionPool

DB_URL = os.environ.get('DATABASE_URL', 'postgres://postgres:postgres@localhost:5431/learnmeak8s')

def get_db_connection():
    return psycopg2.connect(DB_URL)

def get_db_pool(minconn=1, maxconn=5):
    return pool.SimpleConnectionPool(minconn, maxconn, DB_URL)

def get_threaded_db_pool(minconn=1, maxconn=5):
    return ThreadedConnectionPool(minconn, maxconn, DB_URL)




