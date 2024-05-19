import pytest
from olympus_calculator.car import calculate_car_depreciation


def test_car_depreciation_0_years_0_mileage():
    # Given
    car_price = 100
    driven_years = 0
    driven_km = 0

    # When
    depriciated_value = calculate_car_depreciation(car_price, driven_years, driven_km)

    # Then
    assert depriciated_value == 100


@pytest.mark.parametrize(
    "car_price_parameter, driven_years_parameter, expected_value",
    [(100, 1, 90), (100, 2, 81), (100, 3, 72.9)],
)
def test_car_depreciation_for_age(
    car_price_parameter, driven_years_parameter, expected_value
):
    """
    the car's value should be reduced by 10% each year
    """
    # Given
    driven_km = 0
    car_price = car_price_parameter
    driven_years = driven_years_parameter

    # When
    depriciated_value = calculate_car_depreciation(car_price, driven_years, driven_km)

    # Then
    assert depriciated_value == pytest.approx(expected_value, rel=1e-2)


@pytest.mark.parametrize(
    "car_price_parameter, driven_km_parameter, expected_value",
    [(100, 50000, 90), (100, 100000, 81), (100, 150000, 72.9)],
)
def test_car_depreciation_for_mileage(
    car_price_parameter, driven_km_parameter, expected_value
):
    """
    the car's value should be reduced by 10% for each 50000 km driven
    """
    # Given
    driven_years = 0
    car_price = car_price_parameter
    driven_km = driven_km_parameter

    # When
    depriciated_value = calculate_car_depreciation(car_price, driven_years, driven_km)

    # Then
    assert depriciated_value == pytest.approx(expected_value, rel=1e-2)


@pytest.mark.parametrize(
    "car_price_parameter, driven_years_parameter, driven_km_parameter, expected_value",
    [(100, 1, 50000, 80), (100, 5, 50000, 49.05), (100, 5, 100000, 40.05)],
)
def test_car_depreciation_for_age_and_mileage(
    car_price_parameter, driven_years_parameter, driven_km_parameter, expected_value
):
    # Given
    car_price = car_price_parameter
    driven_years = driven_years_parameter
    driven_km = driven_km_parameter

    # When
    depriciated_value = calculate_car_depreciation(car_price, driven_years, driven_km)

    # Then
    assert depriciated_value == pytest.approx(expected_value, rel=1e-2)
