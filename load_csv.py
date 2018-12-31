import psycopg2
import os
import zipfile

rebuildTable = True
try:
  conn = psycopg2.connect("host=192.168.1.2 dbname=Citibike user=Citibike password=citibike")
  print ("connected to db")
except:
  print ("I am unable to connect to the database")

cur = conn.cursor()
if rebuildTable:
  print("Rebuilding Trips Table")
  cur.execute("Drop Table trips;")
  cur.execute("""
  Create Table Trips (
    id serial not null,
    tripduration int,
    starttime timestamp,
    stoptime timestamp,
    start_station_id int,
    start_station_name character varying(150),
    start_station_latitude character varying(150),
    start_station_longitude character varying(150),
    end_station_id int,
    end_station_name character varying(150),
    end_station_latitude character varying(150),
    end_station_longitude character varying(150),
    bikeid int,
    usertype  character varying(150),
    birth_year character varying(4),
    gender int)
  """)
  conn.commit()

runs = 0
totalRuns = 3
pathToZips = '../'

for filename in os.listdir(pathToZips):
    print("Loading file " + runs + " of " + totalRuns)
    if filename.endswith(".zip"):
      with zipfile.ZipFile(pathToZips + filename) as zf:
        for f in zipfile.ZipFile.namelist(zf):
          if os.path.splitext(f)[1] == '.csv':
              csv = zf.open(f)
              cur.copy_expert("""copy trips (tripduration, 
              starttime, 
              stoptime, 
              start_station_id, 
              start_station_name, 
              start_station_latitude, 
              start_station_longitude, 
              end_station_id, 
              end_station_name, 
              end_station_latitude, 
              end_station_longitude, 
              bikeid, 
              usertype, 
              birth_year, 
              gender ) from stdin CSV HEADER Null 'NULL' """, csv)
              conn.commit()
      if runs > totalRuns:
        print('file limit breaker hit')
        break