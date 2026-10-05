from pathlib import Path

import pandas as pd
from sklearn.metrics import roc_auc_score

SEED = 42

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

TARGET = "objetivo"
ID = "id_cliente"
MONTH = "mes"

TRAIN_MONTHS_MAX = 202610
VALID_MONTH = 202611


def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    train = pd.read_csv(RAW / "train.csv")
    test = pd.read_csv(RAW / "test.csv")
    sample = pd.read_csv(RAW / "sample_submission.csv")
    return train, test, sample


def temporal_split(train: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    fit = train[train[MONTH] <= TRAIN_MONTHS_MAX]
    valid = train[train[MONTH] == VALID_MONTH]
    return fit, valid


def gini(y_true, y_pred) -> float:
    return 2 * roc_auc_score(y_true, y_pred) - 1


def check_submission(submission: pd.DataFrame, test: pd.DataFrame) -> None:
    assert list(submission.columns) == [ID, "prediccion"], "columnas incorrectas"
    assert len(submission) == len(test), "numero de filas distinto al de test"
    assert (submission[ID].values == test[ID].values).all(), "ids u orden distintos al de test"
    assert submission["prediccion"].notna().all(), "hay NaN en prediccion"
    assert submission["prediccion"].between(0, 1).all(), "prediccion fuera de [0, 1]"
