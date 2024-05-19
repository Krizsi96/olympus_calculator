from dataclasses import dataclass, field


@dataclass
class CarMonthlyCosts:
    monthly_depreciation_cost: float
    monthly_fuel_cost: float
    monthly_maintenance_cost: float
    monthly_road_tax: float
    monthly_insurance_cost: float
    total_monthly_cost: float = field(init=False)

    def __post_init__(self):
        self.total_monthly_cost = (
            self.monthly_depreciation_cost
            + self.monthly_fuel_cost
            + self.monthly_maintenance_cost
            + self.monthly_road_tax
            + self.monthly_insurance_cost
        )
