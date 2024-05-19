def calculate_car_depreciation(
    initial_price: float, driven_years: int, driven_kms: int
) -> float:
    return initial_price * (0.9**driven_years)
