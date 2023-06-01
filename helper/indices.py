from helper.constants import BASE_URL
from helper.fetch_data import get_api_data

def get_index_stocks_data(index_name: str):
    url = BASE_URL + index_name
    response = get_api_data(url)
    return response
    