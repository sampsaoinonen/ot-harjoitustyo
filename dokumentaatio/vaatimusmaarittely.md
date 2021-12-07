# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on Pythonilla ja Pygamella toteutettu Nokia-puhelimista tuttu matopeli. Pelissä käärmettä kasvatetaan syömällä omenoita samalla väistäen seiniä sekä käärmeen kasvavaa häntää. Peli loppuu kun käärme törmää seinään tai itseensä. 

## Käyttäjät

Peli on yksinpeli ja käyttäjällä on roolina vain pelaaja. Käyttäjä kirjautuu ulos kun sovellus suljetaan.

## Suunnitellut toiminnallisuudet

### Alkunäkymä

- Rekisteröity käyttäjä syöttää pelaajatunnuksen sekä salasanan päästäkseen itse peliin
- Rekisteröimätön käyttäjä pääsee rekistöröimään rekisteröinti-näkymä
- Aloitusnäkymältä pääsee HiScore-näkymään

### Rekisteröintinäkymä

- Pelaaja rekisteröi tunnuksen ja salasanan
- Jos pelaaja yrittää rekisteröidä jo käytössä olevan tunnuksen, hän saa siitä ilmoituksen ja kehoituksen valita toinen tunnus
- Vapaana olevan tunnuksen sekä salasanan syötettyään käyttäjä pääsee suoraan peliin

### Pelinäkymä

- Pelaaja ohjaa käärmettä nuolinäppäimillä keräten omenoita ja väistellen seiniä sekä käärmeen häntää. .. TEHTY
- Ruudun yläreunoissa näkyy kerätyt pisteet sekä käyttäjän nimi .. TEHTY lukuunottamatta käyttäjänäkymää
- Osuma seinään tai käärmeen häntään lopettaa pelin ja siirtyy Game Over-näkymään. .. TEHTY lukuunottamatta Game Over-näkymää

### Game Over-näkymä

- Pelaajalle ilmoitetaan pelin päättyneen
- Pelaajalle ilmoitetaan pisteet
- Pelaajalle ilmoitetaan jos pisteet riittävät HiScore-listaukseen
- Pelaajalle näytetään HiScore-näkymä, jonka jälkeen peli menee alkunäkymään

### HiScore-näkymä 

- Näkymässä näytetään 10 parasta nimimerkkiä pisteineen
- Näkymästä pääsee painamalla mitä tahansa näppäintä alkunäkymään

![Käyttöliittymäluonnos](https://github.com/sampsaoinonen/ot-harjoitustyo/blob/master/dokumentaatio/kayttoliittymaluonnos.png)

## Jatkokehitysideat

- Kaksinpeli paikallisesti samalla tietokoneella
- Vaikeusasteen muuttaminen(nopeus, pituuden lisäys omenasta)
- Peli tietokonetta vastaan, jossa molemmilla oma käärme, mutta yhteiset kerättävät omenat
