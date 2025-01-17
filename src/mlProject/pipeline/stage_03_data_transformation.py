from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger



STAGE_NAME = "data transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_datatransformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.transform_and_save_data()
        print("Transformed and saved")

if __name__=="__main__":
    try:
        logger.info(f">>>>stage {STAGE_NAME} started")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>stage {STAGE_NAME} ended")
    except Exception as e:
        raise e
