from typing import Any, Iterator, Mapping, Optional, Tuple 

from pymongo.client_session import ClientSession
from pymongo.collection import Collection

_DocumentOut = Any

class CommandCursor:
    def __init__(
        self,
        collection: Collection,
        cursor_info: Mapping[str, Any],
        address: Optional[Tuple[str, Optional[int]]],
        retrieved: int = ...,
        batch_size: int = ...,
        max_await_time_ms: Optional[int] = ...,
        session: Optional[ClientSession] = ...,
        explicit_session: bool = ...,
    ) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def batch_size(self, batch_size: int) -> CommandCursor: ...
    @property
    def alive(self) -> bool: ...
    @property
    def cursor_id(self) -> int: ...
    @property
    def address(self) -> Optional[Tuple[str, Optional[int]]]: ...
    @property
    def session(self) -> Optional[ClientSession]: ...
    def __iter__(self) -> Iterator[_DocumentOut]: ...
    def next(self) -> _DocumentOut: ...
    def __next__(self) -> _DocumentOut: ...
    def __enter__(self) -> CommandCursor: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

class RawBatchCommandCursor(CommandCursor):
    def next(self) -> bytes: ...
    def __next__(self) -> bytes: ...
