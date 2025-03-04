import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axis3d
import numpy as np

data = pd.read_csv("C:/Users/paul8/Downloads/culster_spendings.csv")
#data.head()

for x in data.columns:
    data[x] /= np.max(data[x])

model = KMeans(n_clusters=2, random_state=42)
features = data[[x for x in data.columns]]
model.fit(features)
pred = model.predict(features)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(data.yearly_food_spending, 
        data.monthly_sepending_on_gardening_equipment,
        data.monthly_sepending_on_insurances,
        c=pred)

