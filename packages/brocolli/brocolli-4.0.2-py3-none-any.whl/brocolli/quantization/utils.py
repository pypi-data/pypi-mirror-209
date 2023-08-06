import re
import numpy as np


def activation_pre_hook(self, input):
    if hasattr(self, "activation_pre_process"):
        self.activation_pre_process(input[0])


def activation_post_hook(self, input, output):
    if hasattr(self, "activation_post_process"):
        self.activation_post_process(output)


def _parent_name(target):
    """
    Splits a qualname into parent path and last atom.
    For example, `foo.bar.baz` -> (`foo.bar`, `baz`)
    """
    *parent, name = target.rsplit(".", 1)
    return parent[0] if parent else "", name


def replace_node_module(node, modules, new_module):
    assert isinstance(node.target, str)
    parent_name, name = _parent_name(node.target)
    setattr(modules[parent_name], name, new_module)


def get_function_name(node_target):
    function_name = re.findall(
        r"(?:function|method) ([a-z|_|0-9]+.*?)", str(node_target)
    )[0]

    return function_name


def create_target(graph_module, node):
    num = 0
    candidate = node.target
    while 1:
        try:
            target_mod = graph_module.graph.owning_module.get_submodule(candidate)
            candidate = f"{node.target}_{num}"
            num += 1
        except Exception as e:
            break

    return candidate


def check_result(actual, desired):
    assert len(actual) == len(desired), "actual: %d vs desired %d" % (
        len(actual),
        len(desired),
    )

    for idx in range(len(actual)):
        np.testing.assert_allclose(
            actual[idx].cpu().detach().numpy(),
            desired[idx].cpu().detach().numpy(),
            rtol=1e-7,
            atol=1e-3,
        )


def _node_dict(graph_module):
    return {n.name: n for n in graph_module.graph.nodes}
