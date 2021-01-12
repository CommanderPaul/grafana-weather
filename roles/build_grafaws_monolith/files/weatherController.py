#!/usr/bin/env python3

from weatherman import CallWeatherman
from postgresDBO import PostgresDBO
from dbQueries.allResponseQueries import AllResponseQueries

class WeatherController:

  def __init__(self):
    print('Initializing WeatherController')

  def execute(self):

    wet = CallWeatherman()
    wet_response = wet.execute()

    dbo = PostgresDBO()

    arq = AllResponseQueries(wet_response)

    locationQuery = arq.locationInsert()
    location_id = dbo.executeInsert(locationQuery)

    currentQuery = arq.currentInsert(location_id)
    current_id = dbo.executeInsert(currentQuery)

    hourlyQuery = arq.hourlyInsert(location_id)
    hourly_id = dbo.executeValues(hourlyQuery)

    dailyQuery = arq.dailyInsert(location_id)
    daily_id = dbo.executeValues(dailyQuery)

    dbo.closeConnection()

if __name__ == "__main__":
  pass
