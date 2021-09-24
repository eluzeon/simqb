import abc
import enum
import typing

from simqb.builder.node import Node


class ConditionOperator(str, enum.Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self):
        return self.value


class ConditionNode(abc.ABC, Node):
    """
    Base class for condition nodes
    """
    def __init__(self, negated: bool = False):
        self.negated = negated

    def __and__(self, other: 'ConditionNode') -> 'ConditionNode':
        return Condition(self, other, ConditionOperator.AND)

    def __or__(self, other: 'ConditionNode') -> 'ConditionNode':
        return Condition(self, other, ConditionOperator.OR)

    def __invert__(self) -> 'ConditionNode':
        self.negated = not self.negated
        return self


class Condition(ConditionNode):
    def __init__(self, cond1: typing.Optional['ConditionNode'] = None,
                 cond2: typing.Optional['ConditionNode'] = None,
                 op: ConditionOperator = ConditionOperator.AND,
                 *, negated: bool = False):
        super().__init__(negated)
        self.cond1 = cond1
        self.cond2 = cond2
        self.op = op

    def __bool__(self) -> bool:
        return bool(self.cond1) or bool(self.cond2)

    def build(self) -> str:
        s = ""
        if self.cond1:
            s += "{}".format(self.cond1.build())
        if self.cond2:
            s += " {} {}".format(
                str(self.op),
                self.cond2.build()
            )
        if self.negated:
            s = "NOT " + s
        s = s.strip()
        if self.op == ConditionOperator.OR:
            s = "({})".format(s)
        return s
