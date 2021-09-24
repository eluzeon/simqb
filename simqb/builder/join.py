import enum

from simqb.builder.node import Node, SimpleNodeSet


class JoinType(str, enum.Enum):
    INNER = "INNER"
    OUTER = "OUTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    FULL = "FULL"


class Join(Node):
    def __init__(self, target: str, on: str, join_type: JoinType):
        self.target = target
        self.join_type = join_type
        self.on = on

    def build(self) -> str:
        return "{join_type} JOIN {target} ON {on}"\
            .format(join_type=self.join_type,
                    target=self.target,
                    on=self.on)


class JoinSet(SimpleNodeSet[Join]):
    joiner = " "
