#!/usr/bin/env python3

# entry point for Lambda or run_local

from weatherController import WeatherController

def lambda_handler(event, context):

  wc = WeatherController()
  wc.execute()

if __name__ == "__main__":
  pass
