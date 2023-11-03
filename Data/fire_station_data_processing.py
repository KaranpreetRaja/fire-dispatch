
import pandas as pd

# path to csv file
csv_file = 'Data/fire_stations.csv'

# use pandas to read csv file and filter for rows that have "station_id" != 0
df = pd.read_csv(csv_file)
df = df[df['station_id'] != 0]

# extract longitude and latitude from "station_geometry" column which has data in format "{'type': 'MultiPoint', 'coordinates': [[-79.2428700353868, 43.8239927252015]]}" and create new columns for longitude and latitude

# from "{'type': 'MultiPoint', 'coordinates': [[-79.2428700353868, 43.8239927252015]]}" to "-79.2428700353868, 43.8239927252015"
df['coordinates'] = df['station_geometry'].apply(lambda x: x.split(':')[-1].split(']')[0].split('[')[-1])
# from "-79.2428700353868, 43.8239927252015" to "-79.2428700353868"
df['station_longitude'] = df['coordinates'].apply(lambda x: x.split(',')[0])
df['station_latitude'] = df['coordinates'].apply(lambda x: x.split(',')[1])


# save coulmns "station_id", "station_ward", "station_address", "station_longitude", "station_latitude" to csv file
df[['station_id', 'station_ward', 'station_address', 'station_longitude', 'station_latitude']].to_csv('Data/fire_stations_processed.csv', index=False)