#-------------------------------------------------------------------------
# AUTHOR: Cyenadi Greene
# FILENAME: title of the source file
# SPECIFICATION: This program will read the file contact_lens.csv and output a decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: 1 hour 
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#encode the original categorical training features into numbers and add to the 4D array X.
#--> add your Python code here
for row in db:
    sample = []

    # Age
    if row[0] == "Young":
        sample.append(1)
    elif row[0] == "Prepresbyopic":
        sample.append(2)
    else:
        sample.append(3)

    # Spectacle
    if row[1] == "Myope":
        sample.append(1)
    else:
        sample.append(2)

    # Astigmatism
    if row[2] == "Yes":
        sample.append(1)
    else:
        sample.append(2)

    # Tear Production Rate
    if row[3] == "Normal":
        sample.append(1)
    else:
        sample.append(2)

    # Add feature row to X
    X.append(sample)

    #encode the original categorical training classes into numbers and add to the vector Y.
    if row[4] == "Yes":
        Y.append(1)
    else:
        Y.append(2)



# fitting the decision tree to the data using entropy as the impurity measure
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)

# plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], 
               class_names=['Yes','No'], filled=True, rounded=True)
plt.show()