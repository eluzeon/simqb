import pytest

from simqb import select, eq, gt, lt
from simqb.builder.nodes.fields import Field


@pytest.mark.parametrize("query, string", (
        (
            select("users").where(eq("name", 2)),
            "SELECT * FROM users WHERE name = 2"
        ),
        (
            select("users")
                .fields("id", "name", "age")
                .where(eq("name", 2) & gt("age", 16)),
            "SELECT id, name, age FROM users WHERE name = 2 AND age > 16"
        ),
        (
            select("users")
                .fields(Field("name", "user_name"), "age as ag")
                .where((eq("name", 2) | eq("name", 3)) & lt("age", 50)),
            "SELECT name as user_name, age as ag FROM users WHERE (name = 2 OR name = 3) AND age < 50"
        )
))
def test_select_query(query, string):
    assert str(query) == string
