import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point


rent_data = pd.read_csv("data/Rent_Price__LA_.csv")
crime_data = pd.read_csv("data/Crime_Data_from_2010_to_2019.csv")
LA_Neighborhood_map = gpd.read_file("data/Los Angeles Neighborhood Map.geojson")
rent_data_valid = rent_data[["Year", "Amount", "Neighborhood", "Location"]]
crime_data_valid = crime_data[["DATE OCC", "LAT", "LON", ""]]

crime_data_valid["Year"] = crime_data_valid["DATE OCC"].apply(lambda x: int(x[6:10]))
crime_data_valid = crime_data_valid[crime_data_valid["Year"] <= 2016]
rent_data_valid["point"] = rent_data_valid.Location.apply(lambda x: Point(map(float, x.strip("()").split(","))))
crime_data_valid["point"] = crime_data_valid.loc[:, ["LON", "LAT"]].values.tolist()
crime_data_geo = gpd.GeoSeries(crime_data_valid["point"].apply(Point))
LA_Neighborhood_map = LA_Neighborhood_map[LA_Neighborhood_map['geometry'].is_valid]
del crime_data, rent_data

crime_data_neiborhood = []
for geo in crime_data_geo:
    name = (LA_Neighborhood_map["name"])[LA_Neighborhood_map["geometry"].contains(geo)].values
    crime_data_neiborhood.append(name[0] if name.size else None)

crime_data_valid["Neighborhood"] = pd.Series(crime_data_neiborhood)
crime_data_valid.to_csv("data/processed_crime.csv")
rent_data_valid.to_csv("data/processed_rent.csv")


