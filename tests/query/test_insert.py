import pytest

from simqb import insert


@pytest.mark.parametrize("query, sql", (
        (
            insert("users")
                .fields("id", "name", "age")
                .values(1, "Timur", 18),
            "INSERT INTO users(id, name, age) VALUES (1, 'Timur', 18)"
        ),
))
def test_insert_query(query, sql):
    assert str(query) == sql
