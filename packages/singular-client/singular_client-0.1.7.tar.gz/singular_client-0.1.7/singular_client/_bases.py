"""
BASE CLASSES
============
Defines the inherited behavior of all endpoints, and response lists.
"""
from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    TypeVar,
    Union,
    Literal,
    Hashable,
    Tuple,
    List,
    Generic,
    TypedDict,
    Dict,
    Any,
    TypedDict,
    Type,
    get_args,
    get_type_hints,
)
from inspect import signature

if TYPE_CHECKING:
    from singular_client.api import SingularAPI


D = TypeVar("D", bound=Union[TypedDict, dict])


class ResponseDocList(Generic[D], List[D]):
    pass


KwargsKey = Tuple[Hashable, Hashable]
CacheKey = KwargsKey
ResType = TypeVar("ResType")


class _Endpoint(Generic[ResType]):
    """
    Base class for all endpoints
    ----
    Stores a reference to the `SingularAPI` instance that created it.
    The API's `request` method is used to make requests to the Singular API,
    handling the basics like authentication and base URL.

    Caches responses if `cls.cacheable` is True.
        Caching works by creating a unique dict key using the keyword arguments given
        to the request method. The key is a tuple of tuples, where each inner tuple
        is a key-value pair from the keyword arguments. The key is then used to
        retrieve the cached response if it exists, and overwrite the cache if it
        doesn't.
    """

    # Class variables
    endpoint: str
    data_path: list
    res_type: Type[ResType]
    cacheable = True
    returns_collection = True
    # Instance variables
    cache: Dict[CacheKey, Any]
    api: "SingularAPI"
    method: Literal["GET", "POST", "PUT", "DELETE"] = "GET"

    def __init__(self, api: "SingularAPI"):
        self.api = api
        self.cache = dict()

    def request_raw(self, data=None, **kwargs):
        if not self.cacheable:
            return self.api.request(
                endpoint=self.endpoint, method=self.method, params=kwargs, data=data
            )

        kwargs_key = tuple((k, v) for k, v in kwargs.items())
        if data:
            # `data` might contain dicts or lists. Ignore them.
            kwargs_key += tuple(
                (k, v) for k, v in data.items() if not isinstance(v, (list, dict))
            )

        cache_found = self.cache.get(kwargs_key)
        if cache_found:
            print(
                "Using cached response from", f"{self.method.upper()} '{self.endpoint}'"
            )
            return cache_found

        print("New request:", f"{self.method.upper()} '{self.endpoint}'")

        res = self.api.request(
            endpoint=self.endpoint, method=self.method, params=kwargs, data=data
        )
        self.cache[kwargs_key] = res
        return res

    def request(self, **kwargs) -> ResType:
        """
        Orchestrate getting the response data, extracting from the data path,
        casting to response type.
        """
        data = self.request_raw(**kwargs)
        for key in self.data_path:
            data = data[key]

        assert hasattr(
            self, "res_type"
        ), f"'{type(self).__name__}' must define `res_type`"
        return self.res_type(data)

    @property
    def response_schema(self) -> ResponseSchema:
        """
        Return a dict of the response schema.
        Keys: field names
        Values: field types
        """
        assert hasattr(
            self, "res_type"
        ), f"'{type(self).__name__}' must define `res_type`"
        try:
            if not self.returns_collection:
                return ResponseSchema(self.get_annotations(self.res_type))
            args = get_args(self.res_type)
            if args:
                annotated = [arg for arg in args if self.get_annotations(arg)]
                if annotated:
                    return ResponseSchema(self.get_annotations(annotated[0]))
        except Exception:
            pass
        return ResponseSchema({})

    @property
    def parameters(self) -> RequestParams:
        """
        Return a dict of the request schema.
        Keys: field names
        Values: field types
        """
        assert hasattr(
            self, "res_type"
        ), f"'{type(self).__name__}' must define `res_type`"
        return RequestParams(
            [str(param) for _, param in signature(self.request).parameters.items()]
        )

    @staticmethod
    def get_annotations(x) -> dict:
        """
        Safely get annotations from a class
        """
        try:
            return get_type_hints(x)
        except Exception:
            try:
                return x.__annotations__
            except Exception:
                return {}


class RequestParams(List[str]):
    def __repr__(self):
        return "\n".join(self)


class ResponseSchema(Dict[str, type]):
    def __repr__(self):
        return "\n".join([f"{k}: {getattr(v, '__name__', v)}" for k, v in self.items()])
