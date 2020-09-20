import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
from get_model import get_pre_trained_mobilenet
from plot_tf_keras_history import plot_history
from sklearn.model_selection import train_test_split
import scipy
import numpy as np
from PIL import Image
import skimage

def get_dataset():
    (X_train_full, y_train_full), (X_test, y_test) = keras.datasets.cifar10.load_data()
    new_shape = (128, 128, 3)
    X_new = np.empty(shape=(X_train_full.shape[0],) + new_shape)

    for idx in range(X_train_full.shape[0]):
        image = X_train_full[idx]
        X_new[idx] = skimage.transform.resize(image, new_shape)

    X_new = X_new / 255.
    X_test = X_test / 255.
    return X_new, y_train_full

def train_model():
    num_classes = 10
    batch_sz = 2
    data, labels = get_dataset()
    X_train, X_valid, ytrain, yvalid = train_test_split(data, labels, test_size=0.2,
                                                      random_state=42)


    custom_model = get_pre_trained_mobilenet(num_classes)
    lr = 1e-5
    optimizer = tf.keras.optimizers.Adam(learning_rate=lr)

    custom_model.compile(loss="sparse_categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])
    history = custom_model.fit(x=X_train, y=ytrain, batch_size=batch_sz, epochs=10,
                               validation_data=(X_valid, yvalid))

    plot_history(history)

train_model()