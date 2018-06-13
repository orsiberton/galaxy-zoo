"""

http://scikit-learn.org/stable/modules/ensemble.html#forest
http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
http://scikit-learn.org/stable/modules/multiclass.html#multioutput-regression

"""
import csv

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

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

    # TODO do this for every class

    y_true = read_y_true_for_class(utils.get_data_path() + "/Class1.csv")

    print(galaxy_ids)
    print(features)
    print(features.shape)
    print(y_true)

    # splits the train data into train and validation with validation being 20% of the original train data set
    x_train, x_validation, y_train, y_validation = train_test_split(features, y_true, test_size=0.20, random_state=0)

    classifier = create_rf_classifier(240)
    classifier.fit(x_train, y_train)

    score = classifier.score(x_validation, y_validation)
    print("Training score: {0:0.2f}".format(score))

    """
    
    
    """

    return 0


def classify_v2():
    """
    Method to classify images based on a multiClass-multiLabel classifier.

    """
    return 0


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
            i += 1
            if i == 10000:
                break

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
            i += 1
            if i == 10000:
                break

    return y_true


def create_rf_classifier(n_estimators, max_depth=9):
    return RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)


if __name__ == '__main__':
    main()
