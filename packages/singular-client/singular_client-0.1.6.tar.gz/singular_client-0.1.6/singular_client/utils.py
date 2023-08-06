from typing import (
    TypeVar,
    List,
    Union,
    Optional,
    overload,
)
import re


def format_variable(s: str) -> str:
    """
    " ThisText   (x) is a__str " -> "this_text_x_is_a__str"
    """
    # Find camelCase and underscore delimit it before we mess with case
    s = re.sub(r"([a-z])([A-Z])", r"\1_\2", s)
    s = s.strip().lower()
    s = re.sub(r"-", " ", s)
    s = re.sub(r" [^A-Za-z] ", " ", s)  # " - " -> " "
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^A-Za-z0-9_ ]+", "", s)
    s = s.replace(" ", "_")
    return s


def format_constant(s: str) -> str:
    """
    "xX" -> "X_X"
    """
    s = format_variable(s)
    s = re.sub(r"([^A-Z_])([A-Z])", r"\1_\2", s)
    return s.upper()


def format_type(s: str) -> str:
    """
    ONE_two_three -> OneTwoThree
    ONE_twoThree -> OneTwoThree
    oneTwo_three -> OneTwoThree
    """

    def to_title(match):
        return match.group(1).title()

    def to_upper(match):
        return match.group(1).upper()

    s = format_variable(s)
    # Leading lowercase to title
    s = re.sub(r"^([a-z])", to_upper, s)
    # Uppercase to title
    s = re.sub(r"([A-Z]+)", to_title, s)
    # Underscore title or lowercase to title without underscore
    s = re.sub(r"_([A-Za-z][a-z]+)", to_title, s)
    return s


T = TypeVar("T")


@overload
def _convert_list_arg(
    arg: Union[List[T], T, str], default: Optional[List[T]] = None
) -> str:
    ...


@overload
def _convert_list_arg(arg: None = None, default: List[T] = None) -> str:
    ...


@overload
def _convert_list_arg(arg: None = None, default: None = None) -> None:
    ...


def _convert_list_arg(arg=None, default=None):
    """
    Converts a list of arguments to a comma separated string.
    ---
    The overloading allows endpoints with generic dimension and metric types
    to pass those arguments to this function without type issues.
    """
    if isinstance(arg, list):
        return ",".join([str(x) for x in arg])
    if not arg and default:
        return ",".join([str(x) for x in default])
    if arg is not None:
        return str(arg)
    return arg
