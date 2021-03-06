import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .5)

my_classifier = tree.DecisionTreeClassifier()
my_classifier.fit(x_train,y_train)

predict = my_classifier.predict(x_test)
print (accuracy_score(y_test,predict))







