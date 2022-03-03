import typer


def _main(name: str, last_name: str, formal: bool = False):
    greeting_prefix = "Hello" if not formal else "Good day Mr/Ms"

    typer.echo(f"{greeting_prefix} {name} {last_name}!")


def main():
    typer.run(_main)
