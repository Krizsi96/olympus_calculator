import pytest
from olympus_calculator.car import (
    calculate_car_depreciation,
    calculate_fuel_cost,
    calculate_maintenance_cost,
)


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


@pytest.mark.parametrize(
    "driven_km_parameter, fuel_consumption_parameter, fuel_price_parameter, expected_value",
    [(100, 5, 1.5, 7.5), (200, 5, 1.5, 15), (100, 10, 1.5, 15), (100, 5, 2, 10)],
)
def test_fuel_cost_calculation(
    driven_km_parameter,
    fuel_consumption_parameter,
    fuel_price_parameter,
    expected_value,
):
    # Given
    driven_km = driven_km_parameter
    fuel_consumption = fuel_consumption_parameter
    fuel_price = fuel_price_parameter

    # When
    fuel_cost = calculate_fuel_cost(driven_km, fuel_consumption, fuel_price)

    # Then
    assert fuel_cost == pytest.approx(expected_value, rel=1e-2)


@pytest.mark.parametrize(
    "driven_km_parameter, expected_value", [(10000, 458), (20000, 916), (50000, 2290)]
)
def test_calculate_maintenance_cost(driven_km_parameter, expected_value):
    """
    maintenance cost is 458€ per 10000 km
    """
    # Given
    driven_km = driven_km_parameter

    # When
    maintenance_cost = calculate_maintenance_cost(driven_km)

    # Then
    assert maintenance_cost == expected_value
