CREATE TABLE keg_readings 
(
keg_id int,	
ip varchar,	
location varchar,	
reading_id int,	
reading_order int,	
reading_value int,	
time timestamp);


COPY keg_readings FROM '/Users/carsonf/Desktop/klevr/kegcode/test_data.csv' WITH (FORMAT csv, HEADER false);