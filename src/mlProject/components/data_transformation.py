# components
import os
from mlProject import logger
import numpy as np
from sklearn.model_selection import train_test_split
import cv2
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config

    def transform_and_save_data(self):

        data_locn = self.config.data_path
        data = []
        labels = []
        labels_d = {str(i): i for i in range(10)}
        labels_d['+'] = 10
        labels_d['-'] = 11
        labels_d['x'] = 12
        labels_d['d'] = 13

        for symbol in os.listdir(data_locn):
            symbolpath = os.path.join(data_locn, symbol)

            for file in os.listdir(symbolpath):
                img = cv2.imread(os.path.join(symbolpath,file))
                img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                img = cv2.resize(img, (500,500))
                data.append(img)
                labels.append(labels_d[symbol])
        
        data_array = np.array(data)
        labels_array = np.array(labels)

        train_data, test_data, train_labels, test_labels = train_test_split(data_array, labels_array, test_size=0.1)

        np.save(self.config.train_data_path, train_data)
        np.save(self.config.train_labels_path, train_labels)
        np.save(self.config.test_data_path, test_data)
        np.save(self.config.test_labels_path, test_labels)

