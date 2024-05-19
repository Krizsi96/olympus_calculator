def calculate_car_depreciation(
    initial_price: float, driven_years: int, driven_kms: int
) -> float:
    YEAR_DEPRECIATION = 0.1  # every year
    KM_DEPRECIATION = 0.021  # every 10000 km

    year_depreciation_factor = (1 - YEAR_DEPRECIATION) ** driven_years
    depreciation_from_years = initial_price * (1 - year_depreciation_factor)

    km_depreciation_factor = (1 - KM_DEPRECIATION) ** (driven_kms // 10000)
    depreciation_from_kms = initial_price * (1 - km_depreciation_factor)

    total_depreciation = depreciation_from_years + depreciation_from_kms
    return initial_price - total_depreciation


def calculate_fuel_cost(
    driven_kms: int, fuel_consumption: float, fuel_price: float
) -> float:
    return (driven_kms / 100) * fuel_consumption * fuel_price


def calculate_maintenance_cost(driven_kms: int) -> float:
    # maintenance cost is 458€ per 10000 km
    MAINTENANCE_COST = 458  # € per 10000 km
    return (driven_kms / 10000) * MAINTENANCE_COST
