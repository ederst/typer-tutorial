import typer


def _main(name: str, last_name: str):
    typer.echo(f"Hello {name} {last_name}!")


def main():
    typer.run(_main)
