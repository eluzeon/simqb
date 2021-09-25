from simqb.builder import mixins
from simqb.builder.node import Node


class InsertQuery(mixins.FieldsMixin,
                  mixins.ValueMixin,
                  Node):
    def __init__(self, target: str):
        super().__init__()
        self.target = target

    def build(self) -> str:
        s = "INSERT INTO {}".format(self.target)
        if self._fields:
            s += "({}) ".format(self._fields.build())
        if self._values:
            s += "VALUES ({})".format(self._values.build())
        return s.strip()


insert = InsertQuery
