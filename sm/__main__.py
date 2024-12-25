import enum
import click
import logging as log

from enum import Enum, unique
from typing import Self

@enum.unique
class SystemSetupType(Enum):
    Regular = enum.auto()
    Homelab = enum.auto()

    def from_str(s: str) -> Self:
        match s:
            case "regular" | "Regular":
                return SystemSetupType.Regular
            case "homelab" | "Homelab":
                return SystemSetupType.Homelab
            case _:
                raise Exception(f"Cannot convert str to {SystemSetupType.__name__}")

@click.group()
def cli():
    pass

@cli.command()
@click.argument(
    "name",
    type=click.Choice([m.lower() for m in SystemSetupType.__members__]),
    required=True,
    metavar="[NAME]"
)
def setup(name: str):
    st = SystemSetupType.from_str(name)
    ssm = SystemSetupManager(st)

def main():
    log.basicConfig(
        format="{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
        level=log.DEBUG
    )
    cli()
