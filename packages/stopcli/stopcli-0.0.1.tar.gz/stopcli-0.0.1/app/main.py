import click
import pyfiglet
from app.generator import generate_sheets, get_pwd


pyfiglet.print_figlet("Stop CLI")

@click.group()
def run():
    """A CLI for stop template sheets."""
    pass

@run.command()
@click.option("--output", "-o", help="Output file name.", default=f"{get_pwd()}/sheets.pdf")
@click.argument('names', nargs=-1)
def generate(output, names):
    """Generates a stop sheets."""
    generate_sheets(names, print)