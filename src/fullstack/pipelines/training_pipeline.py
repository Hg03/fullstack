class TrainingPipeline:
    def __init__(self, config):
        self.config = config

    def fire(self):
        print(
            "Loading features, Processing them for training, Training the model, Storing to feature and registering it.."
        )
