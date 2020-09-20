import tensorflow as tf
from tensorflow import keras

def get_model():
    model = keras.models.Sequential([
        keras.layers.Flatten(input_shape=[28, 28]),
        keras.layers.BatchNormalization(),
        keras.layers.Dense(300, activation='relu'),
        keras.layers.BatchNormalization(),
        keras.layers.Dense(100, activation='relu'),
        keras.layers.BatchNormalization(),
        keras.layers.Dense(10, activation='relu')
    ])
    return model

def analyse_model():
    model = get_model()
    model.summary()
    layer1 = model.layers[1].variables
    print([(var.name, var.trainable) for var in model.layers[1].variables])

analyse_model()