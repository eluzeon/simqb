import typing

from simqb.builder.node import Node, SimpleNodeSet


class Field(Node):
    def __init__(self, name: str, alias: typing.Optional[str] = None, alias_var: str = "as"):
        self.name = name
        self.alias = alias
        self.alias_var = alias_var

    def build(self) -> str:
        if self.alias is None:
            return self.name
        return "{} {} {}".format(self.name, self.alias_var, self.alias)


class FieldSet(SimpleNodeSet[Field]):
    joiner = ", "

    def build_empty(self) -> str:
        return "*"
