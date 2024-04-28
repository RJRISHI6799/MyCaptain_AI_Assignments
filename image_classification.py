# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

# Load the digits dataset
digits = datasets.load_digits()

# Prepare the data
X = digits.data
y = digits.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Support Vector Machine (SVM) classifier
clf = svm.SVC(gamma=0.001)

# Train the classifier
clf.fit(X_train, y_train)

# Predict the labels for the test set
predicted = clf.predict(X_test)

# Evaluate the model
accuracy = metrics.accuracy_score(y_test, predicted)
print(f"Model Accuracy: {accuracy}")

# Visualize some test samples and their predicted labels
_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, prediction in zip(axes, X_test[:4], predicted[:4]):
    ax.set_axis_off()
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title(f"Prediction: {prediction}")

# Display the classification report
print(f"Classification report for classifier {clf}:\n{metrics.classification_report(y_test, predicted)}")