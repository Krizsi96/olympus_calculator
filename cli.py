from olympus_calculator.car_cost_calculator import CarCostCalculator
from olympus_calculator.car import Car
import typer
from rich import print
from rich.table import Table
from rich.console import Console

console = Console()


def main():
    cost_calculation = CarCostCalculator()
    car = user_car_input()
    fuel_price = user_fuel_price_input()

    car.cost = cost_calculation.calculate_monthly_costs(car, fuel_price)
    car.depreciated_value = cost_calculation.calculate_depreciated_value(car)

    print_calculation_parameters(cost_calculation)
    print_cost(car)


def user_car_input() -> Car:
    price = float(typer.prompt("What is the price of the car? [€]"))
    years = int(typer.prompt("How many years you expect to drive the car?"))
    km_in_a_year = int(
        typer.prompt("How many kilometers you expect to drive the car in one year?")
    )
    fuel_consumption = float(
        typer.prompt("What is the fuel consumption of the car? [l/100km]")
    )
    road_tax = float(typer.prompt("What is the road tax? [€/year]"))
    insurance = float(typer.prompt("What is the insurance cost? [€/year]"))

    return Car(
        initial_value=price,
        driven_years=years,
        driven_km=km_in_a_year * years,
        fuel_consumption=fuel_consumption,
        road_tax_per_year=road_tax,
        insurance_cost_per_year=insurance,
    )


def user_fuel_price_input() -> float:
    return float(typer.prompt("What is the fuel price? [€/l]"))


def print_cost(car_data: Car):
    table = Table("Cost Item", "€/month")
    table.add_row("Depreciation", f"{car_data.cost.monthly_depreciation_cost:.2f}")
    table.add_row("Fuel", f"{car_data.cost.monthly_fuel_cost:.2f}")
    table.add_row("Maintenance", f"{car_data.cost.monthly_maintenance_cost:.2f}")
    table.add_row("Road Tax", f"{car_data.cost.monthly_road_tax:.2f}")
    table.add_row("Insurance", f"{car_data.cost.monthly_insurance_cost:.2f}")
    table.add_row("Total", f"{car_data.cost.total_monthly_cost:.2f}")
    console.print("\nMonthly cost of the car:")
    console.print(table)

    print(
        f"\nAfter [green]{car_data.driven_years}[/green] years and [green]{car_data.driven_km}[/green] km the car will be worth: [cyan]{car_data.depreciated_value:.0f} €[/cyan]"
    )
    print(
        f"The monthly cost of the car is [cyan]{car_data.cost.total_monthly_cost:.2f} €/month[/cyan]"
    )


def print_calculation_parameters(cost_calculation: CarCostCalculator):
    yearly_depreciation = cost_calculation.YEAR_DEPRECIATION * 100
    km_depreciation = cost_calculation.KM_DEPRECIATION * 100
    maintenance_cost = cost_calculation.MAINTENANCE_COST

    print("\nCalculation parameters:")
    print(f"Yearly depreciation: [cyan]{yearly_depreciation} %[/cyan]")
    print(f"Km depreciation: [cyan]{km_depreciation} % / 10000 km[/cyan]")
    print(f"Maintenance cost: [cyan]{maintenance_cost} € / 10000 km[/cyan]")


if __name__ == "__main__":
    typer.run(main)
