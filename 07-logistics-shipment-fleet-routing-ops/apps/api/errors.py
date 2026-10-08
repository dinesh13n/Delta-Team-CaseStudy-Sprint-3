"""Problem-details errors (spec: error-handling-spec). Never return HTTP 200 for an error."""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from apps.api import correlation

MEDIA = "application/problem+json"


class ApiError(Exception):
    def __init__(
        self,
        status: int,
        title: str,
        detail: str = "",
        policy_decision_id: str | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(title)
        self.status, self.title, self.detail = status, title, detail
        self.policy_decision_id, self.headers = policy_decision_id, headers or {}


def problem(
    status: int, title: str, detail: str = "", policy_decision_id: str | None = None, headers: dict[str, str] | None = None
) -> JSONResponse:
    body: dict[str, Any] = {
        "type": "about:blank",
        "title": title,
        "status": status,
        "detail": detail,
        "correlation_id": correlation.current(),
    }
    if policy_decision_id:
        body["policy_decision_id"] = policy_decision_id
    h = dict(headers or {})
    h[correlation.HEADER] = correlation.current()
    return JSONResponse(body, status_code=status, media_type=MEDIA, headers=h)


def install(app: FastAPI) -> None:
    @app.exception_handler(ApiError)
    async def _api(_: Request, exc: ApiError) -> JSONResponse:
        return problem(exc.status, exc.title, exc.detail, exc.policy_decision_id, exc.headers)

    @app.exception_handler(RequestValidationError)
    async def _val(_: Request, exc: RequestValidationError) -> JSONResponse:
        return problem(422, "Validation error", "request parameters are invalid")

    @app.exception_handler(Exception)
    async def _any(_: Request, exc: Exception) -> JSONResponse:
        return problem(500, "Internal error", "unexpected error")
