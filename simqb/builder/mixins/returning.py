import typing

from simqb.builder.nodes.fields import FieldSet, Field


class ReturningMixin:
    def __init__(self):
        self._returning = FieldSet()

    def returning(self, *fields: typing.Union[str, Field]) -> 'ReturningMixin':
        for field in fields:
            if isinstance(field, str):
                self._returning.add(Field(field))
            else:
                self._returning.add(field)
        return self
