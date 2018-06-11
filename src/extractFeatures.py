import os
from concurrent.futures import ThreadPoolExecutor

from scipy import misc
from skimage.feature import hog

import utils


def main():
    extract_features(utils.get_training_images_pre_processed_path(), 'training_features.csv')


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

        if i == 6:
            break

    for worker_index in range(len(workers)):
        features.append(workers[worker_index].result())

    print(features)
    # TODO save this features to a CSV with pandas


if __name__ == '__main__':
    main()
