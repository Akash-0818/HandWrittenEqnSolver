from mlProject.constants import *
from mlProject.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelTrainerConfig
from mlProject.utils.common import read_yaml, create_directories

# config manager 
class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH, schema_filepath = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_dataingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir, 
            source_URL= config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_datavalidation_config(self):
        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            status_file=config.status_file
        )

        return data_validation_config

    def get_datatransformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            train_data_path=config.train_data_path,
            train_labels_path=config.train_labels_path,
            test_data_path=config.test_data_path,
            test_labels_path=config.test_labels_path
        )

        return data_transformation_config
    
    def get_modeltrainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            train_labels_path=config.train_labels_path,
            test_data_path=config.test_data_path,
            test_labels_path=config.test_labels_path,
            model_name=config.model_name
        )

        return model_trainer_config