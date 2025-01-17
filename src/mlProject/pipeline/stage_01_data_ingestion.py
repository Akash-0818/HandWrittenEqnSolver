from mlProject.components.data_ingestion import DataIngestion
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger



STAGE_NAME = "data ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_dataingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()

if __name__=="__main__":
    try:
        logger.info(f">>>>stage {STAGE_NAME} started")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>stage {STAGE_NAME} ended")
    except Exception as e:
        raise e
