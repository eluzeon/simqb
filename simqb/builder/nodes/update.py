import typing

from simqb.builder.node import Node, SimpleNodeSet


class Update(Node):
    def __init__(self, field: str, value: typing.Any):
        self.field = field
        self.value = value

    def build(self) -> str:
        return "{} = {}".format(self.field, self.value)


class UpdateSet(SimpleNodeSet[Update]):
    joiner = ", "
