from models.models import Dataset
from sklearn.model_selection import train_test_split


def test_train_splitter(dataset: Dataset, random_state=None) -> Dataset:
    train_partition, test_partition = train_test_split(
        dataset.df, test_size=0.2, random_state=random_state
    )

    dataset.partitions["test"] = test_partition
    dataset.partitions["train"] = train_partition

    return dataset


def cv_splitter(dataset: Dataset) -> Dataset:
    return dataset
