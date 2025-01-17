from mlProject.components.data_validation import DataValidation
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger



STAGE_NAME = "data validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_datavalidation_config()
        data_validation = DataValidation(config=data_validation_config)
        validation_status = data_validation.validate_data()
        validation_msg = f"Validation status of data: {validation_status}"
        print(validation_msg)
        logger.info(validation_msg)
        with open(data_validation_config.status_file, 'w') as f:
            f.write(validation_msg)

if __name__=="__main__":
    try:
        logger.info(f">>>>stage {STAGE_NAME} started")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>stage {STAGE_NAME} ended")
    except Exception as e:
        raise e
