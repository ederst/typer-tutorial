import typer

GREETING = "Hello"
FORMAL_GREETING = "Good day Mr/Ms"


def _main(name: str, last_name: str, formal: bool = False):
    greeting = GREETING if not formal else FORMAL_GREETING

    typer.echo(f"{greeting} {name} {last_name}!")


def main():
    typer.run(_main)
