import datetime

import pytest

from simqb import update, gt


@pytest.mark.parametrize("query, sql", (
        (
            update("users")
                .set(is_active=True)
                .where(gt("age", 18)),
            "UPDATE users SET is_active = True WHERE age > 18"
        ),
))
def test_update_query(query, sql):
    assert str(query) == sql

