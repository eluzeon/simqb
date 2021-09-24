import typing

from simqb.builder.conditions.op import RawCondition
from simqb.builder.conditions.where import Condition, ConditionNode
from simqb.builder.join import Join, JoinType, JoinSet
from simqb.builder.node import RawNode
from simqb.builder.order import Order, OrderSet
from simqb.builder.query import Query
from simqb.builder.select.fields import Field, FieldSet


class SelectQuery(Query):
    statement = "SELECT"

    def __init__(self, target: str, *, for_update: bool = False):
        super().__init__(target)
        self.for_update = for_update
        self._where: ConditionNode = Condition()
        self._values = FieldSet()
        self._joins = JoinSet()
        self._orders = OrderSet()

    def fields(self, *fields: typing.Union[str, Field]) -> 'SelectQuery':
        for field in fields:
            if isinstance(field, str):
                self._values.add(Field(field))
            else:
                self._values.add(field)
        return self

    def build(self) -> str:
        query = "SELECT {fields} FROM {target} "\
            .format(fields=self._values.build(),
                    target=self.target)
        if self._joins:
            query += self._joins.build()
        if self._where:
            query += "WHERE {}".format(self._where.build())
        return query.strip()

    def join(self, target: str, on: str, join_type: JoinType = JoinType.INNER) -> 'SelectQuery':
        self._joins.add(Join(target, on, join_type))
        return self

    def order_by(self, *fields: typing.Union[str, Order]) -> 'SelectQuery':
        for field in fields:
            if isinstance(field, str):
                self._orders.add(Order(field))
            else:
                self._orders.add(field)
        return self

    def where(self, condition: ConditionNode) -> 'SelectQuery':
        self._where = condition
        return self

    def raw_where(self, condition: str) -> 'SelectQuery':
        self._where &= RawCondition(condition)
        return self
