import psycopg2
import os

#DB_HOST = 'localhost'
#DB_USERNAME = 'postgres'
#DB_NAME = 'store_manager'
#DB_PASS = 'toor10010'
#DB_PORT = '5432'

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


#print(db_url)

#creating connection
#con = psycopg2.connect(url)

#creating cursor
#cur = con.cursor()

#executing the sql query
#result = con.execute(Select from users)

#closing connection
#con.close()