import typing

from simqb.builder.nodes import ValueSet, Value


class ValueMixin:
    def __init__(self):
        super().__init__()
        self._values = ValueSet()

    def values(self, *values: typing.Union[Value, typing.Any]) -> 'ValueMixin':
        for v in values:
            if not isinstance(v, Value):
                self._values.add(Value(v))
            else:
                self._values.add(v)
        return self
