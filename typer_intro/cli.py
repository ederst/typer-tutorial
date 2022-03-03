import typer

GREETING = "Hello"
FORMAL_GREETING = "Good day Mr/Ms"


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
