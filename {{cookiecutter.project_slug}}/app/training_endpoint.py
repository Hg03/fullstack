from {{cookiecutter.project_slug}}.pipelines.feature_pipeline import FeaturePipeline
from {{cookiecutter.project_slug}}.pipelines.training_pipeline import TrainingPipeline
from omegaconf import DictConfig
import hydra


def make_features(config: DictConfig) -> None:
    FeaturePipeline(config=config).fire()


def train_features(config: DictConfig) -> None:
    TrainingPipeline(config=config).fire()


@hydra.main(config_path="../conf", config_name="config", version_base=None)
def main(cfg: DictConfig) -> None:
    make_features(config=cfg)
    train_features(config=cfg)


if __name__ == "__main__":
    main()
