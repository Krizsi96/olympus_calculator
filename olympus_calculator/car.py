def calculate_car_depreciation(
    initial_price: float, driven_years: int, driven_kms: int
) -> float:
    YEAR_DEPRECIATION = 0.1  # every year
    KM_DEPRECIATION = 0.1  # every 50000 km

    year_depreciation_factor = (1 - YEAR_DEPRECIATION) ** driven_years
    depreciation_from_years = initial_price * (1 - year_depreciation_factor)

    km_depreciation_factor = (1 - KM_DEPRECIATION) ** (driven_kms // 50000)
    depreciation_from_kms = initial_price * (1 - km_depreciation_factor)

    total_depreciation = depreciation_from_years + depreciation_from_kms
    return initial_price - total_depreciation
