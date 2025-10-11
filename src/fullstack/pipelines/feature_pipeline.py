class FeaturePipeline:
    def __init__(self, config):
        self.config = config

    def fire(self):
        print("Data Loading, Preprocessing, Storing to feature store came here..")
