from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline


try:
    # STAGE_NAME = "data ingestion stage"
    # logger.info(f">>>>stage {STAGE_NAME} started")
    # obj = DataIngestionTrainingPipeline()
    # obj.main()
    # logger.info(f">>>>stage {STAGE_NAME} ended")

    # STAGE_NAME = "data validation stage"
    # logger.info(f">>>>stage {STAGE_NAME} started")
    # obj = DataValidationTrainingPipeline()
    # obj.main()
    # logger.info(f">>>>stage {STAGE_NAME} ended")

    # STAGE_NAME = "data transformation stage"
    # logger.info(f">>>>stage {STAGE_NAME} started")
    # obj = DataTransformationTrainingPipeline()
    # obj.main()
    # logger.info(f">>>>stage {STAGE_NAME} ended")

    STAGE_NAME = "model trainer stage"
    logger.info(f">>>>stage {STAGE_NAME} started")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>stage {STAGE_NAME} ended")


except Exception as e:
    raise e