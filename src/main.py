import classifiers
import extractFeatures
import preProcessImage
import splitTrainingSolutionsCSV


def main():
    # First solution with default extractors like HOG and 11 classifiers
    preProcessImage.main()
    extractFeatures.main()
    splitTrainingSolutionsCSV.main()
    classifiers.classify_v1()

    # Second solution with features extracted by a DNN and MultiClass-MultiLabel classifier
    # TODO


if __name__ == '__main__':
    main()
