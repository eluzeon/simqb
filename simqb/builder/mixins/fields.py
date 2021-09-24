import typing

from simqb.builder.nodes.fields import FieldSet, Field


class FieldsMixin:
    def __init__(self):
        super().__init__()
        self._fields = FieldSet()

    def fields(self, *fields: typing.Union[str, Field]) -> 'FieldsMixin':
        for field in fields:
            if isinstance(field, str):
                self._fields.add(Field(field))
            else:
                self._fields.add(field)
        return self
