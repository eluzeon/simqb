## [Sim]ple[Q]uery[B]uilder

----
This project is Work in progress
-----
Simple python 3.6+ query builder

### Features:
- Typed (Python 3.6+)
- Flexible
- Lightweight


## 1. Selecting data
You can create select query like this:
```python3
from simqb import select, eq

query = select("users")
print(query)  # SELECT * FROM users

query = select("user").fields("name", "age")
print(query)  # SELECT name, age FROM user

query = select("user").where(eq('name', 4) | eq('name', 10))
print(query)  # SELECT * FROM user WHERE name = 4 OR name = 10
```