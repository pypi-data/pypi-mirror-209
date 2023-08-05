import pyfiglet
import typer
from rich import print
from typer import Typer

from quantready import __description__ as DESCRIPTION
from quantready import __name__ as NAME
from quantready import __version__ as VERSION
from quantready.config import load_config
from quantready.initialize import (
    get_quantready_config,
    initialize,
    is_in_git_repo,
    pull_template_into_existing_repo,
    reformat_template,
)


def banner():
    return pyfiglet.figlet_format(NAME.replace("_", " ").title(), font="slant").rstrip()


app = Typer(help=f"{(NAME or '').replace('_', ' ').title()} CLI")


@app.command()
def info():
    """Prints info about the package"""
    print(f"{banner()}\n")
    print(f"{NAME}: {DESCRIPTION}")
    print(f"Version: {VERSION}\n")
    print(load_config())


@app.command()
def init(
    name: str = "",
    template: str = "",
    description: str = "",
    repo: str = "",
    version: str = "",
    force: bool = False,
):
    """Main Function"""
    print(f"{banner()}\n")

    print("Initializing repository...")
    # If in git repo, check if clean
    try:
        initialize(name, template, description, repo, version, force)
    except ValueError as e:
        print(f"Error: {e}")
        raise typer.Abort() from e

    # Check if pypi is configured
    # Check if gcloud is configured
    print("Repository initialization complete")


@app.command()
def setup_pypi():
    """Configure the package"""
    print(f"{banner()}\n")
    print(
        "This is your configuration command-line interface.  Feel free to customize it as you see fit.\n"
    )


@app.command()
def setup_gcloud():
    """Configure the package"""
    print(f"{banner()}\n")
    print(
        "This is your configuration command-line interface.  Feel free to customize it as you see fit.\n"
    )


@app.command()
def update(template: str = "", force: bool = False):
    # If in git repo, check if clean
    if not is_in_git_repo():
        print("Error: This command must be run in a git repository.")
        typer.Abort()
    qr_info = get_quantready_config("", template, "", "", "")
    template_dir = pull_template_into_existing_repo(force, qr_info)
    reformat_template(template_dir, qr_info)
