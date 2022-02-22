from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/amenities/")
async def amenities(lat: float, lon: float, radius: int):
    endpoint = f"https://overpass-api.de/api/interpreter?data=[out:json];(node[%22amenity%22](around:{radius}, {lat}, {lon});way[%22amenity%22](around:{radius},{lat}, {lon});relation[%22amenity%22](around:{radius}, {lat}, {lon}););out;%3E;"
    
    result = requests.get(endpoint).json()
    return result
