
import pytest
from customer_validation import validate_customer


def test_tc01():
    assert validate_customer(101, "Ravi", 25) == "Valid"


def test_tc02():
    assert validate_customer(-1, "Ravi", 25) == "Invalid"


def test_tc03():
    assert validate_customer(102, "", 30) == "Invalid"


def test_tc04():
    assert validate_customer(103, "Kumar", -5) == "Invalid"


def test_tc05():
    assert validate_customer(104, "Suresh", 40) == "Valid"
