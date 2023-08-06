# simple-wait
Simple wait

[![tests](https://github.com/gil9red/simple-wait/actions/workflows/run-tests.yml/badge.svg)](https://github.com/gil9red/simple-wait/actions/workflows/run-tests.yml)
[![upload to pypi](https://github.com/gil9red/simple-wait/actions/workflows/python-publish.yml/badge.svg)](https://github.com/gil9red/simple-wait/actions/workflows/python-publish.yml)
[![pypi](https://img.shields.io/pypi/v/simple-wait.svg)](https://pypi.org/project/simple-wait/)
![pypi python versions](https://img.shields.io/pypi/pyversions/simple-wait.svg)
[![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![License](https://img.shields.io/badge/license-MIT-black.svg)](https://opensource.org/licenses/MIT)

Example:
```python
from datetime import datetime
from simple_wait import wait

print("Start wait")
wait(seconds=5)
print("Finish wait")

while True:
    print()
    print("Current datetime:", datetime.now())
    print()
    wait(minutes=1, seconds=30)
```
