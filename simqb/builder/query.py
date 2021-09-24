import abc
import typing

from simqb.builder.node import Node


class Query(abc.ABC, Node):
    def __init__(self, target: str):
        self.target = target

    def __str__(self) -> str:
        return self.build()


class UpdateQuery(Query):
    pass


class DeleteQuery(Query):
    pass


class InsertQuery(Query):
    pass
