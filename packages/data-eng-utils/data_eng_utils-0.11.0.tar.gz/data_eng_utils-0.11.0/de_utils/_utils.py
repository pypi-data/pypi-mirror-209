"""Generic collection of python utils."""
from functools import wraps
from typing import (
    Union,
    Any,
    List,
    Callable,
    get_type_hints,
)


def rm_pre_wrap():
    """Remove pre-wrapping from all iPython console outputs.

    Removes pre-wrapping from iPython console outputs e.g. in CDSW and jupyterlab.
    This could also be added to an .ipython config to make it the default behaviour.

    source: https://stackoverflow.com/questions/43427138
    """
    from IPython.core.display import HTML, display
    display(HTML("<style>pre { white-space: pre !important; }</style>"))


def to_list(obj: Any) -> List[Any]:
    """Return input as List[input] if it's not already, unless input is None."""
    return [obj] if not isinstance(obj, (list, type(None))) else obj


def enforce_type_hints(to_check: Union[str, List[str]]) -> Callable:
    """
    Raise exception when type of argument used is different to type hint.

    Parameters
    ----------
    to_check: str or List[str]
        Names of parameters to enforce type hinting on, otherwise "all" to check all.

    Note
    ----
    - This is not to enforce types from typing module i.e. List[..], Dict[..] or Optional.
       Doing the above will raise a "TypeError: Parameterized generics cannot be used with
       class or instance checks" error.
    - Use this decorator only when you know that python or the library using the
      parameter won't already handle the error if a param of the wrong type is passed.

    Returns
    -------
    callable
        A decorator that can be used to decorate functions and check their arguments before use.
    """
    def caller(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal to_check
            to_check = to_list(to_check)

            _args = dict(zip(func.__code__.co_varnames, args))
            all_args = {**_args, **kwargs}

            if 'all' in to_check:
                to_check = all_args

            dup_args = [a for a in _args if a in kwargs]
            if dup_args:
                raise TypeError(
                    f" args and kwargs conflict: {func.__name__}() got multiple"
                    " values for arguments '" + "', '".join(dup_args) + "'")

            hints = get_type_hints(func)

            failed = {
                arg: type(val) for arg, val in all_args.items()
                if arg in to_check and not isinstance(val, hints[arg])}

            if failed:
                msg = [f'-"{p}" should be type {hints[p]} but instead got {failed[p]}'
                       for p in failed]

                raise TypeError('Parameter of unexpected type:\n' + '\n '.join(msg))

            return func(*args, **kwargs)
        return wrapper
    return caller
