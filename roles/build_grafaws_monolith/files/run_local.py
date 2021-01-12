#!/usr/bin/env python3

import configparser
import os

from handler import lambda_handler

class RunLocal:
  pathToSecrets = '/home/ubuntu/.ssh/secrets.ini'
  print('Path to secrets {}'.format(pathToSecrets))

  def __init__(self):
    print('Loading env vars from secrets.ini')
    cfg = configparser.ConfigParser()

    # TODO wrap in try/catch
    cfg.read(self.pathToSecrets)

    os.environ['APP_ID'] = cfg.get('secrets', 'APP_ID')
    os.environ['DB_USER'] = cfg.get('secrets', 'postgres_remote_admin_username')
    os.environ['DB_PASSWORD'] = cfg.get('secrets', 'postgres_remote_admin_password')
    os.environ['DB_HOST'] = cfg.get('secrets', 'postgres_database_host')
    os.environ['DB_PORT'] = cfg.get('secrets', 'postgres_database_port')
    os.environ['DB_DATABASE'] = cfg.get('secrets', 'postgres_database_name')

    print('Calling handler')
    event = {}
    context = {}
    lambda_handler(event,context)

if __name__ == '__main__':
  runLocal = RunLocal()
