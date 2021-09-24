import abc
import typing

from simqb.builder.nodes.condition import ConditionNode


class BinaryOperator(ConditionNode, abc.ABC):
    operator = ""

    def __init__(self, op1: str, op2: typing.Any):
        super().__init__()
        self.op1 = op1
        self.op2 = op2

    def build(self) -> str:
        return "{} {} {}".format(
            self.op1,
            self.operator,
            str(self.op2)
        )


class Equal(BinaryOperator):
    operator = "="


class Less(BinaryOperator):
    operator = "<"


class LessOrEqual(BinaryOperator):
    operator = "<="


class Greater(BinaryOperator):
    operator = ">"


class GreaterOrEqual(BinaryOperator):
    operator = ">="


class RawCondition(ConditionNode):
    def __init__(self, raw: str):
        super().__init__()
        self.raw = raw

    def build(self) -> str:
        return self.raw


eq = Equal
lt = Less
gt = Greater
lte = LessOrEqual
gte = GreaterOrEqual
