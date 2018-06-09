import os
from concurrent.futures import ThreadPoolExecutor

from scipy import misc, ndimage
from skimage import restoration

import utils


def main():
    pre_process_images(utils.get_training_images_path(), utils.get_training_images_pre_processed_path())
    pre_process_images(utils.get_test_images_path(), utils.get_test_images_pre_processed_path())


def pre_process_images(root_dir=None, pre_processed_dir=None):
    if not os.path.exists(pre_processed_dir):
        os.mkdir(pre_processed_dir)

    pool = ThreadPoolExecutor(max_workers=8)
    workers = []
    for file in os.listdir(root_dir):
        if file[-4:] == ".jpg":
            pre_process_image(file, root_dir, pre_processed_dir)
            td = pool.submit(pre_process_image, file=file, root_dir=root_dir, pre_processed_dir=pre_processed_dir)
            workers.append(td)

    for worker_index in range(len(workers)):
        workers[worker_index].result()


def pre_process_image(file, root_dir, pre_processed_dir):
    # Open image
    image = misc.imread(root_dir + "/" + file)

    # Crop the center of the image
    cropped_image = crop_center(image, 175, 175)

    # Enhance edges of the galaxy
    image_edge = misc.imfilter(cropped_image, 'edge_enhance_more')

    # Filter image
    image_filtered = ndimage.percentile_filter(image_edge, 10, 2)

    # Denoise Image
    image_denoised = restoration.denoise_tv_chambolle(image_filtered, weight=0.1, multichannel=True)

    misc.imsave(pre_processed_dir + "/" + file, image_denoised)
    print("Image {} pre processed.".format(file))


def crop_center(img, cropx, cropy):
    y, x, _ = img.shape
    startx = x // 2 - (cropx // 2)
    starty = y // 2 - (cropy // 2)
    return img[starty:starty + cropy, startx:startx + cropx]


if __name__ == '__main__':
    main()
