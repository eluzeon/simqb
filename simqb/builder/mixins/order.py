import typing

from simqb.builder.nodes.order import OrderSet, Order


class OrderMixin:
    def __init__(self):
        super().__init__()
        self._orders = OrderSet()

    def order_by(self, *fields: typing.Union[str, Order]) -> 'OrderMixin':
        for field in fields:
            if isinstance(field, str):
                self._orders.add(Order(field))
            else:
                self._orders.add(field)
        return self
