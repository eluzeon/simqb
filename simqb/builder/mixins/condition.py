from simqb.builder.nodes.condition import Condition, ConditionNode
from simqb.builder.operators import RawCondition


class ConditionMixin:
    def __init__(self):
        super().__init__()
        self._where: ConditionNode = Condition()

    def where(self, condition: ConditionNode) -> 'ConditionMixin':
        self._where = condition
        return self

    def raw_where(self, condition: str) -> 'ConditionMixin':
        self._where &= RawCondition(condition)
        return self
