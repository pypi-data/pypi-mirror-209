import argparse
import os
import pickle

import pandas as pd
from scipy.stats import randint
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.tree import DecisionTreeRegressor

from HousingPriceSP.logger import configure_logger


def get_data(path):
    prepared = pd.read_csv(path + "/train_x.csv")
    lables = pd.read_csv(path + "/train_y.csv")
    lables = lables.values.ravel()
    return prepared, lables


def train(housing_prepared, housing_labels):
    lin_reg = LinearRegression()
    lin_reg.fit(housing_prepared, housing_labels)

    tree_reg = DecisionTreeRegressor(random_state=42)
    tree_reg.fit(housing_prepared, housing_labels)

    param_distribs = {
        "n_estimators": randint(low=1, high=200),
        "max_features": randint(low=1, high=8),
    }

    forest_reg = RandomForestRegressor(random_state=42)
    rnd_search = RandomizedSearchCV(
        forest_reg,
        param_distributions=param_distribs,
        n_iter=10,
        cv=5,
        scoring="neg_mean_squared_error",
        random_state=42,
    )
    rnd_search.fit(housing_prepared, housing_labels)

    param_grid = [
        # try 12 (3×4) combinations of hyperparameters
        {"n_estimators": [3, 10, 30], "max_features": [2, 4, 6, 8]},
        # then try 6 (2×3) combinations with bootstrap set as False
        {"bootstrap": [False], "n_estimators": [3, 10], "max_features": [2, 3, 4]},
    ]

    forest_reg = RandomForestRegressor(random_state=42)
    # train across 5 folds, that's a total of (12+6)*5=90 rounds of training
    grid_search = GridSearchCV(
        forest_reg,
        param_grid,
        cv=5,
        scoring="neg_mean_squared_error",
        return_train_score=True,
    )
    grid_search.fit(housing_prepared, housing_labels)

    return lin_reg, tree_reg, rnd_search, grid_search


def dump_model(model, output_path, filname):
    with open(os.path.join(output_path, filname), "wb") as p:
        pickle.dump(model, p)


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
        "--artifacts", help="path to store artifacts", type=str, default="/artifacts"
    )

    args = parser.parse_args()
    logger = configure_logger(
        log_level=args.log_level,
        log_file=args.log_path,
        console=not args.no_console_log,
    )

    repo_path = os.getcwd()
    input_path = repo_path + args.dataprocessed
    output_path = repo_path + args.artifacts

    x, y = get_data(input_path)
    logger.debug(f"Fetched training data from {input_path}.")
    logger.debug("Going to Run models...")
    lin_reg, tree_reg, forest_reg, grid_search = train(x, y)
    logger.debug("Training completed")
    models_name = [
        "LinearRegression",
        "DecisionTreeRegression",
        "RandomForestRegressor_RandomSearch",
        "randomForestRegressor_GridSearch",
    ]
    dump_model(lin_reg, output_path, models_name[0])
    dump_model(tree_reg, output_path, models_name[1])
    dump_model(forest_reg, output_path, models_name[2])
    dump_model(grid_search, output_path, models_name[3])
    logger.debug(f"All Models are saved at {output_path}.")