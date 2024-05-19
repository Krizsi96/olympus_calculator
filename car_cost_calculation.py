from olympus_calculator.car import calculate_car_depreciation
import typer
from rich import print


def main():
    price = float(typer.prompt("What is the price of the car? [€]"))
    years = int(typer.prompt("How many years you expect to drive the car?"))
    km_in_a_year = int(
        typer.prompt("How many kilometers you expect to drive the car in one year?")
    )

    km = int(years) * int(km_in_a_year)
    depriciated_value = calculate_car_depreciation(price, years, km)
    monthly_cost = (price - depriciated_value) / (years * 12)

    print(
        f"\nAfter [green]{years}[/green] years and [green]{km}[/green] km the car will be worth: [cyan]{depriciated_value:.0f} €[/cyan]"
    )
    print(f"The monthly cost of the car is [cyan]{monthly_cost:.2f} €/month[/cyan]")


if __name__ == "__main__":
    typer.run(main)
