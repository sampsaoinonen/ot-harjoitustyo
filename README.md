
## JakeTheSnake - matopeli

JakeTheSnake on Pygame-kirjastolla toteutettu versio klassisesta matopelistä.


### Käyttöohjeet

Ohjelman asennus tapahtuu komennolla:

```bash
poetry install
```

Ohjelman suorittaminen tapahtuu komennolla:

```bash
poetry run invoke start
```

Ohjelman testien suorittaminen tapahtuu komennolla:

```bash
poetry run invoke test
```

Ohjelman testien tallentaminen htlm-muotoon tapahtuu komennolla:

```bash
poetry run invoke coverage-report
```

Ohjelman koodin voi tarkistaa Pylint:llä  komennolla:

```bash
poetry run invoke pylint
```
### Pelaaminen

Tässä vaiheessa soveluksessa on kolme näkymää: 

* Alkuruutu, jossa kirjoitat nimesi ja pääset pelaamaan painamalla enter tai klikkaamalla hiirellä kuvaketta
* Pelitila, joka lähtee käyntiin nuolinäppäintä painamalla. Pelissä keräät omenoita väistäen samalla seiniä sekä omaa häntää
* Loppuruutu, johon päädyt törmättyäsi seinään tai itseesi. Samalla näet lopulliset pisteesi

### Linkit


* [Vaatimusmäärittely](https://github.com/sampsaoinonen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [Tuntikirjanpito](https://github.com/sampsaoinonen/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
* [Arkkitehtuuri](https://github.com/sampsaoinonen/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
* [GitHub-release(week5)](https://github.com/sampsaoinonen/ot-harjoitustyo/archive/refs/tags/viikko5.zip)
* [GitHub-release(week6)](https://github.com/sampsaoinonen/ot-harjoitustyo/archive/refs/tags/viikko6.zip)
