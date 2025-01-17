# components 
import os
from pathlib import Path
import zipfile
from urllib import request
from mlProject import logger
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.utils.common import get_size

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            print(self.config.source_URL)
            print(self.config.local_data_file)
            filename, headers = request.urlretrieve(url=self.config.source_URL, filename=self.config.local_data_file)
            logger.info(f"{filename} downloaded with info: {headers}")
        else:
            logger.info(f"{filename} already exists! size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
