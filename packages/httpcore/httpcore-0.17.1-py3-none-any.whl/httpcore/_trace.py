import logging
from types import TracebackType
from typing import Any, Dict, Optional, Type

from ._models import Request

logger = logging.getLogger("httpcore")


class Trace:
    def __init__(
        self,
        name: str,
        request: Optional[Request] = None,
        kwargs: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.name = name
        self.trace_extension = (
            None if request is None else request.extensions.get("trace")
        )
        self.debug = logger.isEnabledFor(logging.DEBUG)
        self.kwargs = kwargs or {}
        self.return_value: Any = None
        self.should_trace = self.debug or self.trace_extension is not None

    def trace(self, name: str, info: Dict[str, Any]) -> None:
        if self.trace_extension is not None:
            self.trace_extension(name, info)

        if self.debug:
            if not info or "return_value" in info and info["return_value"] is None:
                message = name
            else:
                args = " ".join([f"{key}={value!r}" for key, value in info.items()])
                message = f"{name} {args}"
            logger.debug(message)

    def __enter__(self) -> "Trace":
        if self.should_trace:
            info = self.kwargs
            self.trace(f"{self.name}.started", info)
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        if self.should_trace:
            if exc_value is None:
                info = {"return_value": self.return_value}
                self.trace(f"{self.name}.complete", info)
            else:
                info = {"exception": exc_value}
                self.trace(f"{self.name}.failed", info)

    async def atrace(self, name: str, info: Dict[str, Any]) -> None:
        if self.trace_extension is not None:
            await self.trace_extension(name, info)

        if self.debug:
            if not info or "return_value" in info and info["return_value"] is None:
                message = name
            else:
                args = " ".join([f"{key}={value!r}" for key, value in info.items()])
                message = f"{name} {args}"
            logger.debug(message)

    async def __aenter__(self) -> "Trace":
        if self.should_trace:
            info = self.kwargs
            await self.atrace(f"{self.name}.started", info)
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        if self.should_trace:
            if exc_value is None:
                info = {"return_value": self.return_value}
                await self.atrace(f"{self.name}.complete", info)
            else:
                info = {"exception": exc_value}
                await self.atrace(f"{self.name}.failed", info)
