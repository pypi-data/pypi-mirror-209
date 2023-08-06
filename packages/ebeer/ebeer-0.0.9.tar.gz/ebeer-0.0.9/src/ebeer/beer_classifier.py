import numpy as np
import tensorflow as tf

# from label_index import labels_index
from tensorflow import keras
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Dense, Flatten, Conv2D, MaxPooling2D)


class BeerClassifier:

    def __init__(self) -> None:
        pass

    def predict(self, path_img):

        width = 128
        height = 128
        size = (width, height)
        channels = 3
        n_neuronios_saida = 20
        learning_rate = 1e-4

        model = Sequential()

        # Extração de caracteristicas
        model.add(Conv2D(256, (3, 3), activation='relu',
                         input_shape=(width, height, channels)))
        model.add(MaxPooling2D((2, 2)))

        model.add(Conv2D(128, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2)))

        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2)))

        model.add(Conv2D(32, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2)))

        # Achatamento
        model.add(Flatten())

        # classificadores
        model.add(Dense(128, activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(n_neuronios_saida, activation='softmax'))

        model.compile(
            optimizer=Adam(learning_rate=learning_rate),
            loss='binary_crossentropy',
            metrics=[
                'accuracy',
                tf.keras.metrics.Precision(),
                tf.keras.metrics.Recall()
            ]
        )

        model = keras.models.load_model("src/trained_model/trained_model.h5")

        image_original = tf.keras.utils.load_img(
            path_img,
            grayscale=False,
            color_mode="rgb",
            target_size=None,
            interpolation="nearest"
        )

        image_resized = image_original.resize(size)

        image_prepared = np.expand_dims(image_resized, axis=0)

        predicted = model.predict(image_prepared)

        n_pos = predicted.argmax(axis=-1)[0]

        return n_pos
