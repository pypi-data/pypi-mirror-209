from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import ast
from typing import Iterable

import networkx as nx

from byecycle.misc import EdgeKind, ImportKind, cycle_severity, filename_to_module_path


class Module:
    _modules: list["Module"] = list()
    _sorted: bool = False

    def __init__(self, name: str):
        self.name: str = name
        Module._modules.append(self)
        self.imports: dict[Module : set[ImportKind]] = defaultdict(set)

    def add(self, other: "Module" | str, tags: list[ImportKind]):
        """Add an import to this Module.

        This method can only be called once all Modules have been instantiated.

        Args:
            other: A modules, either as an object or as a string that will be evaluated as
                its longest match from all valid module names. Valid strings are fully
                qualified import arguments, i.e. `"foo.bar"` from `import foo.bar` or
                `"foo.bar.baz"` from `from foo.bar import baz`. If `foo.bar` is a
                registered module with name `baz` in it, both strings would add the module
                `foo.bar` as an import.
            tags: Describes the kind of import, e.g. import of module `foo` has the
                tags `typing` and `parent`, meaning it is the import of a parent module
                within an `if typing.TYPE_CHECKING` block, which will be important
                information once we want to visualize the severity of certain cyclic
                imports.
        """
        if not Module._sorted:
            # sort in descending alphabetical order, so that the longest match is found
            # first
            Module._modules.sort(key=lambda n: n.name, reverse=True)
            Module._sorted = True

        if isinstance(other, Module):
            self.imports[other].update(tags)
            return
        if isinstance(other, str):
            for node in Module.modules():
                if other.startswith(node.name):
                    self.imports[node].update(tags)
                    return

    def __hash__(self):
        return self.name.__hash__()

    def __repr__(self):
        imports = {
            k.name: v if v else "∅"
            for k, v in sorted(
                self.imports.items(), key=lambda x: x[0].name, reverse=True
            )
        }
        return f"Module('{self.name}') -> {imports}"

    @classmethod
    def modules(cls) -> Iterable["Module"]:
        """Accessor for all registered modules."""
        yield from cls._modules

    @classmethod
    def add_parent_imports(cls):
        """Make modules with parent packages import them explicitly.

        While the parent package's name doesn't automatically exist in a module's
        namespace, any import like `from foo.bar import baz` will, before `baz` is
        resolved, import `foo.bar` -- which in turn needs an import of `foo` before that.

        Treating their reliance chain as _imports_ models this link accurately for the
        most part, but does create the impression of cycles if a parent imports names from
        a child, which is a popular pattern for simplifying/exposing a public API. As a
        consequence, these child-parent imports should be treated differently during
        analysis.

        See Also:
            https://discuss.python.org/t/question-understanding-imports-a-bit-better-how-are-cycles-avoided/26647/2

        Notes:
            This method can only be called once all Nodes have been initialised.
        """
        nodes: dict[str, Module] = {node.name: node for node in cls.modules()}
        for node in cls.modules():
            package = node.name.rsplit(".", 1)[
                0
            ]  # only direct parent, not grandparents
            if package in nodes:
                node.add(nodes[package], ["parent"])


class ImportVisitor(ast.NodeVisitor):
    def __init__(self):
        self.imports: list[tuple[str, list[ImportKind]]] = []

    @classmethod
    def find_import_kinds(cls, node: ast.Import | ast.ImportFrom) -> list[ImportKind]:
        ret: list[ImportKind] = []
        parent: ast.AST = node.parent
        # conditional top-level module imports
        if isinstance(parent, ast.If) and isinstance(parent.parent, ast.Module):
            # guarded by `if typing.TYPE_CHECKING:`
            if isinstance(parent.test, ast.Name):
                if parent.test.id == "TYPE_CHECKING":
                    ret.append("typing")
            elif isinstance(parent.test, ast.Attribute):
                if parent.test.attr == "TYPE_CHECKING":
                    ret.append("typing")
            # probably guarded by `if sys.version >= (x, y, z):`, but doesn't actually
            # matter -- anything but TYPE_CHECKING is env-dependent during runtime or
            # too obtuse to consider (I'm not writing code that checks for `if True:`)
            else:
                ret.append("conditional")
        else:
            # test if the import happens somewhere in a function
            current = parent
            while hasattr(current, "parent"):
                if isinstance(current, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    ret.append("dynamic")
                    break
                current = current.parent
            else:
                # any nodes that reach this point are treated as regular toplevel imports,
                # like imports that happen in a class body
                pass
        return ret

    def visit_Import(self, node: ast.Import):
        kinds = self.find_import_kinds(node)
        for alias in node.names:
            self.imports.append((alias.name, kinds))

    def visit_ImportFrom(self, node: ast.ImportFrom):
        kinds = self.find_import_kinds(node)
        for alias in node.names:
            self.imports.append((f"{node.module}.{alias.name}", kinds))


def import_map(package: str) -> list[Module]:
    """Creates a directed graph of import statements.

    Args:
        package: Path to the source root, e.g. "/home/dev/my_lib/src/my_lib"

    Returns:
        Mapping of python module names to a list of all module names that it imports
    """
    node_data: dict[Module, list[tuple[str, list[ImportKind]]]] = {}
    package_name = Path(package).name

    for path in map(str, Path(package).rglob("*")):
        if not path.endswith(".py"):
            continue
        name = filename_to_module_path(path, package, package_name)

        with open(path) as f:
            ast_ = ast.parse(f.read())
        for node in ast.walk(ast_):
            for child in ast.iter_child_nodes(node):
                child.parent = node
        # ast_ = AddParentLink().visit(ast_)
        visitor = ImportVisitor()
        visitor.visit(ast_)
        node_data[Module(name)] = [
            (m, t) for m, t in visitor.imports if m.startswith(package_name)
        ]
    Module.add_parent_imports()

    # add all found imports to their respective module
    for node, imports in node_data.items():
        for import_, kinds in imports:
            node.add(import_, kinds)

    return [*Module.modules()]


def build_digraph(modules: list[Module], **kwargs: dict[ImportKind, EdgeKind]) -> nx.DiGraph:
    """Turns a module-imports-mapping into a smart graph object."""
    g = nx.DiGraph()
    g.add_nodes_from([m.name for m in modules])
    for module in modules:
        for import_, tags in module.imports.items():
            g.add_edge(module.name, import_.name, severity=cycle_severity(tags, **kwargs))

    for e_0, e_1 in g.edges():
        if g.has_edge(e_1, e_0):
            g[e_0][e_1].update(cycle=True)
        else:
            g[e_0][e_1].update(cycle=False)

    return g


def solve(
    path: str,
    *,
    dynamic: EdgeKind = "complicated",
    conditional: EdgeKind = "complicated",
    typing: EdgeKind = "skip",
    parent: EdgeKind = "complicated",
) -> nx.DiGraph:
    modules = import_map(
        path
    )
    return build_digraph(modules,
        dynamic=dynamic,
        conditional=conditional,
        typing=typing,
        parent=parent,)
