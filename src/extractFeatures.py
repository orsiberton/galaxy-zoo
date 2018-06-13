import csv
import os
from concurrent.futures import ThreadPoolExecutor

from scipy import misc
from skimage.feature import hog

import utils

"""

The first column of the features CSV is the galaxy ID.

"""


def main():
    extract_features(utils.get_training_images_pre_processed_path(), utils.get_training_features_path())
    extract_features(utils.get_test_images_pre_processed_path(), utils.get_test_features_path())


def extractor(procnum, image_path, image_name):
    print("{} - Extracting features for image {}".format(procnum, image_name))

    image = misc.imread(image_path)
    features = [int(image_name[:-4])]
    features.extend(hog(image, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), block_norm='L2-Hys',
                        visualize=False, feature_vector=True, multichannel=True).tolist())

    return features


def extract_features(images_path=None, output_filename=None):
    pool = ThreadPoolExecutor(max_workers=8)
    features = []
    workers = []

    i = 1
    for file in sorted(os.listdir(images_path)):
        image_path = images_path + "/" + file
        td = pool.submit(extractor, procnum=i, image_path=image_path, image_name=file)
        workers.append(td)
        i += 1

    for worker_index in range(len(workers)):
        features.append(workers[worker_index].result())

    with open(output_filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for feature in features:
            writer.writerow(feature)


if __name__ == '__main__':
    main()
