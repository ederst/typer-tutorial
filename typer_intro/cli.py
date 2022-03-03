import typer

SILLY_NAMES = ["Boaty McBoatface", "Dishy McFlatface"]
SILLY_MESSAGE = "'{silly_full_name}' is a really silly name."

GREETING = "Hello"
FORMAL_GREETING = "Good day Mr/Ms"

GREETING_STYLE = dict(fg=typer.colors.GREEN, bold=True)
FORMAL_GREETING_STYLE = dict(bg=typer.colors.RED)
STDERR_STYLE = dict(fg=typer.colors.RED)


def _main(
    name: str = typer.Argument(...),
    last_name: str = "",
    formal: bool = False,
    use_stderr: bool = False,
    abort_on_errors: bool = False,
):
    """
    Say hi to NAME, optionally with a --last-name.

    If --formal is used, say hi very formally.
    """

    try:
        full_name = f"{name} {last_name}".strip()
        if full_name in SILLY_NAMES:
            typer.echo(SILLY_MESSAGE.format(silly_full_name=full_name), err=True)
            raise typer.Exit(code=1)

        greeting = GREETING if not formal else FORMAL_GREETING

        if not use_stderr:
            greeting_style = GREETING_STYLE if not formal else FORMAL_GREETING_STYLE
            greeting = typer.style(greeting, **greeting_style)

        full_greeting = f"{greeting} {full_name}!"
        full_greeting_style = STDERR_STYLE if use_stderr else {}

        typer.secho(full_greeting, err=use_stderr, **full_greeting_style)
    except RuntimeError as e:
        if abort_on_errors:
            raise typer.Abort()
        else:
            raise e


def main():
    typer.run(_main)
