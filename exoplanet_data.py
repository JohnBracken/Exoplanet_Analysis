import pandas as pd
from astropy.io.votable import parse
#import tkinter as tk
#import numpy as np
from matplotlib import pyplot as plt

import csv

def votable_to_pandas(votable_file):
    votable = parse(votable_file)
    table = votable.get_first_table().to_table(use_names_over_ids=True)
    return table.to_pandas()

exoplanet_table = votable_to_pandas("exoplanet_data.xml")

best_planets = []

with open('top_24_planets.csv') as top_planets:
    csvreader = csv.reader(top_planets)
    for row in csvreader:
        best_planets.extend(row)


best_exoplanet_table = exoplanet_table[exoplanet_table['pl_name'].isin(best_planets)]

new_index= list(range(1,(best_exoplanet_table.shape[0]+1)))
best_exoplanet_table.set_index(pd.Index(new_index),inplace = True)

print(best_exoplanet_table.agg({"pl_orbper":["min","max","median","mean","std"],
                                "pl_orbsmax":["min","max","median","mean","std"],
                                "pl_rade":["min","max","median","mean","std"],
                                "pl_bmasse":["min","max","median","mean","std"],
                                "pl_orbeccen":["min","max","median","mean","std"],
                                "pl_insol":["min","max","median","mean","std"],
                                "pl_eqt":["min","max","median","mean","std"],
                                "st_teff":["min","max","median","mean","std"],
                                "st_rad":["min","max","median","mean","std"],
                                "st_mass":["min","max","median","mean","std"],
                                "st_logg":["min","max","median","mean","std"],
                                "sy_dist":["min","max","median","mean","std"],
                                "sy_gaiamag":["min","max","median","mean","std"]}))

fig =plt.figure(figsize=(8,6))
planets = best_exoplanet_table['pl_name'][7:13].tolist()
distances = best_exoplanet_table['sy_dist'][7:13].tolist()
plt.bar(planets,distances)
plt.xlabel('Exoplanet')
plt.ylabel('Distance (parsecs)')
plt.xticks(fontsize=8)
plt.show()
