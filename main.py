from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from fastapi import Query
from typing import Optional, List, Dict

from uvicorn import run

# Import using Routes
# from routes import userRouter
from config import Config

app = FastAPI()
app.add_middleware(
    CORSMiddleware
)

App = Config('App')


@app.get('/')
async def home():
    return {'msg': 'Hello world! Home!!!'}


@app.get('/users')
async def get_user_by_params(names: Optional[List[str]] = Query(None)):
    if names:
        print(names)
        return {'msg': f'User names: {names}'}
    return {'msg': 'All Users'}


@app.get('/users/{user_id}')
async def get_user_by_id(user_id: int):
    return {'msg': f'Users {user_id}'}


if __name__ == "__main__":
    run(
        f"main:{App['app_name']}",
        host=App['host'],
        port=App['port'],
        reload=App['reload'],
        log_level=App['log_level'])
