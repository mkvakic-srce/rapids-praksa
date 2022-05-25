# Jasmin praksa - rapids

## Zadatak 1 - Osnove Isabelle, pythona i paralelnog računanja

Prvi zadatak posvećen je upoznavanju s HPC tehnologijama korištenjem klastera
Isabelle, i primarno će se fokusirati na pisanje i izvršavanje skripta koje se
oslanjaju na više-jezgreno ubrzanje. Vještine koje bi se usvojile su:

- Rad u Linuxu na terminalu putem sjednice SSH
- Pisanje osnovnih bash i python skripta
- Upoznavanje s klasterom Isabella i sustavom za podnošenje poslova SGE
- Upoznavanje s osnovama paralelizacije putem pythona i podnošenje posla na više jezgri

### Zadaci
1. Napisati python program (`hello.py`) koji na ekranu ispisuje “Hello world!”
   10 puta putem for petlje, a koji se poziva bash skriptom (`hello.sh`)
2. Napraviti paralelnu verziju programa (`hello_parallel.py`) korištenjem
   funkcije map iz multiprocessing modula koja ovisno o broju zatraženih jezgri
   (`NSLOTS`) pri podnošenju posla (`hello_parallel.sge`) ispisuje odgovarajući
   broj “Hello world!” datoteka (npr. `hello_1.out`)
3. Pomnožiti listu brojeva od 1 od 10**8 (`double.py`) koristeći istu
   metodologiju i provjeriti vrijeme izvršavanja programa (`double.sge`) u
   ovisnosti o broju jezgri

_Napomena: pri paralelizaciji treba paziti da se posao ne širi izvan jednog čvora_

### Bibliografija
- [Pristup Isabelli](https://wiki.srce.hr/display/RKI/Pristup)
- [Osnove pythona](https://www.learnpython.org)
- [Podnošenje poslova putem SGE](https://wiki.srce.hr/display/RKI/Pokretanje+i+upravljanje+poslovima)
- [Python multiprocessing](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing)
