import pytest
import pandas as pd
from ml.model import train_model, compute_model_metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def test_train_model():
    """
    # Test the train model algorithm
    """
    X = pd.DataFrame({'test_feature1': [1, 3], 'test_feature2': [2, 4]})
    y = pd.Series([0, 1])
    model = train_model(X, y)
    assert isinstance(model, LogisticRegression)


def test_train_test_dataset_size():
    """
    # test that train_test_split returns correct dataset sizes
    """
    X = pd.DataFrame({'feature1': [1, 2, 3, 4, 5]})
    y = pd.Series([0, 1, 1, 0, 1])

    total_size = len(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    assert len(X_train) == int(0.8 * total_size)
    assert len(X_test) == int(0.2 * total_size)
    assert len(y_train) == int(0.8 * total_size)
    assert len(y_test) == int(0.2 * total_size)


def test_compute_model_metrics_value():
    """
    # Test if expected value is returned from the computing metrics function
    """
    y = pd.Series([0, 1, 1, 0])
    preds = pd.Series([0, 1, 0, 1])
    precision, recall, fbeta = compute_model_metrics(y, preds)
    expected_precision = 0.5
    expected_recall = 0.5
    expected_fbeta = 0.5
    assert precision == expected_precision
    assert recall == expected_recall
    assert fbeta == expected_fbeta