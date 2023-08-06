from typing import Type, TypeVar, Any, cast

RESTResult = TypeVar("RESTResult")


def execute(return_type: Type[RESTResult], p: Any) -> RESTResult:
    return cast(RESTResult, p)


def run(return_type: Type[RESTResult], p: Any) -> RESTResult:
    return execute(return_type=return_type, p=p)


print(run(Type[str], "ok"))
