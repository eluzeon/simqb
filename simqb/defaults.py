import typing

from simqb.builder.nodes.join import Join
from simqb.builder.node import Node, NodeType
from simqb.exceptions import NodeNotRegistered


_registry: typing.Dict[NodeType, typing.Type[Node]] = {
    NodeType.JOIN: Join,
}


def get_node(node_type: NodeType) -> typing.Type[Node]:
    node = _registry.get(node_type)
    if node is None:
        raise NodeNotRegistered(
            "node for {} type is not registered. Did you override it? Check it is correctly overridden"
            .format(str(node_type))
        )
    return node


def override_default(node: NodeType, cls: typing.Type[Node]) -> None:
    """
    Overrides default nodes to custom one.
    Should be called before usage and once.
    Example usage.
    >>> override_default(NodeType.JOIN, MyCustomJoinNode)
    """
    _registry[node] = cls


def overrides_default(node: NodeType) -> typing.Callable[[typing.Type[Node]], typing.Type[Node]]:
    """
    Same as override_default but can be used as decorator for class
    Example usage
    >>> @overrides_default(NodeType.JOIN)
    ... class MyCustomJoinNode(Node):
    ...     ...
    """
    def _wrapper(wrap: typing.Type[Node]) -> typing.Type[Node]:
        override_default(node, wrap)
        return wrap
    return _wrapper
