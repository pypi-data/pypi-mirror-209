from loguru import logger
import numpy as np
from onnx import helper


from .base_layer import BaseLayer


class UnsqueezeFunc(BaseLayer):
    def __init__(self, source_node, module=None, auto_gen=True):
        super(UnsqueezeFunc, self).__init__(source_node, module, auto_gen)

    def generate_node(self, name=None, params=None, attr_dict=None):
        if name is not None:
            self._name = name

        if params is None:
            axes = self._source_node.args[1]
            params = np.array([axes])

        self.create_params(self._name + "_unsqueeze", params)
        node = helper.make_node(
            "Unsqueeze", self._in_names, self._out_names, self._name
        )

        logger.info(f"{self.__class__.__name__}: {self._name} created")
        self._node.append(node)
