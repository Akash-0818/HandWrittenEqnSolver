# components
import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config

    def validate_data(self):
        data_locn = self.config.unzip_data_dir
        validation_status = True
        list_of_symbols = ['-','+','times','div','=','0','1','2','3','4','5','6','7','8','9']

        for symbol in os.listdir(data_locn):
            if symbol not in list_of_symbols:
                valdation_status = False
                break
            if len(os.listdir(os.path.join(data_locn,symbol)))<800:
                validation_status = False
                break
        
        return validation_status

