from uvicorn import run
from fastapi import FastAPI
from models import User
from fastapi.middleware.cors import CORSMiddleware

from config import Config

app = FastAPI()
app.add_middleware(
	CORSMiddleware
)

App = Config('App')


@app.get('/')
async def home():
	return {'msg': 'Hello world! Home!!!'}

@app.get('/users/{user_id}')
async def users(user_id: int):
	return {'msg': f'Users {user_id}'}

if __name__ == "__main__":
    run(
    	f"main:{App['app_name']}",
    	host=App['host'],
    	port=App['port'],
    	reload=App['reload'],
    	log_level=App['log_level'])