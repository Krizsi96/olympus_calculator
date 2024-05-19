def calculate_car_depreciation(
    initial_price: float, driven_years: int, driven_kms: int
) -> float:
    depreciation_from_years = initial_price - initial_price * (0.9**driven_years)
    depreciation_from_kms = initial_price - initial_price * (
        0.85 ** (driven_kms // 50000)
    )
    total_depreciation = depreciation_from_years + depreciation_from_kms
    return initial_price - total_depreciation
