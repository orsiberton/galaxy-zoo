import classifiers
import extractFeatures
import preProcessImage
import splitTrainingSolutionsCSV


def main():
    preProcessImage.main()
    splitTrainingSolutionsCSV.main()

    # First solution with default extractors like HOG and 11 classifiers
    extractFeatures.main()
    classifiers.classify_v1()

    # Second solution with features extracted by a DNN and MultiClass-MultiLabel classifier
    extractFeatures.main()  # TODO change this to CNN when it's ready
    classifiers.classify_v2()


if __name__ == '__main__':
    main()
