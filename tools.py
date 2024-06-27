import numpy as np
import os
import pathlib
# import tensorflow as tf

data_dir = pathlib.Path('tflite/images')
BATCH_SIZE = 32
IMG_HEIGHT = 224
IMG_WIDTH = 224
IMG_SHAPE = (IMG_HEIGHT, IMG_WIDTH, 3)
CLASS_NAMES = np.array([item.name for item in data_dir.glob('train/*') if item.name != "LICENSE.txt"])


# def get_label(file_path):
#   parts = tf.strings.split(file_path, os.path.sep)
#   return parts[-2] == CLASS_NAMES[0]

# def decode_img(img):
#   img = tf.image.decode_jpeg(img, channels=3)
#   img = tf.image.convert_image_dtype(img, tf.float32)
#   return tf.image.resize(img, [IMG_WIDTH, IMG_HEIGHT])

# def process_path(file_path):
#   label = get_label(file_path)
#   img = tf.io.read_file(file_path)
#   img = decode_img(img)
#   return img, label

# def format_image(image, label):
#     image = tf.image.resize(image, IMAGE_SIZE) / 255.0
#     return  image, label


print('Utility methods loaded!')