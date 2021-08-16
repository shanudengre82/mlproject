# tests/test_distance.py
from mlproject.distance import haversine

def test_distance_1():
    assert haversine(0, 0, 0, 0) == 0

def test_distance_2():
    assert round(haversine(48.865, 2.380, 48.235, 2.393)) == round(70.00696965697475)

def test_distance_3():
    assert type(haversine(48.865, 2.380, 48.235, 2.393)) == float
