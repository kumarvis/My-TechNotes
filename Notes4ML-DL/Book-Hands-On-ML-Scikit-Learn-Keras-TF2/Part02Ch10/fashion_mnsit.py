import tensorflow as tf
from tensorflow import keras

def exp01():
    model = keras.models.Sequential()
    model.add(keras.layers.Flatten(input_shape=[28, 28]))
    model.add(keras.layers.Dense(300, activation="relu"))
    model.add(keras.layers.Dense(100, activation="relu"))
    model.add(keras.layers.Dense(10, activation="softmax"))



    layers = model.layers
    print(layers[0].name)
    print(len(layers))

def exp02():
    fashion_mnist = keras.datasets.fashion_mnist
    (X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()

    X_valid, X_train = X_train_full[:5000] / 255., X_train_full[5000:] / 255.
    y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
    X_test = X_test / 255.
    model = keras.models.Sequential()
    model.add(keras.layers.Flatten(input_shape=[28, 28]))
    model.add(keras.layers.Dense(300, activation="relu"))
    model.add(keras.layers.Dense(100, activation="relu"))
    model.add(keras.layers.Dense(10, activation="softmax"))
    #keras.utils.plot_model(model, "my_fashion_mnist_model.png", show_shapes=True)

    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer="sgd",
                  metrics=["accuracy"])

    #history = model.fit(X_train, y_train, epochs=30,
    #                    validation_data=(X_valid, y_valid))

    history = model.fit(X_train, y_train, epochs=30,
                        validation_split=0.2)

def exp03():
    input_A = keras.layers.Input(shape=[5], name="wide_input")
    input_B = keras.layers.Input(shape=[6], name="deep_input")
    hidden1 = keras.layers.Dense(30, activation="relu")(input_B)
    hidden2 = keras.layers.Dense(30, activation="relu")(hidden1)
    concat = keras.layers.concatenate([input_A, hidden2])
    output = keras.layers.Dense(1, name="output")(concat)
    model = keras.Model(inputs=[input_A, input_B], outputs=[output])
    model.summary()

exp03()