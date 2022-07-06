# Contribution

The code follows [PEP 0008](https://peps.python.org/pep-0008/), [PEP 0257](https://peps.python.org/pep-0257/), and replaced some PEPS with the newly implemented PEP, such as [PEP 0308](https://peps.python.org/pep-0308/) in some context being replaced with [PEP 0636](https://peps.python.org/pep-0636/), and strictly complies with [PEP 0484](https://peps.python.org/pep-0484/) with some revisions based on the preferences of the main author.

# Revisions

1. Long variable declaration, functions, and context managers broken into multiple lines should have an indent:

```python
# long variable declaration
variable_sample: tuple[list[int], str] = (
        """ whatever variable here"""
    )

# long variables with long type hint should be done as if type alias is not an option
variable_sample: dict[
        list[str | list[str]], tuple[list[int]]
    ] = {
        ["entry one"]: ([1, 2, 3], [1, 3, 5], ...),
        ...
    }

# functions
def hello_world_but_with_long_parameters(
        params_one: int,
        params_two: float,
        ...
    ) -> WhatEverType:
    ...

# context manager
with open(
        "file", "mode", encoding="encoding"
    ) as file:
    ...
```

2. (Functions) Calls broken into multiple lines should not have an indent:

```python
hello_world_but_with_long_parameters(
    params_one, params_two, ...
)

hello_world_but_with_long_value_of_parameters(
    "parameter one is very long",
    "so does parameter two, which is long",
    "parameter three is significantly longer",
    ...
)
```

3. Variable declarations should be separated depending on class which are (1.) Initiation; (2.) Constants; and (3.) Blanks

```python
# initiations
Variable: object = ClassInitiation()
ClassInit: object = ClassInitt()
console: object = rich.console.Console()
log: object = src.custom.logger.Logger()

# constants
BASE_DIR: str = f"{'/'.join(dirname(__file__).split('/')[:-3])}/HelloWorld"
BASE_PATH: str = f"{BASE_DIR}/sub_helloworld/..."

# blanks, anything that would change later on
index_when_else: int = 0
img_paths: list[str] = []
dicts: dict[str, str] = {}
```
