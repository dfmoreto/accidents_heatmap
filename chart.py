import numpy as np
import pandas as pd
import folium
from folium import plugins
from datetime import datetime

CSV_DIR = "./files"

heatmap = []
dates = []

for year in range(2017, 2020):
  pf_accidents = pd.read_csv(CSV_DIR + '/datatran' +str(year)+ '.csv', dtype=object, sep=';', encoding='iso-8859-1')

  date_array = [datetime(year, month, 1).strftime("%Y-%m") for month in range(1, 13) ]
  dates.extend(date_array)

  pf_accidents['latitude']  = pf_accidents['latitude'].astype(float)
  pf_accidents['longitude'] = pf_accidents['longitude'].astype(float)
  pf_accidents['feridos']   = pf_accidents['feridos'].astype(float)

  heatmap_data = pf_accidents[pf_accidents['uf'] == 'ES']
  heatmap_data = heatmap_data[heatmap_data['feridos'] > 0]
  heatmap_data = heatmap_data[['latitude', 'longitude', 'data_inversa']]

  heatmap_data = heatmap_data.dropna(axis = 0, subset = ['latitude', 'longitude'])
  heatmap_data = [[row['latitude'], row['longitude'], row['data_inversa']] for index, row in heatmap_data.iterrows()]

  for date in date_array:
    heatmap_array = [[row[0], row[1]] for row in heatmap_data if row[2][:-3] == date]
    if heatmap_array:
      heatmap.append(heatmap_array)
    else:
      dates.remove(date)


es_map = folium.Map(location = [-19.690729, -40.533432], zoom_start = 7.5)
hm = plugins.HeatMapWithTime(heatmap, index = dates)
hm.add_to(es_map)

es_map.save('index.html')