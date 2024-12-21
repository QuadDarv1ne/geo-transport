# app/api/endpoints.py
from fastapi import APIRouter, HTTPException
from app.core.config import settings
import httpx

router = APIRouter()

@router.get("/geocode")
async def geocode(address: str):
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={settings.yandex_api_key}&geocode={address}&format=json"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    if "response" in data:
        geo_object = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        coordinates = geo_object["Point"]["pos"]
        return {"coordinates": coordinates}
    else:
        raise HTTPException(status_code=404, detail="Address not found")

@router.get("/reverse_geocode")
async def reverse_geocode(lat: float, lon: float):
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={settings.yandex_api_key}&geocode={lat},{lon}&format=json"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    if "response" in data:
        geo_object = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        address = geo_object["metaDataProperty"]["GeocoderMetaData"]["text"]
        return {"address": address}
    else:
        raise HTTPException(status_code=404, detail="Coordinates not found")