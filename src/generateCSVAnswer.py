import csv

import numpy as np

import utils


def main():
    generate_csv([10, 20, 30], np.array([[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 5],
                                         [1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0],
                                         [1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0]]))


def generate_csv(galaxy_ids, y_pred):
    print("Generating csv with answers")
    with open(utils.get_my_solutions_csv_path(), 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(utils.get_solutions_csv_header())

        for index, y in enumerate(y_pred):
            line = calculate_classes(galaxy_ids, index, y)
            writer.writerow(line)


def calculate_classes(galaxy_ids, index, y):
    normalize = True
    line = [str(galaxy_ids[index])]
    if normalize:
        norm_y_list = handle_classes(y, utils.get_number_class_by_category())
        for norm_y in norm_y_list:
            line.append(str(norm_y))

    else:
        for class_number, i in enumerate(utils.get_number_class_by_category()):
            for sub_class_number in range(i):
                if y[class_number] == sub_class_number:
                    line.append("1")
                else:
                    line.append("0")
    return line


def handle_classes(y_pred, number_class_by_category):
    y = [0 for _ in range(sum(number_class_by_category))]

    return handle_class_1(y, y_pred)


def handle_class_1(y, y_pred):
    y[y_pred[0]] = 1

    if y_pred[0] == 0:
        # Go to class 7
        y = handle_class_7(y, y_pred)
    elif y_pred[0] == 1:
        # Go to class 2
        y = handle_class_2(y, y_pred)
    elif y_pred[0] == 2:
        # End
        return y

    return y


def handle_class_2(y, y_pred):
    index = 3

    y[index + y_pred[1]] = 1

    if y_pred[1] == 0:
        # Go to class 9
        y = handle_class_9(y, y_pred)
    elif y_pred[1] == 1:
        # Go to class 3
        y = handle_class_3(y, y_pred)

    return y


def handle_class_3(y, y_pred):
    index = 5

    y[index + y_pred[2]] = 1

    y = handle_class_4(y, y_pred)

    return y


def handle_class_4(y, y_pred):
    index = 7

    y[index + y_pred[3]] = 1

    if y_pred[3] == 0:
        # Go to class 10
        y = handle_class_10(y, y_pred)
    elif y_pred[3] == 1:
        # Go to class 5
        y = handle_class_5(y, y_pred)

    return y


def handle_class_5(y, y_pred):
    index = 9

    y[index + y_pred[4]] = 1

    y = handle_class_6(y, y_pred)

    return y


def handle_class_6(y, y_pred):
    index = 13

    y[index + y_pred[5]] = 1

    if y_pred[5] == 0:
        # Go to class 8
        y = handle_class_8(y, y_pred)
    elif y_pred[5] == 1:
        # End
        return y

    return y


def handle_class_7(y, y_pred):
    index = 15

    y[index + y_pred[6]] = 1

    y = handle_class_6(y, y_pred)

    return y


def handle_class_8(y, y_pred):
    index = 18

    y[index + y_pred[7]] = 1

    return y


def handle_class_9(y, y_pred):
    index = 25

    y[index + y_pred[8]] = 1

    y = handle_class_6(y, y_pred)

    return y


def handle_class_10(y, y_pred):
    index = 28

    y[index + y_pred[9]] = 1

    y = handle_class_11(y, y_pred)

    return y


def handle_class_11(y, y_pred):
    index = 31

    y[index + y_pred[10]] = 1

    y = handle_class_5(y, y_pred)

    return y


if __name__ == '__main__':
    main()
