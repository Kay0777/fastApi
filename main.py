from uvicorn import run
from fastapi import FastAPI
from models import User
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
	CORSMiddleware
)


@app.get('/')
async def home():
	return {'msg': 'Hello world! Home!!!'}

@app.get('/users/{user_id}')
async def users(user_id: int):
	return {'msg': f'Users {user_id}'}

if __name__ == "__main__":
    run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="info")