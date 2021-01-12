#!/usr/bin/env python3

import psycopg2
from psycopg2.extras import execute_values
import os

class PostgresDBO:

  def __init__(self):
    print('Initializing PostgresDBO')
    print('Connecting to database')
    try:
      self.connection = psycopg2.connect(user = os.environ.get('DB_USER'),
                        password = os.environ.get('DB_PASSWORD'),
                        host = os.environ.get('DB_HOST'),
                        port = os.environ.get('DB_PORT'),
                        database = os.environ.get('DB_DATABASE'),
                        options=f'-c search_path=weatherman') # search_path sets schema

      print('Getting cursor')
      self.cursor = self.connection.cursor()
    except (Exception, psycopg2.Error) as error:
      print ("Error while connecting to PostgreSQL", error)

  def executeValues(self, queryDict):
    response = ''
    try:
      response = execute_values(self.cursor, queryDict['query'], queryDict['listOfTuples'])
      self.connection.commit() # required for inserts
    except (Exception, psycopg2.Error) as error:
      print ("Error while executing query", error)
    finally:
      return response

  def executeInsert(self, queryDict):
    insert_id = ''
    try:
      self.cursor.execute(queryDict['query'], queryDict['valuesTuple'])
      self.connection.commit() # required for inserts
      insert_id = self.cursor.fetchone()[0]
    except (Exception, psycopg2.Error) as error:
      print ("Error while executing query", error)
    finally:
      return insert_id

  def executeSelect(self, query):
    db_response = ''
    try:
      self.cursor.execute(query)
      db_response = self.cursor.fetchone()
    except (Exception, psycopg2.Error) as error:
      print ("Error while executing query", error)
    finally:
      return db_response

  def closeConnection(self):
    if(self.connection):
      print('Closing cursor')
      self.cursor.close()
      print("Closing connection")
      self.connection.close()

if __name__ == '__main__':
  pass
