
#!/usr/bin/python3

import mysql.connector as mariadb
import Adafruit_BMP.BMP085 as BMP085
import time
from datetime import datetime, timedelta

_connection = None
_cursor = None
_keep_looping = True
_loop_delay = 5

def get_connection():
    global _connection
    if not _connection:
        _connection = mariadb.connect(user='dbuser', password='dbpassword', database='sewer')
    return _connection

def close_connection():
    global _connection
    if _connection:
        _connection.close()
        _connection = None

def get_cursor():
    global _cursor
    if not _cursor:
        _cursor = get_connection().cursor()
    return _cursor

def close_cursor():
    global _cursor
    if _cursor:
        _cursor.close()
        _cursor = None

def add_reading(reading):
    get_cursor().execute("USE sewer")
    sql = "INSERT INTO pressures (reading) VALUES (%s)"
    val = (reading,)
    get_cursor().execute(sql, val)
    records_added = get_cursor().rowcount
    get_connection().commit()
    close_cursor()
    close_connection()
    return records_added

def get_readings(from_date = "", to_date = ""):
    # date times in YYYY-MM-DD HH:MM:SS
    if from_date == "":
        from_date = date_string(5)
    if to_date == "":
        to_date  = date_string()

    get_cursor().execute("USE sewer")
    get_cursor().execute(f"SELECT * from pressures where timestamp between cast('{from_date}' as datetime) AND cast('{to_date}' as datetime)")
    records = get_cursor().fetchall()
    close_cursor()
    close_connection()
    return records

def date_string(mins_to_subtract = 0):
    value = datetime.now() - timedelta(minutes = mins_to_subtract)
    value = value.strftime("%Y-%m-%d %H:%M:%S")
    return value

def stop_reading():
    global _keep_looping
    _keep_looping = False

def start_reading():
    global _keep_looping
    _keep_looping = True
    main_loop()

def get_data(from_date = "", to_date = ""):
    records = get_readings(from_date, to_date)
    labels = []
    data = []
    for id, timestamp, reading in records:
        output_format = timestamp.strftime("%d/%m %H:%M:%S")
        labels.append(output_format)
        data.append(reading)
    return labels, data

def main_loop():
    global _loop_delay
    global _keep_looping
    sensor = BMP085.BMP085()
    while _keep_looping:
        reading = sensor.read_pressure()
        no_of_records_added = add_reading(reading)
        time.sleep(_loop_delay)

# List of stuff accessible to importers of this module. Just in case
__all__ = [ 'get_connection' ]
