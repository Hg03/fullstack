class InferencePipeline:
    def __init__(self, config):
        self.config = config

    def fire(self):
        print("Take the features, take the model, serve the predictions..")
