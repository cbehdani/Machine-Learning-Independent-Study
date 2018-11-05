import xlrd
book = xlrd.open_workbook('HomePriceSizeDatasetCleaned.xlsx')
sheet = book.sheet_by_name('Sheet1')


baseline_size = [sheet.cell_value(r, 0) for r in range(sheet.nrows)]

size = [sheet.cell_value(r, 0) for r in range(sheet.nrows)]
print("next")
print(size)

house_price = [sheet.cell_value(r, 1) for r in range(sheet.nrows)]
print("next")
print(house_price)


# size = [sheet.cell_value(r, 3) for r in range(50)]
# print("next")
# print(size)
#
# house_price = [sheet.cell_value(r, 4) for r in range(50)]
# print("next")
# print(house_price)


# size = [sheet.cell_value(r, 6) for r in range(25)]
# print("next")
# print(size)
#
# house_price = [sheet.cell_value(r, 7) for r in range(25)]
# print("next")
# print(house_price)



#FIRST SET (100)########################################################################

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model, datasets

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

graph('regr.coef_*x + regr.intercept_', range(0, 4000))
plt.scatter(size, house_price, color='black')
plt.ylabel('house price (per 10,000 dollars)')
plt.xlabel('size of house (per 100 sq ft)')
plt.yticks([0, 50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000], ['0', '5', '10', '15', '20', '25', '30', '35', '40'])
plt.xticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000], ['0', '5', '10', '15', '20', '25', '30', '35', '40'])
plt.show()
# #####################################################################################
# while len(house_price) < 100:
#
#     size.append(baseline_size[len(size)])
#
#     tempPrice = int(size[len(size)-1])
#
#     house_price.append(regr.predict(tempPrice)[0])
#
#
# print("finished looping through")



# #####################################################################################
# determining price given a new size input and plotting it in red
size_new = 2265
print("predicted regression/home price is ", regr.predict([[size_new]])[0])

graph('regr.coef_*x + regr.intercept_', range(0, 4000))
plt.scatter(size, house_price, color='black')
plt.scatter(size_new, regr.predict([[size_new]])[0], color='red')
# plt.plot(size_new,regr.predict([[size_new]])[0])
plt.ylabel('house price (per 10,000 dollars)')
plt.xlabel('size of house (per 100 sq ft)')
# plt.yticks([0, 50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000], ['0', '5', '10', '15', '20', '25', '30', '35', '40'])
# plt.xticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000], ['0', '5', '10', '15', '20', '25', '30', '35', '40'])
plt.show()

