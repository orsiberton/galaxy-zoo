def get_training_images_path():
    return "../data/images_training"


def get_training_images_pre_processed_path():
    return "../data/images_training_preprocessed"


def get_test_images_path():
    return "../data/images_test"


def get_test_images_pre_processed_path():
    return "../data/images_test_preprocessed"


def get_training_features_path():
    return "../data/training_features.csv"


def get_test_features_path():
    return "../data/test_features.csv"


def get_training_solution_csv_path():
    return "../data/training_solutions.csv"


def get_data_path():
    return "../data"


def get_number_class_by_category():
    return [3, 2, 2, 2, 4, 2, 3, 7, 3, 3, 6]


def get_solutions_csv_header():
    header = ["GalaxyID"]
    for class_number, i in enumerate(get_number_class_by_category()):
        for sub_class_number in range(i):
            header.append("Class{}.{}".format(class_number + 1, sub_class_number + 1))

    return header


def get_my_solutions_csv_path():
    return "my_solutions.csv"
