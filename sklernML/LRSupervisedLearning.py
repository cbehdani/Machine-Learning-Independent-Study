import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model, datasets

# inputted data(square footage of home size) and expected output(price)
size = [1300, 1700, 1750, 1875, 1050, 1575, 2250, 2550, 1425, 1730]
# size = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]
house_price = [235, 312, 289, 318, 193, 219, 425, 334, 329, 265]

# put each number of size into its own array for future formatting
sizeReformatted = np.array(size).reshape((-1, 1))

# creating the linear regression line
regr = linear_model.LinearRegression()
regr.fit(sizeReformatted, house_price)
print("Coefficient value of regression line is ", regr.coef_)
print("intercept value of regression line is ", regr.intercept_)
print("Equation would look like y=", regr.coef_[0] , "x+", regr.intercept_)

# #####################################################################################
# to plot the points and create the initial graph
def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x,y)

graph('regr.coef_*x + regr.intercept_', range(1000, 2700))
plt.scatter(size, house_price, color='black')
plt.ylabel('Home price (dollars)')
plt.xlabel('Size of Home(sq ft)')
plt.show()
# #####################################################################################
# determining price given a new size input and plotting it in red
size_new = 2265
print("predicted regression/home price is ", regr.predict([[size_new]])[0])

graph('regr.coef_*x + regr.intercept_', range(1000, 2700))
plt.scatter(size, house_price, color='black')
plt.scatter(size_new, regr.predict([[size_new]])[0], color='red')
# plt.plot(size_new,regr.predict([[size_new]])[0])
plt.ylabel('house price')
plt.xlabel('size of house')
plt.show()


# linear regression function
