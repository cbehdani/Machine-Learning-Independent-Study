#Cameron Behdani
# ITCS 6880 - Independent Study - Machine Learning - Unsupervised Machine Learning Algorithm

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
from sklearn import datasets

#Implementing housing data
import xlrd
book = xlrd.open_workbook('HomePriceSizeDatasetCleaned.xlsx')
sheet = book.sheet_by_name('Sheet1')

# x = [sheet.cell_value(r, 0) for r in range(sheet.nrows)]
# y = [sheet.cell_value(r, 1) for r in range(sheet.nrows)]

iris_dataset = datasets.load_iris()
x = iris_dataset.data[:, 0]  # Sepal Length
y = iris_dataset.data[:, 2]  # Sepal Width
# z = [None] * len(x)

# X = np.column_stack((x,y,z))
X = np.column_stack((x,y))
#


# datapoints to plot
# x = [3, 4, 8.8, 9.1, 0, 7]
# y = [2, 3, 9, 7.3, .5, 7]
plt.scatter(x,y)
plt.show()

# convert dataset to workable numpy array

# X = np.array([[3,2],[4,3],[8.8,9],[9.1,7.3],[0,0.5], [7, 7]])

################################################################

# give the number of clusters that will be used
kmeans_model = KMeans(n_clusters=3)

#training method to set center of cluster based off input data
kmeans_model.fit(X)

#setting up data visualization
centroids = kmeans_model.cluster_centers_
labels = kmeans_model.labels_
print("centroids\n", centroids)
print("labels\n", labels)
# colors for each type of cluster
colors = ["y.", "b.", "r."]

# plotting points and centers of cluster
for i in range(len(X)):
    print ("coordinate:",X[i],"label:",labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
    # X[i,2] = labels[i]

plt.scatter(centroids[:, 0], centroids[:,1], marker = "x", s=150, linewidths = 5, zorder = 10)
plt.ylabel('Sepal Width (cm)')
plt.xlabel('Sepal Length (cm)')
plt.show()