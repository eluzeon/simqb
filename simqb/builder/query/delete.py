from simqb.builder.mixins.condition import ConditionMixin
from simqb.builder.node import Node


class DeleteQuery(Node, ConditionMixin):
    def __init__(self, target: str):
        super().__init__()
        self.target = target

    def build(self) -> str:
        s = "DELETE FROM {} ".format(self.target)
        if self._where:
            s += "WHERE {}".format(self._where.build())
        return s.strip()


delete = DeleteQuery
