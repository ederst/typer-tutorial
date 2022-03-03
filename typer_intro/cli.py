import typer


def _main(name: str):
    typer.echo(f"Hello {name}!")


def main():
    typer.run(_main)
