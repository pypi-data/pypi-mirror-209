import argparse
import os
import tarfile

import numpy as np
import pandas as pd
from six.moves import urllib
from sklearn.impute import SimpleImputer
from sklearn.model_selection import StratifiedShuffleSplit, train_test_split

from HousingPriceSP.logger import configure_logger

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("data", "raw")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


def income_cat_proportions(data):
    return data["income_cat"].value_counts() / len(data)


def split(housing):

    housing["income_cat"] = pd.cut(
        housing["median_income"],
        bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
        labels=[1, 2, 3, 4, 5],
    )
    train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    compare_props = pd.DataFrame(
        {
            "Overall": income_cat_proportions(housing),
            "Stratified": income_cat_proportions(strat_test_set),
            "Random": income_cat_proportions(test_set),
        }
    ).sort_index()
    compare_props["Rand. %error"] = (
        100 * compare_props["Random"] / compare_props["Overall"] - 100
    )
    compare_props["Strat. %error"] = (
        100 * compare_props["Stratified"] / compare_props["Overall"] - 100
    )

    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)

    return strat_train_set, strat_test_set


def preprocess(strat_train_set):
    housing = strat_train_set.copy()
    housing.plot(kind="scatter", x="longitude", y="latitude")
    housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)

    corr_matrix = housing.corr()
    corr_matrix["median_house_value"].sort_values(ascending=False)
    housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]
    housing["bedrooms_per_room"] = housing["total_bedrooms"] / housing["total_rooms"]
    housing["population_per_household"] = housing["population"] / housing["households"]

    housing = strat_train_set.drop(
        "median_house_value", axis=1
    )  # drop labels for training set
    housing_labels = strat_train_set["median_house_value"].copy()

    imputer = SimpleImputer(strategy="median")

    housing_num = housing.drop("ocean_proximity", axis=1)

    imputer.fit(housing_num)
    X = imputer.transform(housing_num)

    housing_tr = pd.DataFrame(X, columns=housing_num.columns, index=housing.index)
    housing_tr["rooms_per_household"] = (
        housing_tr["total_rooms"] / housing_tr["households"]
    )
    housing_tr["bedrooms_per_room"] = (
        housing_tr["total_bedrooms"] / housing_tr["total_rooms"]
    )
    housing_tr["population_per_household"] = (
        housing_tr["population"] / housing_tr["households"]
    )

    housing_cat = housing[["ocean_proximity"]]
    housing_prepared = housing_tr.join(pd.get_dummies(housing_cat, drop_first=True))
    return housing_prepared, housing_labels


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--log-level", type=str, default="DEBUG")
    parser.add_argument("--no-console-log", action="store_true")
    parser.add_argument("--log-path", type=str, default=os.getcwd() + "/logs/logs.log")
    parser.add_argument(
        "--datapath", help="path to store the dataset", type=str, default="/data/raw"
    )
    parser.add_argument(
        "--dataprocessed",
        help="path to store the dataset",
        type=str,
        default="/data/processed",
    )
    parser.add_argument(
        "--artifacts", help="path to store artifacts", type=str, default="artifacts"
    )

    args = parser.parse_args()
    logger = configure_logger(
        log_level=args.log_level,
        log_file=args.log_path,
        console=not args.no_console_log,
    )

    repo_path = os.getcwd()
    path = repo_path + args.datapath
    fetch_housing_data(housing_path=path)
    logger.debug(f"Fetched and saved housing data at {path}.")

    housing = load_housing_data(housing_path=path)
    logger.debug("Loaded housing data.")

    training_set, testing_set = split(housing)
    logger.debug("Splitted data into training and testing set.")

    train_x, train_y = preprocess(training_set)
    test_x, test_y = preprocess(testing_set)
    logger.debug("Preprossed housing dataset.")

    processed_path = repo_path + args.dataprocessed
    trainpath_x = os.path.join(processed_path, "train_x.csv")
    testpath_x = os.path.join(processed_path, "test_x.csv")
    trainpath_y = os.path.join(processed_path, "train_y.csv")
    testpath_y = os.path.join(processed_path, "test_y.csv")

    train_x.to_csv(trainpath_x, index=False)
    test_x.to_csv(testpath_x, index=False)
    train_y.to_csv(trainpath_y, index=False)
    test_y.to_csv(testpath_y, index=False)
    logger.debug(f"Saved preprossed train and test datasets at {processed_path}.")