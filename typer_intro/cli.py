import typer

GREETING = "Hello"
FORMAL_GREETING = "Good day Mr/Ms"


def _main(name: str, last_name: str = "", formal: bool = False):
    greeting = GREETING if not formal else FORMAL_GREETING
    full_name = f"{name} {last_name}".strip()

    typer.echo(f"{greeting} {full_name}!")


def main():
    typer.run(_main)
