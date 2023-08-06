# simple-wait
Simple wait

[![Run tests](https://github.com/gil9red/simple-wait/actions/workflows/run-tests.yml/badge.svg)](https://github.com/gil9red/simple-wait/actions/workflows/run-tests.yml)
[![Upload Python Package](https://github.com/gil9red/simple-wait/actions/workflows/python-publish.yml/badge.svg)](https://github.com/gil9red/simple-wait/actions/workflows/python-publish.yml)

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
