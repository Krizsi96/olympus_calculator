from dataclasses import dataclass, field
from olympus_calculator.car_monthly_cost import CarMonthlyCosts


@dataclass
class Car:
    initial_value: float
    depreciated_value: float = field(init=False)
    driven_years: int
    driven_km: int
    fuel_consumption: float
    road_tax_per_year: float
    insurance_cost_per_year: float
    cost: CarMonthlyCosts = field(init=False)
