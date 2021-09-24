import abc
import enum
import typing


class Node:
    @abc.abstractmethod
    def build(self) -> str:
        """
        Compiles itself to sql string
        """
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.build()


class NodeType(str, enum.Enum):
    JOIN = "JOIN"
    WHERE = "WHERE"


class RawNode(Node):
    def __init__(self, raw: str):
        self.raw = raw

    def build(self) -> str:
        return self.raw


T = typing.TypeVar("T", bound=Node)


class SimpleNodeSet(Node, typing.Generic[T]):
    joiner: str = " "

    def __init__(self, *nodes: T):
        self.nodes = list(nodes)

    def add(self, node: T) -> None:
        self.nodes.append(node)

    def build_empty(self) -> str:
        return ""

    def build(self) -> str:
        if not self.nodes:
            return self.build_empty()
        return self.joiner.join((node.build() for node in self.nodes))

    def __bool__(self) -> bool:
        return bool(self.nodes)
