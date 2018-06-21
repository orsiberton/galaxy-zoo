"""

http://scikit-learn.org/stable/modules/ensemble.html#forest
http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
http://scikit-learn.org/stable/modules/multiclass.html#multioutput-regression

"""
import csv

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier

import generateCSVAnswer
import utils


def main():
    classify_v1()
    classify_v2()


def classify_v1():
    """
    Method to classify images with 11 classifiers, one for each category and then,
    joins up everything in to the final answer.

    """
    galaxy_ids, features = read_features(utils.get_training_features_path())
    test_galaxy_ids, test_features = read_features(utils.get_test_features_path())

    y_pred = []
    for class_number in range(1, 12):
        y_pred.append(classify_class(class_number, features, test_features))

    # Creates an array [n_samples, number of classes] which each position is the answer for the given class
    y_pred = np.array(y_pred)
    y_pred = np.transpose(y_pred)

    generateCSVAnswer.generate_csv(test_galaxy_ids, y_pred)


def classify_v2():
    """
    Method to classify images based on a multiClass-multiLabel classifier.

    """
    galaxy_ids, features = read_features(utils.get_training_features_path())
    test_galaxy_ids, test_features = read_features(utils.get_test_features_path())

    y_pred = classify_class_multi_label(features, test_features)

    generateCSVAnswer.generate_csv(test_galaxy_ids, y_pred)


def read_y_true_for_all_classes():
    y_true = []
    for class_number in range(1, 12):
        y_true.append(read_y_true_for_class(utils.get_data_path() + "/Class{}.csv".format(class_number)))

    # Creates an array [n_samples, number of classes] which each position is the labeled data for the given class
    y_true = np.array(y_true)
    y_true = np.transpose(y_true)

    return y_true


def classify_class_multi_label(features, test_features):
    y_true = read_y_true_for_all_classes()

    # splits the train data into train and validation with validation being 20% of the original train data set
    x_train, x_validation, y_train, y_validation = train_test_split(features, y_true, test_size=0.20, random_state=0)

    classifier = MultiOutputClassifier(create_rf_classifier(240), n_jobs=-1)
    classifier.fit(x_train, y_train)

    y_true_transposed = np.transpose(y_true)
    y_pred_transposed = np.transpose(classifier.predict(features))

    for class_number in range(0, 11):
        score = accuracy_score(y_true_transposed[class_number], y_pred_transposed[class_number], normalize=True)
        print("Training score for Class {}: {:0.2f}".format(class_number + 1, score))

    return classifier.predict(test_features)


def classify_class(class_number, features, test_features):
    y_true = read_y_true_for_class(utils.get_data_path() + "/Class{}.csv".format(class_number))

    # splits the train data into train and validation with validation being 20% of the original train data set
    x_train, x_validation, y_train, y_validation = train_test_split(features, y_true, test_size=0.20, random_state=0)

    classifier = create_rf_classifier(240)
    classifier.fit(x_train, y_train)

    score = classifier.score(x_validation, y_validation)
    print("Training score for Class {}: {:0.2f}".format(class_number, score))
    return classifier.predict(test_features).tolist()


def read_features(file_path):
    galaxy_ids = []
    features = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        i = 0
        for line in reader:
            galaxy_ids.append(int(line[0]))
            features.append([float(feature) for feature in line[1:]])

            # TODO delete this
            # i += 1
            # if i == 1000:
            #     break

    return galaxy_ids, np.array(features)


def read_y_true_for_class(class_path):
    y_true = []
    i = 0
    with open(class_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # skip header
        for line in reader:
            y_true.append(int(line[1]))

            # TODO delete this
            # i += 1
            # if i == 1000:
            #     break

    return y_true


def create_rf_classifier(n_estimators, max_depth=9):
    return RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, n_jobs=-1)


if __name__ == '__main__':
    main()
