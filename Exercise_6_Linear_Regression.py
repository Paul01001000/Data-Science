import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

houses = pd.read_csv("c:\\Users\\paul8\\Downloads\\houses.csv")
"""
p5 = np.poly1d(np.polyfit(houses.living_space_size, houses.price, 5))
print(p5)
p4 = np.poly1d(np.polyfit(houses.living_space_size, houses.price, 4))
print(p4)
p3 = np.poly1d(np.polyfit(houses.living_space_size, houses.price, 3))
print(p3)

p2 = np.poly1d(np.polyfit(houses.living_space_size, houses.price, 2))
print(p2)

p20 = np.poly1d(np.polyfit(houses.living_space_size, houses.price, 20))
print(p20)
"""
p1 = np.poly1d(np.polyfit(houses.living_space_size, houses.price, 1))
print(p1)

range1 = range(100,460,10)
plt.scatter(houses.living_space_size, houses.price)
plt.plot([i for i in range1], [p1(i) for i in range1], c="r")
plt.show()

"""
n = 30
#pseudo code:
mae = sum(abs(houses.iloc[i].price - p20(houses.iloc[i].living_space_size)) for i in range(30)) / n
print(mae)
"""
predicted_prices = p1(houses.living_space_size)

MAE = np.mean(np.abs(houses.price - predicted_prices))
print(MAE)

#p4

print(p1(280))

houses_test = pd.read_csv("c:\\Users\\paul8\\Downloads\\houses_test.csv", header=None)
houses_test.columns = ['living_space_size','property_size','price']

predicted_prices_test = p1(houses_test.living_space_size)

#print(houses_test.price - predicted_prices_test)

err = np.mean(np.abs(houses_test.price - predicted_prices_test))
print(err)


#sklearn
from sklearn import linear_model

model = linear_model.LinearRegression()
x = houses.living_space_size.to_numpy().reshape(-1,1)
model.fit(x, houses.price)

print(model.coef_)
print(model.intercept_)

x_plot=np.arange(50,500,10)
x_plot=x_plot.reshape(-1,1)
y_predicted=model.predict(x_plot)

plt.figure()
plt.scatter(houses.living_space_size,houses.price)
plt.plot(x_plot,y_predicted,color='red')
plt.show()

test_x = houses_test.living_space_size.to_numpy().reshape(-1,1)
y_predicted = model.predict(test_x)

err = np.mean(np.abs(houses_test.price - y_predicted))
print(err)




