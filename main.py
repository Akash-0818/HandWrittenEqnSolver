from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "data ingestion stage"
try:
    logger.info(f">>>>stage {STAGE_NAME} started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>stage {STAGE_NAME} ended")
except Exception as e:
    raise e