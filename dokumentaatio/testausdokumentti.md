# TESTAUSDOKUMENTTI

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

`Snake`-luokkaa testataan `TestSnake`-testiluokalla. `Snake`-olio alustetaan ja testataan olemassaolo sekä, että se saa koordinaateikseen luokassa määritetyt arvot.
 
`SnakeTail`- luokka testataan `TestSnakeTail`-testiluokalla. `SnakeTail`-olio alustetaan ja testataan olemassaolo sekä, että se saa koordinaateikseen luokassa määritetyt arvot (100, 100).

`GameLoop`-luokka testataan `TestGameLoop`-testiluokalla. Tässä testaus on toteutettu tarvittavien riippuvuuksien injektoinnilla, joissa riippuvuuksille on toteutettu abstraktiot. Lopulta testataan, että `Level`-luokan metodi Crashed palauttaa True madon osuessa seinään.

### Repositorio -luokka

`UserRepository`-luokka testataan `TestUserRepository`-testiluokalla. Kyseisessä testiluokassa testataan, että `UserRepository`-luokan metodi get_topfive palauttaa kovakoodatun kärkiviisikon tiedot tietokannasta. Lisäksi testataan metodia check_score, palauttaa käyttäjänimellä ja pisteellä Booleanin siitä mahtuuko arvot kärkiviisikkoon.

### Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu käyttöohjeen kuvaamalla tavalla sekä macOS- että Linux-ympäristöön. Testauksessa on käytetty myös eri konfiguraatioita .env-tiedoston kautta.

![Testaus](https://github.com/sampsaoinonen/ot-harjoitustyo/blob/master/dokumentaatio/testaus.png)
