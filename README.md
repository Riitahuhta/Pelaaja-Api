Ohjelma on FastApi:lla toteutettu REST-rajapinta, jolla pystyy luomaan ja hallitsemaan pelaajia ja eventtejä
Pelaajat tallennetaan SQLite-tietokantaan ja eventit muistiin


**Ohjelman käynnistys**

  - Vaadittujen kirjastojen asennus
      pip install -r requirements.txt

  - Sovelluksen käynnistys
      uvicorn main:app --reload

  - Swagger-dokumentaatio löytyy osoitteista
      http://127.0.0.1:8000/docs
      http://localhost:8000/docs


Tekoälyä käytin error koodien selventämiseen, kysymällä miksi asiaa ei voi tehdä tietyllä tavalla, vaikeiden selitysten selventämiseen sekä parin ongelma tilanteen ratkaisemiseen.

**Huomioitavaa**
DB ja Routers kansioden nimet on vaihdettu mutta se ei jostain syystä githubissa näy joten jos tulee ongelmia vaihda ne:
DB -> db
Routers -> routers
