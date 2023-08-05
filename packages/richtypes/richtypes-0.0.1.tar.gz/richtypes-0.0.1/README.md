# RICHTYPES

Enhanced python Datatype with rich extended methods.

## Types Supported

- [x] list
- [x] dict
- [ ] set
- [ ] tuple
- [ ] str

## Install

```bash
pip install richtypes
```

## Examples

### RichList

```python

from richtypes import RichList

rl = RichList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) # create a RichList

rl.append(12) # append a number
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

rl.length # length of the list
# 12


# function to check even
def is_even(num):
    return num % 2 == 0


rl.where(is_even) # filter list which follows is_even func
# [2, 4, 6, 8, 10]

# use inplace=False to return a new list
new = rl.where(is_even, inplace=False)
# [2, 4, 6, 8, 10]


rl.first_where(is_even) # first element which follows is_even func
# 2

```

### RichDict

```python

from richtypes import RichDict

rd = RichDict(a=1, b=2, c=3, d=4, e=5) # create a RichDict

rd.length # length of the dict
# 5


rd.first_item # first item of the dict
# {'a': 1}

rd.replace_key(old_key='a', new_key='r') # replace key
# {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'r': 1}

```
