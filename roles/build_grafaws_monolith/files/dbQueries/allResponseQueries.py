#!/usr/bin/env python3

import datetime

class AllResponseQueries:
  
  def __init__(self, all_response):
    self.all_response = all_response
    self.dto = datetime.datetime

  def locationInsert(self):
    query = ''' INSERT INTO location (lat, lon, timezone, timezone_offset) 
              VALUES (%s, %s, %s, %s) RETURNING location_id;
              '''
    valuesTuple = ( self.all_response['lat'], 
                    self.all_response['lon'],
                    self.all_response['timezone'],
                    self.all_response['timezone_offset']
                    )
    returnDict = {'query': query, 'valuesTuple': valuesTuple}
    return returnDict

  def currentInsert(self, location_id):
    query = ''' INSERT INTO current (location_id, dt, sunrise, sunset, temp, feels_like, pressure, 
                                     humidity, dew_point, clouds, uvi, visibility, wind_speed,
                                     wind_deg) 
                VALUES (%s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s) RETURNING current_id;
    '''
    current = self.all_response['current']

    valuesTuple = ( location_id,
                    self.dto.fromtimestamp(current['dt']),
                    self.dto.fromtimestamp(current['sunrise']),
                    self.dto.fromtimestamp(current['sunset']),
                    current['temp'],
                    current['feels_like'],
                    current['pressure'],
                    current['humidity'],
                    current['dew_point'],
                    current['clouds'],
                    current['uvi'],
                    current['visibility'],
                    current['wind_speed'],
                    current['wind_deg']
                    )

    returnDict = {'query': query, 'valuesTuple': valuesTuple}
    return returnDict

  def hourlyInsert(self, location_id):

    # format to use execute_values   https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query

    query = ''' INSERT INTO hourly (location_id, dt, temp, feels_like, pressure, 
                                  humidity, dew_point, clouds, visibility, wind_speed,
                                  wind_deg, pop) 
                VALUES %s; '''

    hourly = self.all_response['hourly']
    listOfTuples = []

    for hour in hourly: 

      valuesTuple = ( location_id, 
                      self.dto.fromtimestamp(hour['dt']),
                      hour['temp'],
                      hour['feels_like'], 
                      hour['pressure'],
                      hour['humidity'], 
                      hour['dew_point'],
                      hour['clouds'],
                      hour['visibility'],
                      hour['wind_speed'], 
                      hour['wind_deg'],
                      hour['pop'],
                      )
      listOfTuples.append(valuesTuple)

    returnDict = {'query': query, 'listOfTuples': listOfTuples}
    return returnDict

  def dailyInsert(self, location_id):

    query = ''' INSERT INTO daily (location_id, dt, sunrise, sunset,
                                    temp_day, temp_min, temp_max,
                                    temp_night, temp_eve, temp_morn,
                                    feels_like_day, feels_like_night,
                                    feels_like_eve, feels_like_morn,
                                    pressure, humidity, dew_point,
                                    wind_speed, wind_deg,
                                    clouds, pop, uvi ) 
                  VALUES %s; '''

    daily = self.all_response['daily']
    listOfTuples = []

    for day in daily:
      valuesTuple = ( location_id, 
                      self.dto.fromtimestamp(day['dt']),
                      self.dto.fromtimestamp(day['sunrise']),
                      self.dto.fromtimestamp(day['sunset']), 
                      day['temp']['day'],
                      day['temp']['min'],
                      day['temp']['max'],
                      day['temp']['night'],
                      day['temp']['eve'],
                      day['temp']['morn'],
                      day['feels_like']['day'], 
                      day['feels_like']['night'],
                      day['feels_like']['eve'],
                      day['feels_like']['morn'],
                      day['pressure'],
                      day['humidity'],
                      day['dew_point'],
                      day['wind_speed'],
                      day['wind_deg'],
                      day['clouds'],
                      day['pop'],
                      day['uvi'])
      listOfTuples.append(valuesTuple)

    returnDict = {'query': query, 'listOfTuples': listOfTuples}
    return returnDict
