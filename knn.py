import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import math


iris = pd.read_csv('iris.csv')
X_train, X_test = train_test_split(iris, test_size=30, train_size=70, random_state=42)

iris_nospec = iris.iloc[:,:-1]
print(iris_nospec)
q=[5.1, 3.8, 2.0, 0.5]
p = iris_nospec.iloc[1]
print(p)
print
#for i in len(X_train):
    #p = [iris]
   # math.dist()

