import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import os

def create_ml_models():
    if not os.path.exists('assets/ml'):
        os.makedirs('assets/ml')
    
    # Load data
    data = pd.read_csv("data/dataset_part_2.csv")
    X = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_3.csv')
    
    Y = data['Class'].to_numpy()
    transform = preprocessing.StandardScaler()
    X = transform.fit_transform(X)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
    
    results_file = open('assets/ml/results.txt', 'w')
    
    def plot_confusion_matrix(y, y_predict, name):
        cm = confusion_matrix(y, y_predict)
        plt.figure(figsize=(8,6))
        ax = plt.subplot()
        sns.heatmap(cm, annot=True, ax=ax, cmap='Blues')
        ax.set_xlabel('Predicted labels')
        ax.set_ylabel('True labels')
        ax.set_title(f'Confusion Matrix - {name}') 
        ax.xaxis.set_ticklabels(['Did not land', 'Landed'])
        ax.yaxis.set_ticklabels(['Did not land', 'Landed'])
        plt.savefig(f'assets/ml/confusion_matrix_{name}.png', bbox_inches='tight')
        plt.close()
        
    # 1. Logistic Regression
    parameters ={"C":[0.01,0.1,1],'penalty':['l2'], 'solver':['lbfgs']}
    lr = LogisticRegression()
    logreg_cv = GridSearchCV(lr, parameters, cv=10)
    logreg_cv.fit(X_train, Y_train)
    
    results_file.write(f"Logistic Regression Best Parameters: {logreg_cv.best_params_}\n")
    results_file.write(f"Logistic Regression Accuracy: {logreg_cv.best_score_}\n")
    
    # 2. SVM
    parameters = {'kernel':('linear', 'rbf','poly','rbf', 'sigmoid'),
              'C': np.logspace(-3, 3, 5),
              'gamma':np.logspace(-3, 3, 5)}
    svm = SVC()
    # Reduced CV to 5 for speed or use smaller grid if needed. Using 10 as per lab.
    svm_cv = GridSearchCV(svm, parameters, cv=10)
    svm_cv.fit(X_train, Y_train)
    
    results_file.write(f"SVM Best Parameters: {svm_cv.best_params_}\n")
    results_file.write(f"SVM Accuracy: {svm_cv.best_score_}\n")

    # 3. Decision Tree
    parameters = {'criterion': ['gini', 'entropy'],
         'splitter': ['best', 'random'],
         'max_depth': [2*n for n in range(1,10)],
         'max_features': ['auto', 'sqrt'],
         'min_samples_leaf': [1, 2, 4],
         'min_samples_split': [2, 5, 10]}
    tree = DecisionTreeClassifier()
    tree_cv = GridSearchCV(tree, parameters, cv=10)
    tree_cv.fit(X_train, Y_train)
    
    results_file.write(f"Decision Tree Best Parameters: {tree_cv.best_params_}\n")
    results_file.write(f"Decision Tree Accuracy: {tree_cv.best_score_}\n")

    # 4. KNN
    parameters = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
              'p': [1,2]}
    knn = KNeighborsClassifier()
    knn_cv = GridSearchCV(knn, parameters, cv=10)
    knn_cv.fit(X_train, Y_train)
    
    results_file.write(f"KNN Best Parameters: {knn_cv.best_params_}\n")
    results_file.write(f"KNN Accuracy: {knn_cv.best_score_}\n")
    
    # Plot comparisons
    accuracy_dict = {
        'Logistic Regression': logreg_cv.best_score_,
        'SVM': svm_cv.best_score_,
        'Decision Tree': tree_cv.best_score_,
        'KNN': knn_cv.best_score_
    }
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(accuracy_dict.keys()), y=list(accuracy_dict.values()))
    plt.ylabel("Accuracy", fontsize=20)
    plt.title("Model Accuracy Comparison", fontsize=20)
    plt.savefig('assets/ml/model_comparison.png', bbox_inches='tight')
    plt.close()
    
    # Confusion Matrices for best models on test data
    yhat_lr = logreg_cv.predict(X_test)
    plot_confusion_matrix(Y_test, yhat_lr, 'LogisticRegression')
    
    yhat_svm = svm_cv.predict(X_test)
    plot_confusion_matrix(Y_test, yhat_svm, 'SVM')
    
    yhat_tree = tree_cv.predict(X_test)
    plot_confusion_matrix(Y_test, yhat_tree, 'DecisionTree')
    
    yhat_knn = knn_cv.predict(X_test)
    plot_confusion_matrix(Y_test, yhat_knn, 'KNN')

    results_file.close()
    print("Machine Learning Analysis complete.")

if __name__ == "__main__":
    create_ml_models()
