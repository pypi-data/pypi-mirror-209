# htutil

HaoTian's Python Util

![version](https://img.shields.io/pypi/v/htutil)
![downloads](https://img.shields.io/pypi/dm/htutil)
![format](https://img.shields.io/pypi/format/htutil)
![implementation](https://img.shields.io/pypi/implementation/htutil)
![pyversions](https://img.shields.io/pypi/pyversions/htutil)
![license](https://img.shields.io/pypi/l/htutil)

## Install

```sh
pip install htutil
```

## Usage

### file

```python
from htutil import file
```

Refer to C# System.IO.File API, very simple to use.

```python
    s = 'hello'
    write_text('1.txt', s)
    # hello in 1.txt
    append_text('1.txt', 'world')
    # helloworld in 1.txt
    s = read_text('1.txt')
    print(s)  # helloworld

    s = ['hello', 'world']
    write_lines('1.txt', s)
    # hello\nworld in 1.txt
    append_lines('1.txt',['\npython'])
    # hello\nworld\npython in 1.txt
    s = read_lines('1.txt')
    print(s)  # ['hello', 'world', 'python']
```

### cache

cache def result by pickle file.

```python
from htutil import cache
@cache.file_cache
def get_1():
    time.sleep(3)
    return 1
```

### counter

a simple counter based on dict.

```python
    c = Counter()
    c.add('1')
    c.add('1')
    c.add('2')

    print(c.to_dict()) # {'1': 2, '2': 1}

    c.dump() # same as print(c.to_dict())
```
