import tensorflow as tf
from tensorflow import keras
import numpy as np

def get_model():
    model_A = keras.models.Sequential() ##init model
    model_A.add(keras.layers.Flatten(input_shape=[28, 28])) ##input
    for n_hidden in (300, 100, 50, 50, 50):
        model_A.add(keras.layers.Dense(n_hidden, activation="relu")) ##adding layers
    model_A.add(keras.layers.Dense(8, activation="softmax")) ##final softmax
    return model_A

def get_dataset(flag):
    fashion_mnist = keras.datasets.fashion_mnist
    (X, y), (X_test, y_test) = fashion_mnist.load_data()
    X = X / 255.

    y_5_or_6 = (y == 5) | (y == 6)  # sandals or shirts
    y_A = y[~y_5_or_6]
    y_A[y_A > 6] -= 2  # class indices 7, 8, 9 should be moved to 5, 6, 7
    y_B = (y[y_5_or_6] == 6).astype(np.float32)  # binary classification task: is it a shirt (class 6)?
    X_A = X[~y_5_or_6]
    X_B = X[y_5_or_6]

    if flag == 'A':
        return X_A, y_A
    else:
        return X_B, y_B

def train_model_A():
    X_train_A, y_train_A = get_dataset('A')
    model_A = get_model()

    model_A.compile(loss="sparse_categorical_crossentropy",
                    optimizer=keras.optimizers.SGD(lr=1e-3),
                    metrics=["accuracy"])

    history = model_A.fit(X_train_A, y_train_A, epochs=20,
                          validation_split=0.2)

    model_A.save("my_model_A.h5")

def train_model_B():
    model_A = keras.models.load_model("my_model_A.h5") ##load model
    model_B_on_A = keras.models.Sequential(model_A.layers[:-1]) ##remove softmax layer
    model_B_on_A.summary()
    ##model_B_on_A.add(keras.layers.Dense(1, activation="sigmoid"))
train_model_B()
#train_model_A()