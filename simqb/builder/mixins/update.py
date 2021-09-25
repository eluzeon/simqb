import typing

from simqb.builder.nodes import UpdateSet, Update


class UpdateMixin:
    def __init__(self):
        super().__init__()
        self._update_set = UpdateSet()

    def set(self, *updates: Update, **values: typing.Any) -> 'UpdateMixin':
        for upd in updates:
            self._update_set.add(upd)
        for field, value in values.items():
            self._update_set.add(Update(field, value))
        return self
