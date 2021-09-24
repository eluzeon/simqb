from simqb.builder.nodes.join import JoinSet, JoinType, Join


class JoinMixin:
    def __init__(self):
        super().__init__()
        self._joins = JoinSet()

    def join(self, target: str, on: str, join_type: JoinType = JoinType.INNER) -> 'JoinMixin':
        self._joins.add(Join(target, on, join_type))
        return self
