from dataclasses import dataclass, field
from .car_cost import CarMonthlyCosts


@dataclass
class Car:
    initial_value: float
    depreciated_value: float = field(init=False)
    driven_years: int
    driven_km: int
    driven_km_in_a_year: int = field(init=False)
    fuel_consumption: float
    road_tax: float
    insurance_cost: float
    cost: CarMonthlyCosts = field(init=False)

    def __post_init__(self):
        self.driven_km_in_a_year = self.driven_km / self.driven_years
