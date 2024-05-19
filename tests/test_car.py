import pytest
from olympus_calculator.car import calculate_car_depreciation


def test_car_depreciation_0_years_0_mileage():
    car_price = 100
    driven_years = 0
    driven_km = 0
    depriciated_value = calculate_car_depreciation(car_price, driven_years, driven_km)
    assert depriciated_value == 100


@pytest.mark.parametrize(
    "car_price, driven_years, expected_value",
    [(100, 1, 90), (100, 2, 81), (100, 3, 72.9)],
)
def test_car_depreciation_for_age(car_price, driven_years, expected_value):
    driven_km = 0
    depriciated_value = calculate_car_depreciation(car_price, driven_years, driven_km)
    assert depriciated_value == pytest.approx(expected_value, rel=1e-2)


@pytest.mark.parametrize(
    "car_price, driven_km, expected_value",
    [(100, 50000, 85), (100, 100000, 72.25), (100, 150000, 61.41)],
)
def test_car_depreciation_for_mileage(car_price, driven_km, expected_value):
    """
    the car's value should be reduced by 15% for each 50000 km driven
    """
    driven_years = 0
    depriciated_value = calculate_car_depreciation(car_price, driven_years, driven_km)
    assert depriciated_value == pytest.approx(expected_value, rel=1e-2)


# the function should ask for the car's price, the number of years of the usage and for the total number of kilometers
# the function should return the car's depreciated value
# when the year is 0, the car's value should be the same as the price
# the car value should be reduced by 10% each year
# the car's value should be reduced by 15% for each 50000 km
