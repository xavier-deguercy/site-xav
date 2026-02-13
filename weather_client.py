from __future__ import annotations

import httpx

# ce module est un client pour l'API de géocodage d'Open-Meteo, qui permet de convertir un nom de ville en coordonnées géographiques (latitude et longitude). Il utilise la bibliothèque httpx pour effectuer des requêtes HTTP asynchrones. Le module définit également deux exceptions personnalisées : CityNotFoundError pour indiquer qu'une ville n'a pas été trouvée, et UpstreamWeatherError pour signaler des erreurs lors de la communication avec l'API de géocodage.
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"

# Le module weather_client.py est un client pour l'API de géocodage d'Open-Meteo, qui permet de convertir un nom de ville en coordonnées géographiques (latitude et longitude). Il utilise la bibliothèque httpx pour effectuer des requêtes HTTP asynchrones. Le module définit également deux exceptions personnalisées : CityNotFoundError pour indiquer qu'une ville n'a pas été trouvée, et UpstreamWeatherError pour signaler des erreurs lors de la communication avec l'API de géocodage.
class CityNotFoundError(Exception):
    pass

# Le module weather_client.py est un client pour l'API de géocodage d'Open-Meteo, qui permet de convertir un nom de ville en coordonnées géographiques (latitude et longitude). Il utilise la bibliothèque httpx pour effectuer des requêtes HTTP asynchrones. Le module définit également deux exceptions personnalisées : CityNotFoundError pour indiquer qu'une ville n'a pas été trouvée, et UpstreamWeatherError pour signaler des erreurs lors de la communication avec l'API de géocodage.
class UpstreamWeatherError(Exception):
    pass

# 
async def fetch_city_coordinates(city: str) -> dict:
    city = city.strip()
    if not city:
        raise ValueError("city must not be empty")

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            res = await client.get(
                GEOCODING_URL,
                params={"name": city, "count": 1, "language": "fr"},
            )
            res.raise_for_status()
            payload = res.json()
    except httpx.RequestError as exc:
        raise UpstreamWeatherError("geocoding request failed") from exc
    except httpx.HTTPStatusError as exc:
        raise UpstreamWeatherError(f"geocoding http error: {exc.response.status_code}") from exc

    results = payload.get("results") or []
    if not results:
        raise CityNotFoundError(city)

    item = results[0]
    return {
        "city": item["name"],
        "country": item.get("country"),
        "latitude": item["latitude"],
        "longitude": item["longitude"],
    }
