#!/usr/bin/env python3

"""
** Helper for serialisation of assembly graph **
------------------------------------------------
"""

import inspect
import pathlib

import networkx

from cutcutcodec.core.classes.node import Node
from cutcutcodec.utils import get_project_root



def _node_cls_to_string(cls: type) -> str:
    """
    ** Convert a Node class in str. **

    Bijection with ``cutcutcodec.core.compilation.json_to_graph._string_to_node_cls`` function.

    Parameters
    ----------
    cls : type
        The cutcutcodec.core.classes.node.Node subclass.

    Returns
    -------
    str
        The relative import path of the class.

    Examples
    --------
    >>> from cutcutcodec.core.compilation.graph_to_json import _node_cls_to_string
    >>> from cutcutcodec.core.classes.node import Node
    >>> _node_cls_to_string(Node)
    'classes.node.Node'
    >>>
    """
    assert issubclass(cls, Node), cls.__name__
    root_parts = pathlib.Path(
        inspect.getsourcefile(cls)).resolve().relative_to(get_project_root() / "core"
    ).with_suffix("").parts
    cls_str = ".".join(root_parts) + "." + cls.__name__
    return cls_str


def graph_to_json(graph: networkx.MultiDiGraph) -> dict[str]:
    """
    ** Creates the complete json serializable dictionary of the assembly graph. **

    Reverse operation with ``cutcutcodec.core.compilation.json_to_graph.json_to_graph`` function.

    Parameters
    ----------
    graph : networkx.MultiDiGraph
        The assembly graph.

    Returns
    -------
    dict[str]
        The equivalent graph (without cache) in the dictionary form.

    Examples
    --------
    >>> from pprint import pprint
    >>> from cutcutcodec.core.classes.container import ContainerOutput
    >>> from cutcutcodec.core.compilation.graph_to_json import graph_to_json
    >>> from cutcutcodec.core.compilation.tree_to_graph import tree_to_graph
    >>> from cutcutcodec.core.generation.audio.noise import GeneratorAudioNoise
    >>> graph = tree_to_graph(ContainerOutput(GeneratorAudioNoise.default().out_streams))
    >>> pprint(graph_to_json(graph))
    {'edges': [['generator_audio_noise_1', 'container_output_1', '0->0']],
     'nodes': {'container_output_1': {'class': 'classes.container.ContainerOutput',
                                      'state': {}},
               'generator_audio_noise_1': {'class': 'generation.audio.noise.GeneratorAudioNoise',
                                           'state': {'seed': 0.0}}}}
    >>>
    """
    assert isinstance(graph, networkx.MultiDiGraph), graph.__class__.__name__

    json_dict = {
        "edges": sorted((list(e) for e in graph.edges)),
        "nodes": {
            node: {
                "class": _node_cls_to_string(data["class"]),
                "state": data["state"],
            }
            for node, data in graph.nodes.data()
        }
    }
    return json_dict
