Drop Table Trips;

Create Table Trips (
id serial not null,
tripduration character varying(150),
starttime date,
stoptime date,
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

