import tensorflow as tf
from tensorflow import keras
import os
import time
import plot_tf_keras_history as plt_hist
root_logdir = os.path.join(os.curdir, "my_logs")

def get_run_logdir():
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join(root_logdir, run_id)

def get_model():
    model = keras.models.Sequential()
    model.add(keras.layers.Flatten(input_shape=[28, 28]))
    model.add(keras.layers.Dense(300, activation="relu"))
    model.add(keras.layers.Dense(100, activation="relu"))
    model.add(keras.layers.Dense(10, activation="softmax"))

    return model
def get_list_callbacks():
    run_logdir = get_run_logdir()
    tensorboard_cb = keras.callbacks.TensorBoard(run_logdir)
    checkpoint_cb = keras.callbacks.ModelCheckpoint("my_keras_model.h5", save_best_only=True)
    early_stopping_cb = keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)
    return [tensorboard_cb, checkpoint_cb, early_stopping_cb]

def train_valid_fashion_mnsit():
    fashion_mnist = keras.datasets.fashion_mnist
    (X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()
    X_train_full = X_train_full / 255.
    model = get_model()
    model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
    my_callbacks = get_list_callbacks()

    history = model.fit(X_train_full, y_train_full, epochs=2,
                        validation_split=0.2, callbacks=my_callbacks)

    plt_hist.plot_history(history)

    print('break')

train_valid_fashion_mnsit()