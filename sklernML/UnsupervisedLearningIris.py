# Importing Modules
from sklearn import datasets
import matplotlib.pyplot as plt

# Loading dataset
iris_dataset = datasets.load_iris()

# Available methods on dataset
print(dir(iris_dataset))

#Iris Data Contents
print(iris_dataset.data)

# Features
print(iris_dataset.feature_names)

# Targets
print(iris_dataset.target)

# Target Names, one color for each of the 3 types
print(iris_dataset.target_names)
label = {0: 'red', 1: 'blue', 2: 'green'}

# Dataset Slicing
x_axis = iris_dataset.data[:, 0]  # Sepal Length
y_axis = iris_dataset.data[:, 2]  # Sepal Width

# Plotting
plt.scatter(x_axis, y_axis, c=iris_dataset.target)
plt.ylabel('Sepal Width (cm)')
plt.xlabel('Sepal Length (cm)')
plt.show()

###########################

