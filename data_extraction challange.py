data_log="20240315TEMP:25.8C-LOC:NYC-STATUS:OK"
# Use slicing to extract the data from the string below:
# Extract Date: Get the date portion (20240315).
#Extract Temperature: Get the temperature value (25.8).
#Extract Location Code: Get the location code (NYC).
#Extract Status: Get the status (OK).
date=None
temp=None
location=None
status=None
date_length=len('20240315')
date_index=data_log.find('20240315')
date=data_log[date_index:date_length]

temp_index=data_log.find('TEMP:25.8C')
temp_length=len('TEMP:25.8C')
temp_value_index=data_log.find('TEMP:25.8C')+len('TEMP:')
temp_value_length=len('25.8')
temp=data_log[temp_index:temp_index+temp_length]
temp_value=data_log[temp_value_index:temp_value_index+temp_value_length]

location_index=data_log.find('LOC:NYC')
location_length=len('LOC:NYC')
location_value_index=data_log.find('LOC:NYC')+len('LOC:')
loction_value_length=len('NYC')
location=data_log[location_index:location_index+location_length]
location_value=data_log[location_value_index:location_value_index+loction_value_length]

status_index=data_log.find('STATUS:OK')
status_length=len('STATUS:OK')
status_value_index=data_log.find('STATUS:OK')+len('STATUS:')
status_value_length=len('STATUS:OK')
status=data_log[status_index:status_index+status_length]
status_value=data_log[status_value_index:status_value_index+status_value_length]
print(date,temp,location,status)
print(f'Date:{date}\nTemperature:{temp_value}\nLocation:{location_value}\nStatus:{status_value}')
