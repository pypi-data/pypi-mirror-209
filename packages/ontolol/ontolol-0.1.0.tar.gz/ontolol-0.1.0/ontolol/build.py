import logging
from pathlib import Path
from typing import Any, Callable, ClassVar
from urllib.parse import ParseResult, urlparse

from jinja2 import Environment, FileSystemLoader, select_autoescape
from owlready2 import Ontology

from .repo import RepoWorld


# FIXME use this to write files for content negotiation
_format_map: dict[str, Callable[["OntoSiteBuilder", Ontology | str, str], str]] = {}


def build_format(mime_type: str) -> Callable[[Callable], Callable]:
    def register_build_func(
        func: Callable[["OntoSiteBuilder", Ontology | str, str], str]
    ) -> Callable[["OntoSiteBuilder", Ontology | str, str], str]:
        _format_map[mime_type] = func
        return func

    return register_build_func


class OntoSiteBuilder:
    """Builder for a complete ontology repository website."""

    def __init__(
        self,
        repo_path: Path | str,
        output_path: Path | str,
        template_path: Path | str | None = None,
    ):
        if not isinstance(repo_path, Path):
            repo_path = Path(repo_path)
        if not isinstance(repo_path, Path):
            output_path = Path(output_path)
        if template_path is not None and not isinstance(repo_path, Path):
            template_path = Path(template_path)

        self._logger = logging.getLogger(__name__)

        # Configure Jinja2 template environment
        template_paths = [Path(__file__).parent / "templates"]
        if template_path is not None:
            template_paths.insert(template_path)
            self._logger.debug("Added template path %s", template_path)
        self.template_env = Environment(
            loader=FileSystemLoader(template_paths, followlinks=True),
            autoescape=select_autoescape(),
            enable_async=True,
        )

        # Load ontologies from repository
        self.world = RepoWorld.from_repo(repo_path)

        # Store output path
        self._logger.debug("Outputting to $s", output_path)

        self.repo_path = repo_path
        self.output_path = output_path

    @staticmethod
    def get_rel_path_from_url(url: ParseResult | str, with_fragment: bool = True) -> Path:
        """Get a relative path from the URL, including its netloc."""
        if not isinstance(url, ParseResult):
            url = urlparse(url)

        name = url.path.strip("/")
        if with_fragment and url.fragment:
            name += f"_{url.fragment}".strip("/").replace("/", "_")

        path = Path(url.netloc) / Path(name)

        return path

    def get_output_path(self, ontology: Ontology, create: bool = True) -> Path:
        """Get the output path for one ontology."""
        path = self.output_path / self.get_rel_path_from_url(ontology.base_iri)
        if create:
            self._logger.debug("Creating %s", path)
            path.mkdir(parents=True, exist_ok=True)
        return path

    @staticmethod
    async def get_template_names(thing: Any, fallbacks: list[str] | None = None) -> list[str]:
        """Decide what template filenames to try for a thing."""
        extensions = (".html.j2", ".html")
        base_names = [
            str(OntoSiteBuilder.get_rel_path_from_url(thing.iri or thing.base_iri)),
            thing.name,
        ]

        template_names = []
        for base_name in base_names:
            template_names += [base_name + ext for ext in extensions]
        for parent in thing.is_a or []:
            template_names += await OntoSiteBuilder.get_template_names(parent)
        for base_name in fallbacks or []:
            template_names += [base_name + ext for ext in extensions]

        return template_names

    @build_format("text/html")
    async def build_ontology_html(self, ontology: Ontology | str, filename: str = "index.html"):
        """Build one ontology to one HTML file."""
        if not isinstance(ontology, Ontology):
            ontology = self.world.get_ontology(ontology)
        self._logger.info("<%s> Building ontology as HTML", ontology.base_iri)

        # Render all ontology things
        context = {"ontology": ontology, "repo": self.world}
        for attr in ("classes", "individuals"):
            context[attr] = {}
            for thing in getattr(ontology, attr)():
                self._logger.info("  <%s> Rendering thing", thing.iri)

                template_names = await self.get_template_names(thing)
                template = self.template_env.select_template(template_names)
                self._logger.info("  <%s> Using template %s", thing.iri, template.filename)

                context[attr][thing.name] = {
                    "thing": thing,
                    "href": f"#{thing.name}"
                    if thing.iri.startswith(ontology.base_iri)
                    else thing.iri,
                }
                context[attr][thing.name]["html"] = await template.render_async(
                    thing=thing, ontology=ontology, repo=self.world
                )

        # Render full ontology page
        template_names = await self.get_template_names(ontology, fallbacks=["Ontology"])
        template = self.template_env.select_template(template_names)
        self._logger.info("<%s> Using template %s", ontology.base_iri, template.filename)
        output_dir = self.get_output_path(ontology)
        output_path = output_dir / filename
        self._logger.info("<%s> Writing output to %s", ontology.base_iri, output_path)
        with output_path.open("w") as output_file:
            async for chunk in template.generate_async(context):
                output_file.write(chunk)

    @build_format("application/rdf+xml")
    async def build_ontology_rdf(
        self, ontology: Ontology | str, filename: str | None = "index.rdf"
    ):
        """Build one ontology to one RDF file."""
        if not isinstance(ontology, Ontology):
            ontology = self.world.get_ontology(ontology)
        self._logger.info("<%s> Building ontology as RDF/XML", ontology.base_iri)

        output_dir = self.get_output_path(ontology)
        output_path = output_dir / filename
        self._logger.info("<%s> Writing output to %s", ontology.base_iri, output_path)
        with output_path.open("wb") as output_file:
            ontology.save(output_file, format="rdfxml")

    async def build_all(self):
        """Build all ontologies in a repository."""
        self._logger.info("Building ontologies from %s into %s", self.repo_path, self.output_path)

        seen = set()
        for ontology in self.world.ontologies.values():
            if ontology in seen:
                continue

            for mime_type, build_func in _format_map.items():
                await build_func(self, ontology)

            seen.add(ontology)
