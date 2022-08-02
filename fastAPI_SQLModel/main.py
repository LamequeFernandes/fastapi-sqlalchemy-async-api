from fastapi import FastAPI

from api.routers.router import api_router

app = FastAPI()

app.include_router(api_router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8001, reload=True)