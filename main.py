from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "data ingestion stage"
try:
    logger.info(f">>>>stage {STAGE_NAME} started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>stage {STAGE_NAME} ended")

    logger.info(f">>>>stage {STAGE_NAME} started")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>stage {STAGE_NAME} ended")
except Exception as e:
    raise e