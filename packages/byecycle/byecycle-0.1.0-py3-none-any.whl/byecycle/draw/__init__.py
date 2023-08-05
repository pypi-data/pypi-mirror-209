from chextra import warn

warn()

from pathlib import Path

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as clrs
import matplotlib.patches as ptc

DEFAULT_COLORS = {
    "no_cycle": "black",
    "good": "green",
    "bad": "red",
    "complicated": "yellow",
}


def draw_graph(package: str, g: nx.DiGraph) -> tuple[Path, Path]:
    graph_path = Path(f"{package}.png")
    legend_path = Path(f"{package}_legend.png")

    all_colors = list(clrs.CSS4_COLORS)
    ratio = 0 if not g.nodes() else len(all_colors) / len(g.nodes())
    colors = {k: all_colors[int(i * ratio)] for i, k in enumerate(g.nodes())}

    # draw and store digraph visualization
    layout = nx.kamada_kawai_layout(g)
    nx.draw_networkx_nodes(
        g,
        pos=layout,
        node_color=colors.values(),
        node_shape="o",
    )
    nx.draw_networkx_edges(
        g,
        pos=layout,
        edge_color=DEFAULT_COLORS["no_cycle"],
        arrows=True,
        edgelist=[(e_0, e_1) for e_0, e_1 in g.edges if not g[e_0][e_1]["cycle"]],
    )
    nx.draw_networkx_edges(
        g,
        pos=layout,
        edge_color=DEFAULT_COLORS["good"],
        arrows=False,
        edgelist=[
            (e_0, e_1)
            for e_0, e_1 in g.edges
            if g[e_0][e_1]["cycle"] and g[e_0][e_1]["severity"] == "good"
        ],
    )
    nx.draw_networkx_edges(
        g,
        pos=layout,
        edge_color=DEFAULT_COLORS["bad"],
        arrows=False,
        edgelist=[
            (e_0, e_1)
            for e_0, e_1 in g.edges
            if g[e_0][e_1]["cycle"] and g[e_0][e_1]["severity"] == "bad"
        ],
    )
    nx.draw_networkx_edges(
        g,
        pos=layout,
        edge_color=DEFAULT_COLORS["complicated"],
        arrows=False,
        edgelist=[
            (e_0, e_1)
            for e_0, e_1 in g.edges
            if g[e_0][e_1]["cycle"] and g[e_0][e_1]["severity"] == "complicated"
        ],
    )
    plt.title(f"Import graph for {package}")
    plt.savefig(str(graph_path))
    plt.show()

    # store legend
    plt.axis("off")
    plt.legend(
        loc="upper center",
        ncol=2,
        fancybox=True,
        shadow=True,
        handles=[ptc.Patch(color=c, label=l) for l, c in colors.items()],
    )
    plt.savefig(legend_path)

    return graph_path, legend_path
