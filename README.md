# Basisproject API Development
## Thema

Voor mijn project heb ik gekozen voor Star Wars:

Star Wars is een franchise waar ik zelf gepassioneerd over ben.
Het universum, de personages, en de verhalen boeien me enorm.
Hierdoor is het werken aan een project binnen dit thema niet alleen een professionele uidaging, maar ook een kans om te werken met iets waar ik graag met bezig ben.
Binnen de Star Wars-wereld is er een breed scala van entiteiten zoals films, personages en starships maar ook enorm veel collector items of speelgoed.
Dit biedt me de kans om met iets gevarieerd te werken en waar ook zeer veel uitbreidingsmogelijkheden inzitten.

## Werking API

Als basis voor mijn API heb ik een Sqlite-databank gebruikt.
In de databank zitten 3 tabellen: 
1. Films
2. Persons
3. Starships
In de databank kunnen kan je per film de personages en de Starships toevoegen. Via de Api kan je zowel ze oproepen of verwijderen en je kan ook de volledige database in zijn geheel ophalen.

![image](https://github.com/VerbovenSteve/api_development/assets/113888137/11a26828-1db3-436a-aa37-368fae0a41c3)
### link naar API:

https://useritem-api-service-verbovensteve.cloud.okteto.net/docs 

In het volgende deel zal ik alle functies laten zien van de interface.
> we beginnen bij de post requests. Dit wil zeggen het opvullen van de verschillende tabellen
## post 

### post /films

Deze post zal zorgen dat we een film in de databank kunnen zetten
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/5c03458c-620a-4ed0-aeda-50cc14dc322a)

### post /persons

Deze post zorgt ervoor dat we een personage kunnen toevoegen aan een bepaald film id.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/fd733bfd-647c-4305-ba45-c99b5521e478)

### post /starships

Deze post zal starships toevoegen aan een film via de film id.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/1f3f1c6b-1361-4d55-8179-c9b5afe2daef)

