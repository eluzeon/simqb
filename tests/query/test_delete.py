import pytest

from simqb import delete, eq


@pytest.mark.parametrize("query, sql", (
        (
            delete("users").where(eq("id", 2)),
            "DELETE FROM users WHERE id = 2"
        ),
))
def test_delete_query(query, sql):
    assert str(query) == sql
