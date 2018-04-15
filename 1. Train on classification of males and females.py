from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)

print "Trained Decision tree"

pred_tree = clf.predict(X)
acc_tree = accuracy_score(Y,pred_tree)*100
print ("The Accuracy is : {}".format(acc_tree))

# CHALLENGE compare their results and print the best one!

#Added 3 more clssifiers

from sklearn.svm import LinearSVC
clf = LinearSVC(random_state=0)
clf = clf.fit(X, Y)

print "Trained Liner SVC"
pred_tree = clf.predict(X)
acc_tree = accuracy_score(Y,pred_tree)*100
print ("The Accuracy is : {}".format(acc_tree))

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
clf = clf.fit(X, Y)

print "Trained K neighborClassifier"
pred_tree = clf.predict(X)
acc_tree = accuracy_score(Y,pred_tree)*100
print ("The Accuracy is : {}".format(acc_tree))

from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
clf = QuadraticDiscriminantAnalysis()
clf = clf.fit(X,Y)
print ("Trained QuadraticDiscriminant Analysis")
pred_tree = clf.predict(X)
acc_tree = accuracy_score(Y,pred_tree)*100
print ("The Accuracy is : {}".format(acc_tree))



