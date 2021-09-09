# Static
The simple and efficient way of creating statically typed function parameters.


## Example Usage

### Decorators

#### Forcing the parameters to be of a certain type
```py
from static.decorators import static
from math import sqrt

@static
def pythagoras(a: int, b: int, *, are_squared: bool = False) -> int:
    if not are_squared:
        a, b = a ** 2, b ** 2
    return sqrt(a + b)
```

#### Using regex to match the typing
```py
import re
from static.decorators import static

my_expr = re.compile('[0-9]+')

@static(regex=True, as_match=True)
def pythagoras(a: int, b: int, *, are_squared: bool = False) -> int:
    if not are_squared:
        a, b = a ** 2, b ** 2
    return sqrt(a + b)
```

### Enforcing return types
To enforce the return type of your function use the `@enforce_return` decorator.\
If your function doesn't return the type you specified when you call the function, it will raise an error.
```py
from static.decorators import enforce_return, static

@enforce_return
@static
def join(*args: str) -> str:
    return ''.join(args)
```
