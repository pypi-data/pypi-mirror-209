import argparse
import os
import pickle

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error

from HousingPriceSP.logger import configure_logger


def get_data(path):
    prepared = pd.read_csv(path + "/test_x.csv")
    lables = pd.read_csv(path + "/test_y.csv")
    lables = lables.values.ravel()
    return prepared, lables


def score(model, x_test, y_test):
    loadModel = pickle.load(open(model, "rb"))
    predictions = loadModel.predict(x_test)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, predictions)
    return mse, rmse, mae


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
    data_path = repo_path + args.dataprocessed
    model_path = repo_path + args.artifacts

    x_test, y_test = get_data(data_path)

    mse, rmse, mae = score(os.path.join(model_path, "LinearRegression"), x_test, y_test)
    logger.debug(f"Linear Regression -> mse= {mse} , rmse= {rmse}, mae= {mae}")
    mse, rmse, mae = score(
        os.path.join(model_path, "DecisionTreeRegression"), x_test, y_test
    )
    logger.debug(f"Decision Tree Regression -> mse= {mse} , rmse= {rmse}, mae= {mae}")
    mse, rmse, mae = score(
        os.path.join(model_path, "RandomForestRegressor_RandomSearch"),
        x_test,
        y_test,
    )
    logger.debug(
        f"RandomForestRegressor RandomSearch -> mse= {mse} , rmse= {rmse}, mae= {mae}"
    )
    mse, rmse, mae = score(
        os.path.join(model_path, "randomForestRegressor_GridSearch"), x_test, y_test
    )
    logger.debug(
        f"RandomForestRegressor GridSearch -> mse= {mse} , rmse= {rmse}, mae= {mae}"
    )