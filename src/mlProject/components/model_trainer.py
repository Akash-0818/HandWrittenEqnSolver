# components
import os
from mlProject import logger
import numpy as np
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras._tf_keras.keras.utils import to_categorical
import joblib

from mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config

    def train_model(self):
        train_data = np.load(self.config.train_data_path)
        train_labels = np.load(self.config.train_labels_path)

        test_data = np.load(self.config.test_data_path)
        test_labels = np.load(self.config.test_labels_path)

        model = Sequential()
        model.add(Conv2D(128, (3,3), input_shape=(45,45,1), activation="relu"))
        model.add(MaxPooling2D((2,2)))
        model.add(Conv2D(64, (3,3), activation="relu"))
        model.add(MaxPooling2D((2,2)))
        model.add(Flatten())
        model.add(Dense(32, activation="relu"))
        model.add(Dense(15, activation="softmax"))

        model.compile(loss="categorical_crossentropy",optimizer="adam", metrics=['acc'])

        h = model.fit(train_data, train_labels, epochs=15, batch_size=16, validation_data=(test_data,test_labels))
        
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))        


