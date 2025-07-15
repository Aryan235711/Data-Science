from sklearn import  datasets
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

#Printing description and features and labels
print(iris.DESCR)

features = iris.data
labels = iris.target
print(features[0], labels[0])

# creating and training a classifier

cls = KNeighborsClassifier()
cls.fit(features, labels)

pred = cls.predict([[1,1,1,1]]) #Takes a double array as input
print(pred)