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
async def fetch_city_coordinates(city: str) -> dict: # Cette fonction prend en entrée une chaîne de caractères représentant le nom d'une ville, et retourne un dictionnaire contenant les coordonnées géographiques de cette ville (latitude et longitude), ainsi que son nom et son pays. Si la ville n'est pas trouvée, elle lève une exception CityNotFoundError. Si une erreur survient lors de la communication avec l'API de géocodage, elle lève une exception UpstreamWeatherError.
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


# Le module weather_client.py est un client pour l'API de géocodage d'Open-Meteo, qui permet de convertir un nom de ville en coordonnées géographiques (latitude et longitude). Il utilise la bibliothèque httpx pour effectuer des requêtes HTTP asynchrones. Le module définit également deux exceptions personnalisées : CityNotFoundError pour indiquer qu'une ville n'a pas été trouvée, et UpstreamWeatherError pour signaler des erreurs lors de la communication avec l'API de géocodage.
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODE_LABELS_FR = {
    0: "Ensoleille",
    1: "Principalement degage",
    2: "Partiellement nuageux",
    3: "Couvert",
    45: "Brouillard",
    48: "Brouillard givrant",
    51: "Bruine legere",
    61: "Pluie legere",
    63: "Pluie moderee",
    65: "Pluie forte",
    80: "Averses de pluie",
    95: "Orage",
} # Ce dictionnaire associe des codes météorologiques à des étiquettes en français. Les codes sont des entiers qui représentent différents types de conditions météorologiques, tels que l'ensoleillement, la couverture nuageuse, le brouillard, la pluie, les averses et les orages. Les étiquettes correspondantes sont des descriptions textuelles de ces conditions météorologiques en français. Par exemple, le code 0 correspond à "Ensoleille", le code 1 à "Principalement degage", et ainsi de suite. Ce dictionnaire peut être utilisé pour traduire les codes météorologiques obtenus à partir d'une API de prévisions météorologiques en descriptions compréhensibles pour les utilisateurs francophones.


def weather_label_from_code(code: int) -> str:
    return WEATHER_CODE_LABELS_FR.get(code, "Inconnu")


async def fetch_current_weather(latitude: float, longitude: float) -> dict:
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            res = await client.get(
                WEATHER_URL,
                params={
                    "latitude": latitude,
                    "longitude": longitude,
                    "current": "temperature_2m,wind_speed_10m,weather_code",
                    "temperature_unit": "celsius",
                    "wind_speed_unit": "kmh",
                },
            )
            res.raise_for_status()
            payload = res.json()
    except httpx.RequestError as exc:
        raise UpstreamWeatherError("forecast request failed") from exc
    except httpx.HTTPStatusError as exc:
        raise UpstreamWeatherError(f"forecast http error: {exc.response.status_code}") from exc

    current = payload.get("current") or {}
    temp = current.get("temperature_2m")
    wind = current.get("wind_speed_10m")
    code = current.get("weather_code")

    if temp is None or wind is None or code is None:
        raise UpstreamWeatherError("forecast payload missing required fields")

    code = int(code)
    return {
        "temperature_c": float(temp),
        "wind_kmh": float(wind),
        "weather_code": code,
        "weather_label": weather_label_from_code(code),
    }
