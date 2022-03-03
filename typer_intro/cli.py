import typer

GREETING = "Hello"
FORMAL_GREETING = "Good day Mr/Ms"

GREETING_STYLE = dict(fg=typer.colors.GREEN, bold=True)
FORMAL_GREETING_STYLE = dict(bg=typer.colors.RED)
STDERR_STYLE = dict(fg=typer.colors.RED)


def _main(name: str, last_name: str = "", formal: bool = False, use_stderr: bool = False):
    """
    Say hi to NAME, optionally with a --last-name.

    If --formal is used, say hi very formally.
    """

    greeting = GREETING if not formal else FORMAL_GREETING

    if not use_stderr:
        greeting_style = GREETING_STYLE if not formal else FORMAL_GREETING_STYLE
        greeting = typer.style(greeting, **greeting_style)

    full_name = f"{name} {last_name}".strip()

    full_greeting = f"{greeting} {full_name}!"
    full_greeting_style = STDERR_STYLE if use_stderr else {}

    typer.secho(full_greeting, err=use_stderr, **full_greeting_style)


def main():
    typer.run(_main)
