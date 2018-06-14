import csv

import numpy as np

import utils


def main():
    generate_csv([10, 20, 30], np.array([[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 5],
                                         [1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0],
                                         [1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0]]))


def generate_csv(galaxy_ids, y_pred):
    print(y_pred)
    print(utils.get_solutions_csv_header())

    with open(utils.get_my_solutions_csv_path(), 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(utils.get_solutions_csv_header())

        for index, y in enumerate(y_pred):
            line = [str(galaxy_ids[index])]
            for class_number, i in enumerate(utils.get_number_class_by_category()):
                for sub_class_number in range(i):
                    if y[class_number] == sub_class_number:
                        line.append("1")
                    else:
                        line.append("0")
            writer.writerow(line)


if __name__ == '__main__':
    main()
