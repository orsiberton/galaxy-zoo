import csv
import os
from concurrent.futures import ThreadPoolExecutor

from scipy import misc
from keras.applications.inception_v3 import InceptionV3
import utils
from keras import optimizers

"""

The first column of the features CSV is the galaxy ID.

"""

def main():
    extract_features(utils.get_training_images_pre_processed_path(), utils.get_training_features_path())
    extract_features(utils.get_test_images_pre_processed_path(), utils.get_test_features_path())

def extractor(procnum, image_path, image_name, model):
    print("{} - Extracting features for image {}".format(procnum, image_name))

    image = misc.imread(image_path)
    features = [int(image_name[:-4])]
    features.extend(model.predict(image).tolist())

    return features

def extract_features(images_path=None, output_filename=None):
    pool = ThreadPoolExecutor(max_workers=4)
    features = []
    workers = []

    model = cnn_model()

    i = 1
    for file in sorted(os.listdir(images_path)):
        image_path = images_path + "/" + file
        td = pool.submit(extractor, procnum=i, image_path=image_path, image_name=file, model=model)
        workers.append(td)
        i += 1

    for worker_index in range(len(workers)):
        features.append(workers[worker_index].result())

    with open(output_filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for feature in features:
            writer.writerow(feature)

def cnn_model():
    img_width, img_height = 175, 175

    # create the base pre-trained model
    base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=(img_width, img_height, 3))

    # Show a summary of the model. Check the number of trainable parameters
    base_model.summary()

    # Compile the model
    base_model.compile(loss='categorical_crossentropy',
                  optimizer=optimizers.RMSprop(lr=1e-4),
                  metrics=['acc'])

    return base_model

if __name__ == '__main__':
    main()
