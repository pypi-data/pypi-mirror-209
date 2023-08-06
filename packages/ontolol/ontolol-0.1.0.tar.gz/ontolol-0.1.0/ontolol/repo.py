import logging
from pathlib import Path
from typing import Any, Iterable, Optional

from owlready2 import Ontology, World
from rdflib import Graph
from rdflib.namespace import OWL, RDF


class ResolverError(ValueError):
    """Raised when the resolver could not reliably determine a dependency order."""

    from_: Any
    to: Any

    def __init__(self, from_: Any, to: Any, /, *args, **kwargs):
        self.from_ = from_
        self.to = to

        super().__init__(*args, **kwargs)


class RenderableOntology(Ontology):
    """OWLReady ontology with utilities for rendering."""

    @property
    def title(self) -> str:
        if self.metadata.label:
            return self.metadata.label[0]

        return self.name


class RepoWorld(World):
    """An OWLReady2 world linked to a repository path."""

    root: Ontology | None

    _repo_map: dict[str, tuple[Path, set[str]]]
    _load_order: list[str] | None

    def __init__(self):
        super().__init__()

        self._logger = logging.getLogger(__name__)

        self._repo_map = {}
        self._load_order = None
        self.root = None

    @classmethod
    def from_repo(cls, repo_path: Path | str) -> "RepoWorld":
        """Load all ontologies from a "repository" of RDF files.

        Scans the directory recursively for RDF/XML files and loads them.
        """
        if not isinstance(repo_path, Path):
            repo_path = Path(repo_path)

        world = cls()
        for rdf_file in repo_path.rglob("*.rdf"):
            # Register ontology so we can resolve import order
            world.register_ontology_file(rdf_file)

        # Load all ontologies from files
        world.load_registered_ontologies()

        return world

    def guess_root(self) -> Ontology:
        """Set the ontology repo root by looking at dependency order."""
        self.root = self.get_ontology(self.get_dependency_order()[0])
        return self.root

    def load_registered_ontologies(self):
        """Load all registered ontologies in dependency order."""
        for ontology in self.get_dependency_order():
            rdf_file = self._repo_map[ontology][0]
            self.get_ontology(rdf_file.absolute().as_uri(), OntologyClass=RenderableOntology).load()

        self.guess_root()

    def register_ontology_file(self, rdf_file: Path):
        """Register an RDF/XML file as one ontology.

        This will load the ontology into rdflib to extract its dependencies.
        """

        # Invalidate dependency cache
        self._load_order = None

        # Load ontology into rdflib graph
        # We use rdflib because it is not OWL-aware, and thus works without resolving imports
        graph = Graph()
        graph.parse(rdf_file)

        # Find all ontologies in file
        for ontology_iri in graph.subjects(RDF.type, OWL.Ontology):
            imports = set()
            for imported_iri in graph.objects(ontology_iri, OWL.imports):
                imports.add(str(imported_iri))

        # Add to repo map
        if str(ontology_iri) in self._repo_map:
            raise ValueError(f"Ontology {ontology_iri} defined more than once")
        self._repo_map[str(ontology_iri)] = (rdf_file, imports)

    def get_dependency_order(
        self,
        ontologies: Optional[Iterable[str]] = None,
        order: Optional[list[str]] = None,
        seen: Optional[set[str]] = None,
    ) -> list[Path]:
        """ "Get the order in which ontologies have to be loaded from files."""
        if ontologies is None and self._load_order is not None:
            return self._load_order

        save_load_order = False
        if ontologies is None:
            save_load_order = True
            ontologies = self._repo_map.keys()
        if order is None:
            order = []
        if seen is None:
            seen = set()

        for ontology in ontologies:
            if ontology in order:
                continue

            for ontology_dep in self._repo_map[ontology][1]:
                if ontology_dep in order:
                    continue
                if ontology_dep in seen:
                    raise ResolverError(
                        ontology,
                        ontology_dep,
                        f"Circular dependency when resolving {ontology} -> {ontology_dep}",
                    )
                seen.add(ontology_dep)
                self.get_dependency_order([ontology_dep], order, seen)

            order.append(ontology)
            if ontology in seen:
                seen.remove(ontology)

        if save_load_order:
            self._load_order = order
        return order
