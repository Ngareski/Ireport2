import psycopg2
import os


url = "dbname='store_manager' host='localhost' port='5432' user='postgres' password='toor10010'"

db_url = os.getenv('DATABASE_URL')

def connection(url):
    con = psycopg2.connect(url)

def create_tables():
    query1 =
    query2 = create_tables

    queries = [query1, query2]

    for q in queries
    pass

def destroy_tables():
    pass
