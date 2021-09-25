from simqb.builder.mixins import ConditionMixin
from simqb.builder.mixins import FieldsMixin
from simqb.builder.mixins import JoinMixin
from simqb.builder.mixins import OrderMixin
from simqb.builder.node import Node


class SelectQuery(FieldsMixin,
                  ConditionMixin,
                  JoinMixin,
                  OrderMixin,
                  Node):
    def __init__(self, target: str, *, for_update: bool = False):
        super().__init__()

        self.target = target
        self.for_update = for_update

    def build(self) -> str:
        query = "SELECT {fields} FROM {target} " \
            .format(fields=self._fields.build(),
                    target=self.target)
        if self._joins:
            query += self._joins.build()
        if self._where:
            query += "WHERE {}".format(self._where.build())
        return query.strip()


select = SelectQuery
