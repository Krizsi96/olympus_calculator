import pytest
from olympus_calculator.car_cost import CarMonthlyCosts


def test_total_monthly_cost_is_calculated():
    # Given
    monthly_depreciation_cost = 10
    monthly_fuel_cost = 20
    monthly_maintenance_cost = 30
    monthly_road_tax = 40
    monthly_insurance_cost = 50

    # When
    monthly_costs = CarMonthlyCosts(
        monthly_depreciation_cost=monthly_depreciation_cost,
        monthly_fuel_cost=monthly_fuel_cost,
        monthly_maintenance_cost=monthly_maintenance_cost,
        monthly_road_tax=monthly_road_tax,
        monthly_insurance_cost=monthly_insurance_cost,
    )

    # Then
    assert monthly_costs.total_monthly_cost == 150
