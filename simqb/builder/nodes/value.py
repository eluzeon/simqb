import typing

from simqb.builder.node import Node, SimpleNodeSet


class Value(Node):
    def __init__(self, value: typing.Any):
        self.value = value

    def build(self) -> str:
        if isinstance(self.value, str):
            return "'{}'".format(self.value)
        return str(self.value)


class ValueSet(SimpleNodeSet[Value]):
    joiner = ", "
