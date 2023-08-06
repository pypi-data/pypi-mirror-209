import typer
from cookiecutter.main import cookiecutter  # type: ignore
from fluxional.configs import REPOSITORY_TEMPLATE
from pydantic import BaseModel
from typing import Optional


class CreateAppModel(BaseModel):
    project_name: Optional[str] = None
    extract_project_to_root: bool = True


cli = typer.Typer()


@cli.command()
def create_app(
    project_name: Optional[str] = None, extract_project_to_root: bool = True
):
    context = CreateAppModel(
        project_name=project_name, extract_project_to_root=extract_project_to_root
    ).dict(exclude_defaults=True)

    cookiecutter(
        REPOSITORY_TEMPLATE,
        no_input=True,
        extra_context=context,
    )


if __name__ == "__main__":
    cli()
