
import numpy as np 
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
  
# Function importing Dataset 
def importdata(): 
    balance_data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer.data',sep=",") 
      
    # Printing the dataswet shape 
    print ("Dataset Length: ", len(balance_data)) 
    print ("Dataset Shape: ", balance_data.shape) 
      
    # Printing the dataset obseravtions 
    print ("Dataset: ",balance_data.head()) 
    return balance_data 
def splitdataset(balance_data): 
    X = balance_data.values[:, 0:8] 
    Y = balance_data.values[:, 9]  
    X_train, X_test, y_train, y_test = train_test_split(  
    X, Y, test_size = 0.5, random_state = 100) 
      
    return X, Y, X_train, X_test, y_train, y_test 

def train_using_gini(X_train, y_train): 
    
    print("bug", X_train[1:], y_train)
    clf_gini = DecisionTreeClassifier() 
    clf_gini.fit(X_train[1:], y_train) 
    return clf_gini 
def tarin_using_entropy(X_train, X_test, y_train): 
    clf_entropy = DecisionTreeClassifier( 
            criterion = "entropy", random_state = 100, 
            max_depth = 3, min_samples_leaf = 5) 

    clf_entropy.fit(X_train, y_train) 
    return clf_entropy 
def prediction(X_test, clf_object):  
    y_pred = clf_object.predict(X_test) 
    print("Predicted values:") 
    print(y_pred) 
    return y_pred 
def cal_accuracy(y_test, y_pred): 
      
    print("Confusion Matrix: ", 
        confusion_matrix(y_test, y_pred)) 
      
    print ("Accuracy : ", 
    accuracy_score(y_test,y_pred)*100) 
      
    print("Report : ", 
    classification_report(y_test, y_pred)) 
def main(): 
   
    data = importdata() 
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data) 
    print(X_train.shape, y_train.shape)
    print(X_train[:5])
    print(y_train[:5])
    clf_gini = train_using_gini(X_train, y_train) 
    clf_entropy = tarin_using_entropy(X_train, X_test, y_train) 

    print("Results Using Gini Index:") 
   
    y_pred_gini = prediction(X_test, clf_gini) 
    cal_accuracy(y_test, y_pred_gini) 
      
    print("Results Using Entropy:") 
    y_pred_entropy = prediction(X_test, clf_entropy) 
    cal_accuracy(y_test, y_pred_entropy) 
main() 

