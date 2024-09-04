#!/usr/bin/env python3
import sys

import fastapi_cdn_host
import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, RedirectResponse

app = FastAPI()
fastapi_cdn_host.patch_docs(app)


@app.get("/MP_verify_{identifier}.txt")
@app.get("/{pre_path:path}/MP_verify_{identifier}.txt")
async def response_identifier(identifier: str, pre_path: str = "") -> PlainTextResponse:
    """Response `identifier` as plain text"""
    return PlainTextResponse(identifier)


@app.get("/")
async def to_docs() -> RedirectResponse:
    return RedirectResponse(app.docs_url or "/docs")


def main() -> None:
    host, port = "127.0.0.1", 10240
    if sys.argv[1:]:
        if (a1 := sys.argv[1]).isdigit():
            port = int(a1)
        elif a1 == "0.0.0.0":
            host = a1
    uvicorn.run(app, port=port, host=host, log_level="info")


if __name__ == "__main__":
    main()
