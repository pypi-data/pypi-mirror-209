import asyncio
import logging
from enum import StrEnum
from pathlib import Path
from typing import Optional

import typer
from rich.logging import RichHandler

from .build import OntoSiteBuilder

LogLevel = StrEnum("LogLevel", {name: name for name in logging.getLevelNamesMapping().keys()})

app = typer.Typer()


@app.callback()
def configure_app(
    ctx: typer.Context,
    log_level: LogLevel = typer.Option(
        LogLevel.INFO, help="Log level for CLI output", case_sensitive=False
    ),
    repo_path: Path = typer.Option(
        Path("."), help="Path to repository with RDF/XML ontology files"
    ),
):
    ctx.ensure_object(dict)

    ctx.obj["repo_path"] = repo_path

    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )


@app.command()
def build(
    ctx: typer.Context,
    template_path: Optional[Path] = typer.Option(
        None, help="Path to custom templates for the ontology to build"
    ),
    output_path: Path = typer.Option(Path("./public/"), help="Output directory for ontology site"),
):
    """Build static ontology website"""

    builder = OntoSiteBuilder(ctx.obj["repo_path"], output_path, template_path=template_path)
    asyncio.run(builder.build_all())
