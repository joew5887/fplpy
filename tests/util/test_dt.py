import pytest
from datetime import datetime
from fplpy.util.dt import string_to_datetime, datetime_to_string, date_to_string, time_to_string

@pytest.mark.parametrize("input_date,expected", [(datetime(2000, 2, 10, 9, 30, 00), "09:30 - Thu 10 February 2000")])
def test_datetime_to_string(input_date: datetime, expected: str) -> None:
    assert datetime_to_string(input_date) == expected


@pytest.mark.parametrize("input_str,expected", [("2000-02-10T09:30:00Z", datetime(2000, 2, 10, 9, 30, 00))])
def test_string_to_datetime(input_str: str, expected: datetime) -> None:
    assert string_to_datetime(input_str) == expected


@pytest.mark.parametrize("input_date,expected", [(datetime(2000, 2, 10), "Thu 10 February 2000")])
def test_date_to_string(input_date: datetime, expected: str) -> None:
    assert date_to_string(input_date) == expected


@pytest.mark.parametrize("input_date,expected", [(datetime(2000, 2, 10, 9, 30, 00), "09:30")])
def test_time_to_string(input_date: datetime, expected: str) -> None:
    assert time_to_string(input_date) == expected