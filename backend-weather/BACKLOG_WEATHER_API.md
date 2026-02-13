# Backlog - Weather API (apprentissage guide)

## Objectif
Construire toi-meme un backend FastAPI propre pour exposer `GET /api/weather?city=...`.
Le but est d'apprendre la methode, pas de copier-coller une solution complete.

## Decisions fixees
- Ville invalide/introuvable: HTTP `404`.
- Libelles meteo: francais uniquement.
- Client HTTP externe: `httpx.AsyncClient`.
- Source meteo: Open-Meteo (geocoding + forecast).

## Definition of Done globale
- Endpoint `GET /api/weather?city=...` fonctionne en local.
- Contrat JSON stable en succes et en erreur.
- Gestion explicite des erreurs (validation, ville introuvable, upstream).
- Mapping minimal des weather codes en francais.
- Tests manuels reproductibles documentes.

---

## Epic E0 - Setup et cadre de travail
### User story
En tant que developpeur, je veux un environnement local propre pour iterer vite sans confusion.

### Taches
- [ ] Creer/activer le venv du backend (`backend-weather/.venv`).
- [ ] Installer `fastapi`, `uvicorn`, `httpx`.
- [ ] Verifier les versions installees.
- [ ] Ajouter une commande standard de lancement (`uvicorn app.main:app --reload`).

### Tests concrets
- [ ] `python -m pip show fastapi httpx uvicorn`.
- [ ] `GET /api/health` retourne `{"status":"ok"}`.

### Check comprehension
- [ ] Je sais expliquer pourquoi `async` + `httpx` est utile ici.

---

## Epic E1 - Service geocoding (ville -> coordonnees)
### User story
En tant qu'API, je veux convertir une ville en latitude/longitude avant d'interroger la meteo.

### Taches
- [ ] Creer `app/services/weather_client.py`.
- [ ] Definir `CityNotFoundError` et `UpstreamWeatherError`.
- [ ] Implementer `fetch_city_coordinates(city: str) -> dict`.
- [ ] Valider `city` (trim + non vide).
- [ ] Appeler Open-Meteo geocoding en async.
- [ ] Retourner un objet minimal: `city`, `country`, `latitude`, `longitude`.
- [ ] Lever `CityNotFoundError` si aucun resultat.

### Tests concrets
- [ ] `Paris` retourne bien des coordonnees.
- [ ] `VilleInexistanteXYZ` declenche `CityNotFoundError`.
- [ ] `"   "` declenche une erreur de validation (ValueError ou equivalent interne).

### Check comprehension
- [ ] Je sais expliquer la difference entre erreur metier (city not found) et erreur technique (upstream).

---

## Epic E2 - Service forecast (coordonnees -> meteo courante)
### User story
En tant qu'API, je veux recuperer temperature/vent/code meteo puis mapper un libelle FR.

### Taches
- [ ] Definir `WEATHER_URL`.
- [ ] Definir un mapping minimal `weather_code -> weather_label` en FR.
- [ ] Implementer `weather_label_from_code(code: int) -> str`.
- [ ] Implementer `fetch_current_weather(latitude, longitude) -> dict`.
- [ ] Verifier la presence des champs obligatoires dans `payload.current`.
- [ ] Lever `UpstreamWeatherError` si payload incomplet ou erreur HTTP/reseau.

### Tests concrets
- [ ] Appel avec coordonnees de Paris retourne `temperature_c`, `wind_kmh`, `weather_code`, `weather_label`.
- [ ] Simuler code inconnu et verifier label `"Inconnu"`.

### Check comprehension
- [ ] Je sais justifier pourquoi le mapping est volontairement minimal au debut.

---

## Epic E3 - Endpoint GET /api/weather
### User story
En tant qu'utilisateur front, je veux obtenir un JSON meteo simple depuis une ville.

### Taches
- [ ] Ajouter route `GET /api/weather` dans `app/main.py`.
- [ ] Parametre query `city` obligatoire.
- [ ] Orchestrer: geocoding puis forecast.
- [ ] Construire JSON de succes stable.
- [ ] Gerer les exceptions avec codes HTTP cibles.

### Regles HTTP (MVP)
- [ ] `200` succes.
- [ ] `404` ville introuvable.
- [ ] `422` parametre `city` vide/invalide.
- [ ] `502` erreur Open-Meteo (timeout/HTTP non-OK/payload invalide).

### Contrat JSON cible
#### Succes `200`
```json
{
  "ok": true,
  "city": "Paris",
  "country": "France",
  "latitude": 48.85341,
  "longitude": 2.3488,
  "temperature_c": 9.0,
  "wind_kmh": 11.2,
  "weather_code": 3,
  "weather_label": "Couvert",
  "source": "open-meteo"
}
```

#### Erreur ville `404`
```json
{
  "ok": false,
  "error": {
    "code": "city_not_found",
    "message": "Aucune ville trouvee pour 'VilleInexistanteXYZ'"
  }
}
```

### Tests concrets
- [ ] `GET /api/weather?city=Paris` -> 200.
- [ ] `GET /api/weather?city=VilleInexistanteXYZ` -> 404.
- [ ] `GET /api/weather?city=` -> 422.

### Check comprehension
- [ ] Je sais expliquer le role de chaque status code et pourquoi 404 est choisi pour ville introuvable.

---

## Epic E4 - Robustesse et lisibilite
### User story
En tant que mainteneur, je veux un code lisible et facile a faire evoluer.

### Taches
- [ ] Centraliser les constantes d'URL et timeouts.
- [ ] Ajouter des docstrings courtes sur les fonctions publiques.
- [ ] Eviter les commentaires longs redondants.
- [ ] Standardiser les noms de cles JSON.
- [ ] Ajouter un fichier `backend-weather/README.md` (run + endpoints + exemples).

### Tests concrets
- [ ] Relire le code a froid et verifier que chaque fonction a une responsabilite claire.
- [ ] Verifier qu'aucun message d'erreur ne fuit des details internes inutiles.

---

## Epic E5 - Integration front (widgets.html)
### User story
En tant qu'utilisateur du site, je veux saisir une ville et afficher la meteo via ton backend.

### Taches
- [ ] Creer un mini formulaire ville dans `widgets.html`.
- [ ] Ajouter un script `js/weather.js` (appel fetch backend + rendu).
- [ ] Gerer etats UI: chargement, succes, erreur.
- [ ] Afficher explicitement les erreurs 404 (ville non trouvee).

### Tests concrets
- [ ] Ville valide -> carte meteo affichee.
- [ ] Ville invalide -> message clair non bloquant.
- [ ] Backend down -> message "service indisponible".

---

## Epic E6 - Qualite et progression perso
### User story
En tant qu'apprenant, je veux prouver ma comprehension a chaque etape.

### Taches
- [ ] Tenir un journal court des choix techniques (1-3 lignes par decision).
- [ ] Noter ce qui t'a bloque et la solution retenue.
- [ ] A la fin de chaque epic, ecrire "ce que je saurais refaire sans aide".

### Gate de passage entre epics
- [ ] Je passe a l'epic suivant seulement si tous les tests concrets de l'epic courant sont valides.

---

## Sprint propose (ordre conseille)
1. E0 + E1
2. E2
3. E3
4. E4
5. E5
6. E6 (en continu)

## Next action immediate
- [ ] Implementer proprement l'endpoint `GET /api/weather` (Epic E3) en gardant la logique metier dans `weather_client.py`.
