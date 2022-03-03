from typing import List

from click.testing import Result
from typer import Typer
from typer.testing import CliRunner
from typer_intro.cli import FORMAL_GREETING, GREETING, _main

# Test data
FIRST_NAME = "John"
LAST_NAME = "Doe"
FULL_NAME = f"{FIRST_NAME} {LAST_NAME}"

FULL_GREETING = f"{GREETING} {FULL_NAME}!"
FULL_FORMAL_GREETING = f"{FORMAL_GREETING} {FULL_NAME}!"

# Initialize typer test runner
app = Typer()
app.command()(_main)
runner = CliRunner()


def _invoke_app(args: List = None) -> Result:
    return runner.invoke(app, args)


def test_fail_with_missing_argument_NAME():
    result = _invoke_app()
    assert result.exit_code == 2
    assert "Error: Missing argument 'NAME'." in result.stdout


def test_fail_with_missing_argument_LAST_NAME():
    result = _invoke_app([FIRST_NAME])
    assert result.exit_code == 2
    assert "Error: Missing argument 'LAST_NAME'." in result.stdout


def test_fail_with_no_such_option():
    fake_opt = "--fakeopt"
    result = _invoke_app([fake_opt])
    assert result.exit_code == 2
    assert f"Error: No such option: {fake_opt}" in result.stdout


def test_print_greeting():
    result = _invoke_app(FULL_NAME.split())
    assert result.exit_code == 0
    assert FULL_GREETING in result.stdout


def test_print_greeting_with_argument():
    result = _invoke_app(FULL_NAME.split() + ["--no-formal"])
    assert result.exit_code == 0
    assert FULL_GREETING in result.stdout


def test_print_formal_greeting():
    result = _invoke_app(FULL_NAME.split() + ["--formal"])
    assert result.exit_code == 0
    assert FULL_FORMAL_GREETING in result.stdout