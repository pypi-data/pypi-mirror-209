from ingestion.ingestion_pipeline import Ingestion
from model_selection.splitters import test_train_splitter
from preprocessing.time.date_processor import date_processor
from preprocessing.time.duration import duration_builder
from regression.models.randomforest.randomforest import (  # noqa
    RandomForestRegressionRunner,
)
from sklearn.metrics import mean_absolute_error


class LazyLearner:
    def __init__(self, random_state=None):
        self.dataset = None
        self.task = None
        self.models = None
        self.leaderboard = None
        self.random_state = random_state
        self.target = None

    def create_project(self, data, target, task="infer"):
        # ingest data
        self.target = target
        self.dataset = Ingestion().run(data)

        if task == "infer":
            # if target is numeric then regression, else classification
            if self.dataset.column_type_map[target] == "numeric":
                self.task = "regression"
            else:
                self.task = "classification"

        # process dates

        self.dataset = date_processor(self.dataset)
        self.dataset = duration_builder(self.dataset)

        # split partitions

        self.dataset = test_train_splitter(
            self.dataset, random_state=self.random_state
        )  # noqa

        # set modelling configurations

    def run_autopilot(self):
        """
        TODO: Everything here must be abstracted away into strategies
        TODO: such that several models are run and their scores are added to
        TODO: the leaderboard

        :return:
        """

        simple_random_forest = RandomForestRegressionRunner(
            target=self.target,
            dataset=self.dataset,
            random_state=self.random_state,  # noqa
        )
        simple_random_forest.fit()

        # get holdout scores
        simple_random_forest.predict(self.dataset.partitions["test"])
        simple_random_forest.pipeline.holdout_score = mean_absolute_error(
            self.dataset.partitions["test"][self.target],
            simple_random_forest.pipeline.tmp_pred,
        )
        return simple_random_forest
