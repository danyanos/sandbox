from typing import Any, Callable, Dict, List, Protocol, TypeVar


class DataClassBound(Protocol):
    def is_dataclass(obj) -> bool:
        pass

T = TypeVar('T', bound=DataClassBound)


class DataContainer():

    def __init__(self,
                 data: List[Dict[str, Any]]):
        self.data = data

    def get_data(self):
        return self.data

    def as_dataclass(self,
                     class_obj: Callable[..., T]) -> List[T]:
        new_data = []
        for item in self.data:
            new_data.append(class_obj(**item))

        return new_data
