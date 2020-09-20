import  tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense

def get_pre_trained_mobilenet(num_classes=10):
    input_shape = (128, 128, 3)
    base_model = tf.keras.applications.mobilenet.MobileNet(weights='imagenet', input_shape=input_shape,
                                                          include_top=False)
    base_model.trainable = False

    model = tf.keras.Sequential([
        base_model,
        keras.layers.GlobalAveragePooling2D(),
        keras.layers.Dense(num_classes, activation='softmax')
    ])
    #model.summary()
    return model

get_pre_trained_mobilenet()
