from .car import Car
from .car_cost import CarMonthlyCosts


class CarCostCalculator:
    def __init__(self):
        self.YEAR_DEPRECIATION = 0.1  # every year
        self.KM_DEPRECIATION = 0.021  # every 10000 km
        self.MAINTENANCE_COST = 458  # € per 10000 km

    def calculate_monthly_costs(self, car: Car, fuel_price: float) -> CarMonthlyCosts:
        overall_depreciation = self.calculate_car_depreciation(
            car.initial_value, car.driven_years, car.driven_km
        )
        overall_fuel_cost = self.calculate_fuel_cost(
            car.driven_km, car.fuel_consumption, fuel_price
        )
        overall_maintenance_cost = self.calculate_maintenance_cost(car.driven_km)

        number_of_months = car.driven_years * 12

        monthly_costs = CarMonthlyCosts(
            monthly_depreciation_cost=overall_depreciation / number_of_months,
            monthly_fuel_cost=overall_fuel_cost / number_of_months,
            monthly_maintenance_cost=overall_maintenance_cost / number_of_months,
            monthly_road_tax=car.road_tax / 12,
            monthly_insurance_cost=car.insurance_cost / 12,
        )
        return monthly_costs

    def calculate_depreciated_value(self, car: Car) -> float:
        depreciation = self.calculate_car_depreciation(
            car.initial_value, car.driven_years, car.driven_km
        )
        return car.initial_value - depreciation

    def calculate_car_depreciation(
        self, initial_price: float, driven_years: int, driven_kms: int
    ) -> float:
        year_depreciation_factor = (1 - self.YEAR_DEPRECIATION) ** driven_years
        depreciation_from_years = initial_price * (1 - year_depreciation_factor)

        km_depreciation_factor = (1 - self.KM_DEPRECIATION) ** (driven_kms // 10000)
        depreciation_from_kms = initial_price * (1 - km_depreciation_factor)

        total_depreciation = depreciation_from_years + depreciation_from_kms
        return total_depreciation

    def calculate_fuel_cost(
        self, driven_kms: int, fuel_consumption: float, fuel_price: float
    ) -> float:
        return (driven_kms / 100) * fuel_consumption * fuel_price

    def calculate_maintenance_cost(self, driven_kms: int) -> float:
        return (driven_kms / 10000) * self.MAINTENANCE_COST
