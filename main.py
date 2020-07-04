#!/usr/bin/env python3
from fastapi import FastAPI

app = FastAPI()


@app.get('/MP_verify_{identifier}.txt')
@app.get('/{pre_path:path}/MP_verify_{identifier}.txt')
async def response_identifier(identifier: str, pre_path: str=''):
    return identifier


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', port=10240, log_level='info')
