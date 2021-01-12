#!/usr/bin/env python3

import requests
import json
import os

from dbQueries.allResponseQueries import AllResponseQueries

class CallWeatherman:

  BASE_URL = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&units=imperial"

  # Portland lat lon
  LAT = "45.47"
  LON = "-122.65"

  def __init__(self):
    self.temperature = 0

  def execute(self):
    app_id = os.environ.get('APP_ID')
    response = requests.get(self.BASE_URL.format(self.LAT, self.LON, app_id))
    if response.status_code != 200:
      # This means something went wrong.
      print('Openweathermap.org response code {}'.format(response.status_code))
    return_bin = b""

    for response_part in response:
      return_bin += response_part

    all_response = json.loads(return_bin.decode())
    return all_response

if __name__ == "__main__":
  pass
