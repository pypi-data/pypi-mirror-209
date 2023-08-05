import typer
from pathlib import Path
from typing import Annotated

from rich import print, print_json

from byecycle.misc import EdgeKind
from byecycle.graph import solve

cli = typer.Typer(rich_markup_mode="rich")


@cli.command()
def run(
    project: Path,
    dynamic: Annotated[str, typer.Option(help=f"One of {EdgeKind}")] = "complicated",
    conditional: Annotated[str, typer.Option(help=f"One of {EdgeKind}")] = "complicated",
    typing: Annotated[str, typer.Option(help=f"One of {EdgeKind}")] = "skip",
    parent: Annotated[str, typer.Option(help=f"One of {EdgeKind}")] = "complicated",
    draw: Annotated[bool, typer.Option(help=f"Flag which, if set, will draw the resulting import graph with matplotlib and write it to disk.")] = False,
):
    """Run import-cycle-detection for a python project.

    A json-string will be printed to stdout containing a rich import listing which can be
    used for further analysis.

    The treatment of the following types of import statements can be customized to one of
    four treatments, depending on the kind of cycle issues your project is having:

    - dynamic: An import which takes place in a function
    - conditional: A top-level import guarded by an arbitrary if-statement
    - typing: A top-level import that only takes place in static type analysis
    - parent: A top-level parent-module import, which happens by default in a nested structure
    - vanilla: A normal import which doesn't fall into any of the former categories
    """
    graph = solve(str(project), dynamic=dynamic, conditional=conditional, typing=typing, parent=parent)
    print_json(data={k: {**graph[k]} for k in graph})
    if draw:
        from byecycle.draw import draw_graph
        graph_path, legend_path = draw_graph(project.name, graph)
        print(f"Saved graph image at ", end="")
        print(graph_path.resolve())
        print("Saved graph legend at ", end="")
        print(legend_path.resolve())


if __name__ == '__main__':
    run(Path("/home/arne/dev/griffe/src/griffe"), draw=True)




