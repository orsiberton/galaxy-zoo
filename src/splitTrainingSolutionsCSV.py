import csv

import utils


def main():
    # Key to Galaxy ID
    image_name_key = 'GalaxyID'

    # All Classes Keys
    classes_allnames = [
        ['Class{}.{}'.format(i + 1, c + 1) for c in range(utils.get_number_class_by_category()[i])] for i in range(11)
    ]

    # Classes names for new generated csv files
    classes_names = tuple(['Class%d' % x for x in range(1, 12)])

    # Create csv writers
    file_objects = [open(utils.get_data_path() + '/' + classes_names[i] + '.csv', 'w') for i in range(0, 11)]
    csv_writer_dicts = [
        csv.DictWriter(file_objects[i], fieldnames=[image_name_key, classes_names[i]]) for i in range(0, 11)
    ]

    # Write headers in csv files
    for w in csv_writer_dicts:
        w.writeheader()

    # Open original csv readers
    original_csv = open(utils.get_training_solution_csv_path(), 'r')
    reader = csv.DictReader(original_csv)

    # Save csv files
    for row in reader:
        row_id = row[image_name_key]
        for i in range(11):
            values = [float(row[x]) for x in classes_allnames[i]]
            response = values.index(max(values))
            csv_writer_dicts[i].writerow({image_name_key: row_id, classes_names[i]: response})

    # Close all files
    for f in file_objects:
        f.close()
    original_csv.close()


if __name__ == '__main__':
    main()
