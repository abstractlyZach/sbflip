"""Command-line interface."""
import time

import click

from sbflip import tiles


@click.command()
@click.version_option()
def main() -> None:
    """sbflip."""
    flipboard = tiles.Flipboard(80, " abcdefghijklmnopqrstuvwxyz")
    flipboard.set_message("hi welcome to my flipboard")
    flipboard.set_message("this is pretty cool i think")

    while True:
        print(flipboard.text, end="\r")
        flipboard.tick()
        time.sleep(0.25)


if __name__ == "__main__":
    main(prog_name="sbflip")  # pragma: no cover
