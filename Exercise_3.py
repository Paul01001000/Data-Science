import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

towns = pd.read_json("c:\\Users\\paul8\\Downloads\\postcodes.json")

east = towns.loc[towns["longitude"] > 0, ["longitude","latitude"]]
west = towns.loc[towns["longitude"] < 0, ["longitude","latitude"]]
#greenwich = towns.loc[towns['town'] == "Greenwich", ["longitude","latitude"]]




plt.figure(figsize=(8,8), dpi=80)
plt.scatter(east['longitude'], east['latitude'],c="g")
plt.scatter(west['longitude'], west['latitude'],c="r")
plt.scatter(0,51.5,c="k",s=500)
plt.show()


