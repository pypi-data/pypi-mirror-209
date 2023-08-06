from loguru import logger
from onnx import helper

from .base_layer import BaseLayer


class LeakyReluLayer(BaseLayer):
    def __init__(self, source_node, module=None, auto_gen=True):
        super(LeakyReluLayer, self).__init__(source_node, module, auto_gen)

    def get_leakyrelu_attr(self):
        attr_dict = {"alpha": 0}

        attr_dict["alpha"] = float(self._module.negative_slope)

        return attr_dict

    def generate_node(self, name=None, params=None, attr_dict=None):
        attr_dict = self.get_leakyrelu_attr()
        node = helper.make_node(
            "LeakyRelu", self._in_names, self._out_names, self._name, **attr_dict
        )
        logger.info(f"{self.__class__.__name__}: {self._name} created")
        self._node.append(node)
