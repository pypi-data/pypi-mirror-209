# test-data-generation-framework

## About

This framework enables users to generate test data either imperatively or directly from a `de-utils/SchemaManager` schema via CLI or `TableGenerator.from_schema()`.

## Examples

### Setup by explicitly specifying table schema and generation parameters.

```python
from de_utils.test_data_generation import TableGenerator
from de_utils.test_data_generation.columns import *

gen = TableGenerator()

gen.columns = [
    StringColumn('id', size=10, distinct=True),
    StringColumn('postcode', size=8, generation_method="postcode"),
    DecimalColumn('age', precision=3, scale=0),
    DateColumn('date_of_birth'),
]

gen.generate("data.csv", desired_size=100)
```


### Load directly from a JSON schema file.

#### Using the module:

```python
from de_utils.test_data_generation import TableGenerator

gen = TableGenerator.from_schema(schema_path="schema.json")

gen.generate("data.csv", desired_size=100)
```

#### Using the CLI:

```shell
python table_generator.py -f schema.json -o data.csv -n 100
```

### Combine with [Faker](https://github.com/joke2k/faker) for rich data creation:

```python
from de_utils.test_data_generation import TableGenerator
from de_utils.test_data_generation.columns import *
from faker import Faker


faker = Faker('en-GB')

gen = TableGenerator()

gen.columns = [
    StringColumn('name', size=10, distinct=True, generation_method=faker.name),
    StringColumn('postcode', size=8, generation_method=faker.postcode),
]

gen.generate("data.csv", desired_size=100)
```

## Implemented Columns

### DecimalColumn

```python
class DecimalColumn(
    col_name: str,
    precision: int = 10,
    scale: int = 0,
    **kwargs
)
```
`DecimalColumn` provides support for control over the `precision` and `scale` of numeric values that are outputted.

- `col_name`: the name of the column, used in output headers if appropriate
- `precision`: the total number of digits in the outputted number (both before and after dp)
  - where `1 <= precision <= 38`
- `scale`: the number of digits after the decimal place
  - where `(-precision + 1) <= scale <= precision`

```python
# Example where age can only produce values between 0 and 99 (inclusive)
DecimalColumn(col_name="age", precision=2, scale=0)
```

### StringColumn

```python
class StringColumn(
    col_name: str,
    size: int = 50,
    size_mode: int = StringColumn.SIZE_TRUNCATE,
    generation_method: Optional[Union[str, Callable]] = None,
    **kwargs
)
```
`StringColumn` encompasses arbitrary text generation, existing generation functions (see below) and the ability to pass your own custom functions.

- `col_name`: the name of the column, used in output headers if appropriate
- `size`: the maximum size of the column
  - where no `generation_method` is passed, the column produces arbitrary random text with length of `size`
- `size_mode`: how to handle generated values that exceed `size`, one of the following:
  - `StringColumn.SIZE_TRUNCATE`: trim any values that exceed `size`(*default*)
  - `StringColumn.SIZE_IGNORE`: allow values longer than `size` to be generated (*overflow*)
  - `StringColumn.SIZE_ERROR`: throw an error when values longer than `size` are created
- `generation_method`: either a `str` identifier to one of the listed methods, or a reference to a function
  - a passed function should not require any arguments to be passed (use a `lambda` or `functools.partial` where needed)

Currently implemented include:

| Name | `generation_method` |
| - | - |
| country code | `country_code` |
| 'y' or 'n' flag | `y_or_n` |
| tax code | `tax_code` |
| postcode | `postcode` |
| gender code | `gender_code` |
| email | `email` |
| mobile number | `mobile_number` |
| bank account number | `bank_account_number` |
| bank sort code | `bank_sort_code` |

These methods (`de_utils/test_data_generation/common.py`) can be contributed to with functions for common column types we typically find in datasets.

```python
# Example using an existing generation method
StringColumn(col_name="postcode", size=8, generation_method="postcode")
```

[Faker](https://github.com/joke2k/faker) can be hooked up to `StringColumn` to enable richer values in the outputted data.

```python
# Example
faker = Faker("en-GB")

StringColumn(col_name="postcode", size=8, generation_method=faker.postcode)
```

### DateColumn and TimestampColumn

Generates a random date or timestamp between `min_year` and `max_year` (inclusive).

```python
class DateColumn(
    col_name: str,
    format: str = '%Y-%m-%d',
    min_year: int = 2010,
    max_year: int = 2022,
    **kwargs
)

class TimestampColumn(
    col_name: str,
    format: str = '%Y-%m-%dT%H:%M:%SZ',
    min_year: int = 2010,
    max_year: int = 2022,
    **kwargs
)
```

- `col_name`: the name of the column, used in output headers if appropriate
- `format`: the format for generated date/timestamps to be converted to (`strftime`)
- `min_year`: lower year bound for the generated date
- `max_year`: upper year bound for the generated date


```python
# Example
DateColumn(
    "date_of_birth",
    format="%d-%m-%Y",
    min_year=2015
)
```
