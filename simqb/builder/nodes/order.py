import enum
import typing

from simqb.builder.node import Node, SimpleNodeSet


class OrderDirection(str, enum.Enum):
    ASC = "ASC"
    DESC = "DESC"


class OrderNullPolicy(str, enum.Enum):
    NULLS_LAST = "NULLS_LAST"
    NULLS_FIRST = "NULLS_FIRST"


class Order(Node):
    def __init__(self, field: str,
                 direction: typing.Optional[OrderDirection] = None,
                 nulls: typing.Optional[OrderNullPolicy] = None):
        self.field = field
        self.direction = direction
        self.nulls = nulls

    def build(self) -> str:
        s = self.field
        if self.direction:
            s += " " + str(self.direction)
        if self.nulls:
            s += " " + str(self.nulls)
        return s.strip()


class OrderSet(SimpleNodeSet[Order]):
    joiner = ", "
