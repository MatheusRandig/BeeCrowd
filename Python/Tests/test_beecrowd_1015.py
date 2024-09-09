from Python.Problems import beecrowd_1015

# check area rectangle triangle
def test_beginner1015_distance_points_km_one():
    result = beecrowd_1015.distance_points("1.0 7.0","5.0 9.0",4)
    assert result == "4.4721"

def test_beginner1015_distance_points_two():
    result = beecrowd_1015.distance_points("-2.5 0.4","12.1 7.3",4)
    assert result == "16.1484"

def test_beginner1015_distance_points_three():
    result = beecrowd_1015.distance_points("2.5 -0.4","-12.2 7.0",4)
    assert result == "16.4575"

