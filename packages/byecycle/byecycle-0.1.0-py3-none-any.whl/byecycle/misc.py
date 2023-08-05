from typing import TypedDict, TypeAlias, Literal, Iterable

Edges: TypeAlias = list[tuple[str, str]]
EdgeKind: TypeAlias = Literal["good", "bad", "complicated", "skip"]
ImportKind: TypeAlias = Literal["dynamic", "conditional", "typing", "parent"]
edge_order: dict[EdgeKind, int] = {"bad": 0, "complicated": 1, "good": 2, "skip": 3}
default_cycle_severity: dict[ImportKind, EdgeKind] = {
    "dynamic": "complicated",
    "conditional": "complicated",
    "typing": "skip",
    "parent": "complicated",
}


def cycle_severity(
    cycles: Iterable[ImportKind], **kwargs: dict[ImportKind, EdgeKind]
) -> EdgeKind | None:
    if not cycles:
        return None
    severity_map = {**default_cycle_severity, **kwargs}
    severity = sorted((severity_map[c] for c in cycles), key=edge_order.get)
    return severity[0]


class EdgeConfig(TypedDict):
    dynamic_imports: EdgeKind
    conditional_imports: EdgeKind
    typing_imports: EdgeKind
    parent_imports: EdgeKind


def filename_to_module_path(path: str, base: str, name: str):
    """Turns a file path into a valid module name.

    Notes:
        - test if namespaces are handled correctly
        - if the distro name is different from the base, things won't work
        - multiple distros in a package... what do?
    """
    return (
        path.removeprefix(base[: -len(name)])
        .removesuffix(".py")
        .removesuffix("__init__")
        .strip("/")
        .replace("/", ".")
    )
