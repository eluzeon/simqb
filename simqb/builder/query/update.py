from simqb.builder.node import Node
from .. import mixins


class UpdateQuery(mixins.ConditionMixin,
                  mixins.ReturningMixin,
                  mixins.JoinMixin,
                  mixins.UpdateMixin,
                  Node):
    def __init__(self, target: str):
        super().__init__()
        self.target = target

    def build(self) -> str:
        s = "UPDATE {} SET {} ".format(self.target, self._update_set.build())
        if self._where:
            s += "WHERE {}".format(self._where.build())
        if self._returning:
            s += "RETURNING {}".format(self._returning.build())
        return s.strip()


update = UpdateQuery
