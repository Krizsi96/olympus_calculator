from dataclasses import dataclass


@dataclass
class CarMonthlyCosts:
    monthly_depreciation_cost: float = 0
    monthly_fuel_cost: float = 0
    monthly_maintenance_cost: float = 0
    monthly_road_tax: float = 0
    monthly_insurance_cost: float = 0
