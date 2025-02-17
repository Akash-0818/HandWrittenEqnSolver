from mlProject.components.model_trainer import ModelTrainer
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger



STAGE_NAME = "model trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_modeltrainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train_model()
        print("Model Trained")

if __name__=="__main__":
    try:
        logger.info(f">>>>stage {STAGE_NAME} started")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>stage {STAGE_NAME} ended")
    except Exception as e:
        raise e
