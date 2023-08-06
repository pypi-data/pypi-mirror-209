# startstop

A simple way to start and stop a Python profiler ([pyinstument](https://github.com/joerick/pyinstrument)) and view the results in the browser.

[![PyPI - Version](https://img.shields.io/pypi/v/startstop.svg)](https://pypi.org/project/startstop)

-----

## Installation

```console
pip install startstop
```

## Usage

```python
from startstop import t, tc, p, pc
```

### Simple timer

```python
t()
# This is where your code goes.
t()
```

TIMER: 0.024 sec

```python
t(label="your label", precision=2)
# This is where your code goes.
t()
```

TIMER your label: 0.02 sec

### Simple timer as contex manager

```python
with tc():
    # This is where your code goes.
```

TIMER: 0.024 sec

```python
with tc(label="your label", precision=2):
    # This is where your code goes.
```

TIMER your label: 0.02 sec

### Profiler

```python
p()
# This is where your code goes.
p()
```

--> Browser output

```python
p(interval=0.01, async_mode="disabled")
# This is where your code goes.
p()
```

--> Browser output

### Profiler as context manager

```python
with pc():
    # This is where your code goes.
```

--> Browser output

```python
with pc(interval=0.002, async_mode="strict"):
    # This is where your code goes.
```

--> Browser output
