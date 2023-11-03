
import pandas as pd

# path to csv file
csv_file = 'Data/fire_incidents.csv'

'''
coulmns:

(['Incident_id', 'Area_of_Origin', 'Building_Status', 'Business_Impact',
       'Civilian_Casualties', 'Count_of_Persons_Rescued',
       'Estimated_Dollar_Loss', 'Estimated_Number_Of_Persons_Displaced',
       'Exposures', 'Ext_agent_app_or_defer_time', 'Extent_Of_Fire',
       'Final_Incident_Type', 'Fire_Alarm_System_Impact_on_Evacuation',
       'Fire_Alarm_System_Operation', 'Fire_Alarm_System_Presence',
       'Fire_Under_Control_Time', 'Ignition_Source', 'Incident_Number',
       'station_id', 'Ward', 'Initial_CAD_Event_Type', 'Intersection',
       'Last_TFS_Unit_Clear_Time', 'Latitude', 'Level_Of_Origin', 'Longitude',
       'Material_First_Ignited', 'Method_Of_Fire_Control',
       'Number_of_responding_apparatus', 'Number_of_responding_personnel',
       'Possible_Cause', 'Property_Use', 'Smoke_Alarm_at_Fire_Origin',
       'Smoke_Alarm_at_Fire_Origin_Alarm_Failure',
       'Smoke_Alarm_at_Fire_Origin_Alarm_Type',
       'Smoke_Alarm_Impact_on_Persons_Evacuating_Impact_on_Evacuation',
       'Smoke_Spread', 'Sprinkler_System_Operation',
       'Sprinkler_System_Presence', 'Status_of_Fire_On_Arrival',
       'TFS_Alarm_Time', 'TFS_Arrival_Time', 'TFS_Firefighter_Casualties']
'''

# rename columns to lowercase
df = pd.read_csv(csv_file)
df.columns = df.columns.str.lower()

# calculate response time
df['response_time'] = pd.to_datetime(df['tfs_arrival_time']) - pd.to_datetime(df['tfs_alarm_time'])

# convert response time to seconds
df['response_time'] = df['response_time'].dt.total_seconds()

# filter for rows that have "response_time" > 0
df = df[df['response_time'] > 0]


# coulmns to keep
columns_to_keep = ['incident_id', 'station_id', 'ward', 'latitude', 'longitude', 'response_time']
# NOTE: Some other columns that might be useful: 'fire_under_control_time', 'status_of_fire_on_arrival', 'tfs_alarm_time', 'tfs_arrival_time',


# save coulmns to csv file
df[columns_to_keep].to_csv('Data/fire_incidents_processed.csv', index=False)
