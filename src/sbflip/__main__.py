"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """sbflip."""


if __name__ == "__main__":
    main(prog_name="sbflip")  # pragma: no cover
