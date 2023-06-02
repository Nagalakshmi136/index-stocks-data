from typing import Optional
from fastapi import FastAPI
from helper.indices import get_index_stocks_data

app = FastAPI()

@app.get('/')
def home():
    return "This is start page"

@app.get('/index/{index_name}')
def index_stocks(index_name: str,specific_stock: Optional[str] = None):
    return get_index_stocks_data(index_name, specific_stock)
