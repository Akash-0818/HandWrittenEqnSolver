# components
import os
from mlProject import logger
import numpy as np
from sklearn.model_selection import train_test_split
import cv2
from mlProject.entity.config_entity import DataTransformationConfig
from keras._tf_keras.keras.utils import to_categorical

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
        self.labels_d = {str(i): i for i in range(10)}
        self.labels_d['+'] = 10
        self.labels_d['-'] = 11
        self.labels_d['times'] = 12
        self.labels_d['div'] = 13
        self.labels_d['='] = 14

    def preprocess(self, datapath, symbol):
        data = []
        target = []
        ctr = 0
        symbolpath = os.path.join(datapath, symbol)

        for f in os.listdir(symbolpath):
            try:
                ctr += 1
                if ctr > 800:
                    break
                imgpath = os.path.join(symbolpath,f)
                img = cv2.imread(imgpath)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = np.array(img)
                img = np.reshape(img, (45,45,1))
                data.append(img)
                target.append(self.labels_d[symbol])
            except Exception as e:
                print("symbol: ", symbol)
                print("symbol type: ", type(symbol))
                print("filepath: ", imgpath)
                print(e)

        data = np.array(data)
        target = np.array(target)
        return data, target

    def transform_and_save_data(self):

        data_locn = self.config.data_path
        data, target = [], []

        for symbol in os.listdir(data_locn):
            dt, tt = self.preprocess(data_locn, symbol)
            data.extend(dt)
            target.extend(tt)
            print(f"done for {symbol}")

        data = np.array(data)
        target = np.array(target)
        target = to_categorical(target)

        xTrain, xTest, yTrain, yTest = train_test_split(data, target, test_size=0.1)

        # print("\ntrain data shape: ", xTrain.shape)
        # print("train target shape: ", yTrain.shape)
        # print("test data shape: ", xTest.shape)
        # print("test target shape: ", yTest.shape)
        
        np.save(self.config.train_data_path, xTrain)
        np.save(self.config.train_labels_path, yTrain)
        np.save(self.config.test_data_path, xTest)
        np.save(self.config.test_labels_path, yTest)

