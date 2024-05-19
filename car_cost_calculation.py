from olympus_calculator.car import calculate_car_depreciation
import typer


def main():
    price = float(typer.prompt("What is the price of the car? [€]"))
    years = int(typer.prompt("How many years you expect to drive the car?"))
    km_in_a_year = int(
        typer.prompt("How many kilometers you expect to drive the car in one year?")
    )

    km = int(years) * int(km_in_a_year)
    depriciated_value = calculate_car_depreciation(price, years, km)
    monthly_cost = (price - depriciated_value) / (years * 12)

    typer.echo(
        f"\nAfter {years} years and {km} km the car will be worth: {depriciated_value:.0f} €"
    )
    typer.echo(f"The monthly cost of the car is {monthly_cost:.2f} €/month")


if __name__ == "__main__":
    typer.run(main)
