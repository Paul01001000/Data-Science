#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

stores = pd.read_csv("c:\\Users\\paul8\\Downloads\\stores.csv")
premium = stores.loc[stores['premium_store'] == 1]
normal = stores.loc[stores['premium_store'] == 0]


fig = plt.figure(figsize=(10,8), dpi=80)
plt.scatter(premium.latitude, premium.longitude, 
            c=premium.marketing_cost, 
            norm=mpl.colors.Normalize(1,3000), 
            cmap='RdYlGn_r', 
            s=premium.sales_volume)
plt.scatter(normal.latitude, normal.longitude,
            c=normal.marketing_cost, 
            norm=mpl.colors.Normalize(1,3000), 
            cmap='RdYlGn_r', 
            marker="h", 
            s=premium.sales_volume)
fig.show()