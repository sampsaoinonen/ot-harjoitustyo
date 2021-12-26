![arkkitehtuuri](https://github.com/sampsaoinonen/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.png)

## Pelilogiikan sekvenssikaavio

![sekvenssikaavio](https://github.com/sampsaoinonen/ot-harjoitustyo/blob/master/dokumentaatio/sekvenssikaavio.png)


## Käyttöliittymä sisältää 6 erilaista näkymää:

- Mainmenu, jossa samassa kirjautuminen
- Hiscore, johon haetaan tietokannasta viisi parasta suoritusta
- Options, josta saa valita pelin nopeuden
- Instructions, jossa kerrotaan lyhyesti peliohjeet
- Pelinäkymä, klassinen matopeli näkymä
- Game Over, jossa ilmoitetaan käyttäjän pisteet

Näkymät näytetään yksi kerrallaan. Pelinäkymä on toteutettu omissa luokissaan kun taas muut menun näkymät ovat menu.py luokassa omina metodeina. Kaikki ovat toteutettu PyGamella. Käyttöliittymä on erotettu lähes täysin pelilogiikasta. Käyttöliittymä vain antaa pelinopeuden ja ottaa vastaan pistemäärän pelilogiikalta. Tietokantaan käyttöliittymä pitää yhteyden database-hakemistossa olevia luokkia ja niiden metodeja käyttäen.

## Yhteys tietokantaan

Yhteys tietokantaan luodaan database_connection.py:ssa. Sovelluksen käynnistyessä tietokanta tyhjennetään tauluista ja luodaan Users-taulu database_init.py:n avulla. Users-tauluun tallenetaan käyttäjänimi sekä pisteet. UserRepository antaa käyttöliittymälle taulukosta viisi parasta suoritusta sekä tallentaa käyttäjän tiedot, jos pisteet riittävät viiden joukkoon. 

