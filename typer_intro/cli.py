import typer

GREETING = typer.style("Hello", fg=typer.colors.GREEN, bold=True)
FORMAL_GREETING = typer.style("Good day Mr/Ms", bg=typer.colors.BRIGHT_RED)


def _main(name: str, last_name: str = "", formal: bool = False):
    """
    Say hi to NAME, optionally with a --last-name.

    If --formal is used, say hi very formally.
    """

    greeting = GREETING if not formal else FORMAL_GREETING
    full_name = f"{name} {last_name}".strip()

    typer.echo(f"{greeting} {full_name}!")


def main():
    typer.run(_main)
