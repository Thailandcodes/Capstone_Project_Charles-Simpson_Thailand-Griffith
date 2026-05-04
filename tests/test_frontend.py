import pytest
import pandas as pd
from unittest.mock import patch, Mock

mock_api_data = [
    {
        "id": 1,
        "country": "USA",
        "month": "January",
        "element": "Temperature",
        "year": 2000,
        "value": 23.5,
    },
    {
        "id": 2,
        "country": "Canada",
        "month": "February",
        "element": "Temperature",
        "year": 2005,
        "value": 12.3,
    },
]


@patch("requests.get")
def test_api_returns_data(mock_get):
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = mock_api_data

    import requests
    response = requests.get("fake_url")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_dataframe_creation():
    df = pd.DataFrame(mock_api_data)
    assert not df.empty
    assert "country" in df.columns


def test_year_filter():
    df = pd.DataFrame(mock_api_data)
    filtered = df[(df["year"] >= 2000) & (df["year"] <= 2000)]
    assert len(filtered) == 1
    assert filtered.iloc[0]["year"] == 2000


def test_country_filter():
    df = pd.DataFrame(mock_api_data)
    filtered = df[df["country"] == "USA"]
    assert len(filtered) == 1
    assert filtered.iloc[0]["country"] == "USA"


def test_invalid_country_filter():
    df = pd.DataFrame(mock_api_data)
    filtered = df[df["country"] == "Mars"]
    assert filtered.empty


def test_groupby_chart_data():
    df = pd.DataFrame(mock_api_data)
    grouped = df.groupby("year")["value"].mean()
    assert len(grouped) == 2
    assert 2000 in grouped.index


@patch("requests.get")
def test_api_failure(mock_get):
    mock_get.side_effect = Exception("API down")

    import requests

    with pytest.raises(Exception):
        requests.get("fake_url")


def test_required_columns():
    df = pd.DataFrame(mock_api_data)
    required = ["country", "month", "element", "year", "value"]

    for col in required:
        assert col in df.columns


def test_value_is_float():
    df = pd.DataFrame(mock_api_data)
    assert isinstance(df.iloc[0]["value"], float)


def test_empty_dataframe():
    df = pd.DataFrame([])
    assert df.empty
