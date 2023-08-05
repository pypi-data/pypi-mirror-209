import json
import os
import re
import subprocess
import time
from pathlib import Path

import typer
from rich import print

from quantready.helpers import snakecase
from quantready.models import QuantReadyInfo


def is_in_git_repo() -> bool:
    try:
        subprocess.check_output(["git", "rev-parse", "--is-inside-work-tree"])
        return True
    except subprocess.CalledProcessError:
        return False


def assert_git_repo_clean():
    try:
        subprocess.check_output(["git", "diff-index", "--quiet", "HEAD", "--"])
    except subprocess.CalledProcessError as e:
        print(
            "Error: This command must be run with a clean git repository. Please commit any pending changes."
        )
        raise typer.Abort() from e


def assert_gh_cli_installed():
    result = os.system("gh --version > /dev/null 2>&1")

    if result != 0:
        print("Error: The GitHub CLI is not installed.")
        raise typer.Abort()


def get_git_repo_remote_url():
    try:
        repo = (
            subprocess.check_output(["git", "config", "--get", "remote.origin.url"])
            .decode("utf-8")
            .strip()
        )
        if repo.startswith("git@"):
            repo = repo.replace(":", "/").replace("git@", "https://")
        if repo.endswith(".git"):
            repo = repo[:-4]
        return repo
    except subprocess.CalledProcessError:
        print("Warning: Could not find remote url for git repository.")
        return None


def pull_template(qr_info: QuantReadyInfo, force: bool = False) -> Path:
    if is_in_git_repo():
        return pull_template_into_existing_repo(force, qr_info)
    else:
        return pull_template_into_new_repo(qr_info)


def pull_template_into_new_repo(qr_info: QuantReadyInfo):
    assert_gh_cli_installed()

    print("Cloning template repository")
    name = qr_info.name.strip().replace(" ", "_")
    description = qr_info.description.replace('"', "'")

    try:
        output = subprocess.check_output(
            [
                "gh",
                "repo",
                "create",
                name,
                "--description",
                description,
                "--private",
                "--template",
                qr_info.template,
            ]
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            "Error: Could not create repository.  Please check that the name is not already taken."
        ) from e

    qr_info.repo = output.decode("utf-8").strip()
    print(f"Repository created: {qr_info.repo} - sleeping for 15 seconds")
    time.sleep(15)
    try:
        output = subprocess.check_output(["gh", "repo", "clone", qr_info.repo])
        print(f"Clone successful {output.decode('utf-8').lstrip()}".strip())
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            "Error: Could not clone repository.  Please check github cli permissions are set."
        ) from e

    return Path(f"./{name}").resolve().absolute().resolve().absolute()


def pull_template_into_existing_repo(force: bool, qr_info: QuantReadyInfo) -> Path:
    if not force:
        assert_git_repo_clean()
    print("Merging template repository into existing repository")

    os.system(f"git remote add quantready-template {qr_info.template}")
    os.system("git fetch --all")
    os.system("git merge quantready-template/main --allow-unrelated-histories")
    os.system("git remote remove quantready-template")
    return Path(".").resolve().absolute().resolve().absolute()


def get_quantready_config(
    name, template, description, repo, version, config_dir: Path | None = None
):
    config_dir = config_dir or Path(".")

    if os.path.exists(config_dir / ".quantready"):
        print("Loading .quantready config file")
        with open(config_dir / ".quantready") as f:
            qr_info = QuantReadyInfo(**json.load(f))
    else:
        print("Creating .quantready config file")
        qr_info = create_config_file(
            name, template, description, repo, version, config_dir=config_dir
        )
    return qr_info


def create_config_file(
    name,
    template,
    description,
    repo,
    version,
    require_confirm: bool = False,
    config_dir: Path | None = None,
):
    repo = repo or get_git_repo_remote_url() or ""
    if not name:
        name = typer.prompt("Please enter a name")
        require_confirm = True
    if not template:
        template = typer.prompt("Please enter a template url")
        require_confirm = True
    if not description:
        description = typer.prompt("Please enter a description")
        require_confirm = True
    if not repo:
        repo = typer.prompt("Please enter a repo")
        require_confirm = True
    if not version:
        version = typer.prompt("Please enter a version (example: 0.1.0)")
        require_confirm = True

    if require_confirm:
        confirm = typer.confirm(
            f"Name: {name}\nTemplate: {template}\nDescription: {description}\nRepo: {repo}\nVersion: {version}\n\nAre these values correct?"
        )
        if not confirm:
            typer.echo("Exiting...")
            raise typer.Abort()

    qr_info = QuantReadyInfo(
        name=name,
        template=template,
        description=description,
        repo=repo,
        version=version,
    )

    # write config file to .quantready
    config_dir = config_dir or Path(".")
    with open(config_dir / ".quantready", "w") as f:
        f.write(qr_info.json(indent=4))
    return qr_info


def reformat_template(template_dir: Path, qr_info: QuantReadyInfo):
    template_name = qr_info.template.split("/")[-1].replace(".git", "")
    template_package_name = (snakecase(template_name) or template_name).replace(
        "-", "_"
    )
    new_package_name = (snakecase(qr_info.name) or qr_info.name).replace("-", "_")

    # Move .quantready file into directory to ./name

    # Find and replace "quantready_base" with "name" (exclude README.md)
    for file in template_dir.glob("**/*"):
        if (
            file.is_file()
            and file.name != "README.md"
            and ".git" not in str(file.resolve())
        ):
            with file.open("r") as f:
                contents = f.read()
            new_contents = contents.replace(template_name, qr_info.name)
            new_contents = new_contents.replace(template_package_name, new_package_name)
            if new_contents != contents:
                print(f"Updating {file.resolve()}")
            with file.open("w") as f:
                f.write(new_contents)

    # Rename ./quantready_base with ./name
    if (template_dir / template_package_name).exists():
        print("Renaming template package directory")
        (template_dir / template_package_name).rename(template_dir / new_package_name)

    # Update text in pyproject.toml: <description>, <repo>, <version>
    pyproject_toml = template_dir / "pyproject.toml"
    with pyproject_toml.open("r") as f:
        contents = f.read()
    new_contents = re.sub(r"name = .*", f'name = "{qr_info.name}"', contents)
    new_contents = re.sub(
        r"version = .*", f'version = "{qr_info.version}"', new_contents
    )
    new_contents = re.sub(
        r"description = .*", f'description = "{qr_info.description}"', new_contents
    )
    new_contents = re.sub(
        r"\"Repository\".*", f'"Repository" = "{qr_info.repo}"', new_contents
    )
    new_contents = re.sub(
        r"\"Bug Tracker\".*", f'"Bug Tracker" = "{qr_info.repo}/issues"', new_contents
    )

    if new_contents != contents:
        print(f"Updating {pyproject_toml.resolve()}")
    with pyproject_toml.open("w") as f:
        f.write(new_contents)

    # Update text in ./name/init.py: <description>, <version>
    init_py = template_dir / new_package_name / "__init__.py"
    with init_py.open("r") as f:
        contents = f.read()

    new_contents = re.sub(
        r"__description__.*", f'__description__ = "{qr_info.description}"', contents
    )
    new_contents = re.sub(
        r"__version__.*", f'__version__ = "{qr_info.version}"', new_contents
    )

    if new_contents != contents:
        print(f"Updating {init_py.resolve()}")
    with init_py.open("w") as f:
        f.write(new_contents)

    # Add new header to README.md
    readme = template_dir / "README.md"
    with readme.open("r") as f:
        contents = f.read()
    new_header = f"""# {qr_info.name}

{qr_info.description}

Built using [quantready](https://github.com/closedloop-technologies/quantready) using template ([{qr_info.template}])[{qr_info.template}]

"""
    contents = new_header + contents
    print(f"Updating {readme.resolve()}")
    with readme.open("w") as f:
        f.write(contents)


def initialize(
    name, template, description, repo, version, force, config_dir: Path | None = None
) -> tuple[QuantReadyInfo, Path]:
    if name and "test" in name.lower():
        raise ValueError("Name cannot contain 'test'")
    qr_info = get_quantready_config(
        name, template, description, repo, version, config_dir=config_dir
    )

    # Clone the repository
    template_dir = pull_template(qr_info, force=force)
    reformat_template(template_dir, qr_info)
    return qr_info, template_dir
