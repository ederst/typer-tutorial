from typing import List

import typer
from click.testing import Result
from typer.testing import CliRunner

from typer_intro.cli import FORMAL_GREETING, FORMAL_GREETING_STYLE, GREETING, GREETING_STYLE, STDERR_STYLE, _main

# Test data
FIRST_NAME = "John"
LAST_NAME = "Doe"
FULL_NAME = f"{FIRST_NAME} {LAST_NAME}"

STYLED_GREETING = typer.style(GREETING, **GREETING_STYLE)
STYLED_FORMAL_GREETING = typer.style(FORMAL_GREETING, **FORMAL_GREETING_STYLE)

GREETING_WITH_FULL_NAME = f"{STYLED_GREETING} {FULL_NAME}!"
GREETING_WITH_FIRST_NAME = f"{STYLED_GREETING} {FIRST_NAME}!"
FORMAL_GREETING_WITH_FULL_NAME = f"{STYLED_FORMAL_GREETING} {FULL_NAME}!"
FORMAL_GREETING_WITH_FIRST_NAME = f"{STYLED_FORMAL_GREETING} {FIRST_NAME}!"
STDERR_GREETING = typer.style(f"{GREETING} {FIRST_NAME}!", **STDERR_STYLE)

# Initialize typer test runner
app = typer.Typer()
app.command()(_main)
runner = CliRunner(mix_stderr=False)


def _invoke_app(args: List = None) -> Result:
    return runner.invoke(app, args, color=True)


def test_fail_with_missing_argument_NAME():
    result = _invoke_app()
    assert result.exit_code == 2
    assert "Error: Missing argument 'NAME'." in result.stderr


def test_fail_with_no_such_option():
    fake_opt = "--fakeopt"
    result = _invoke_app([fake_opt])
    assert result.exit_code == 2
    assert f"Error: No such option: {fake_opt}" in result.stderr


def test_print_greeting_with_first_name():
    result = _invoke_app([FIRST_NAME])
    assert result.exit_code == 0
    assert GREETING_WITH_FIRST_NAME in result.stdout


def test_print_greeting_with_first_name_to_stderr():
    result = _invoke_app([FIRST_NAME, '--use-stderr'])
    assert result.exit_code == 0
    assert STDERR_GREETING not in result.stdout
    assert STDERR_GREETING in result.stderr


def test_fail_with_unexpected_extra_arguments():
    result = _invoke_app(FULL_NAME.split())
    assert result.exit_code == 2
    assert f"Error: Got unexpected extra argument ({LAST_NAME})" in result.stderr


def test_print_greeting_with_full_name():
    result = _invoke_app([FIRST_NAME, "--last-name", LAST_NAME])
    assert result.exit_code == 0
    assert GREETING_WITH_FULL_NAME in result.stdout


def test_print_greeting_with_full_name_and_no_formal_argument():
    result = _invoke_app([FIRST_NAME, "--last-name", LAST_NAME, "--no-formal"])
    assert result.exit_code == 0
    assert GREETING_WITH_FULL_NAME in result.stdout


def test_print_formal_greeting_with_first_name():
    result = _invoke_app([FIRST_NAME, "--formal"])
    assert result.exit_code == 0
    assert FORMAL_GREETING_WITH_FIRST_NAME in result.stdout


def test_print_formal_greeting_with_full_name():
    result = _invoke_app([FIRST_NAME, "--last-name", LAST_NAME, "--formal"])
    assert result.exit_code == 0
    assert FORMAL_GREETING_WITH_FULL_NAME in result.stdout
