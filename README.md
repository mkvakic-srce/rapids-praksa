# Jasmin praksa

## Zadatak 1 - Osnove Isabelle, pythona i paralelnog računanja

Prvi zadatak posvećen je upoznavanju s HPC tehnologijama korištenjem klastera
Isabelle, i primarno će se fokusirati na pisanje i izvršavanje skripta koje se
podnose na sustav za raspodjeljivanje poslova SGE. Vještine koje bi se usvojile
su:

- Rad u Linuxu na terminalu putem sjednice SSH
- Pisanje osnovnih bash i python skripta
- Upoznavanje s klasterom Isabella i sustavom za podnošenje poslova SGE

### Zadaci
1. Napisati python program (`hello.py`) koji na ekranu ispisuje “Hello world!”
   deset puta i koji se poziva bash skriptom (`hello.sh`)
2. Napisati SGE skriptu (`hello.sge`) koja podnosi prethodni program
   (`hello.py`) i ispisuje rezultate u direktorij `output`
3. Napisati program koji for petljom zbraja listu brojeva do 10**8 (`sum.py`),
   izvršiti ga SGE skriptom (`sum.sge`) i ispisati vrijeme izvršavanja
   korištenjem bash komande `time`

### Bibliografija
- [Pristup Isabelli](https://wiki.srce.hr/display/RKI/Pristup)
- [Osnove pythona](https://www.learnpython.org)
- [Podnošenje poslova putem SGE](https://wiki.srce.hr/display/RKI/Pokretanje+i+upravljanje+poslovima)

## Zadatak 2 - Python virtualna okruženja i MPI

Svrha ovog zadatka je upoznavanje s Python virtualnim okruženjima koja
olakšavaju razvoj aplikacija putem izoliranih instalacijskih okolina.
Korištenjem virtualnog okruženja, pripremiti okolinu koja će omogućiti razvoj i
izvršavanje prethodnog programa na više čvorova pomoću MPI. Vještine koje bi se
usvojile su:

- Upoznavanje s Python virtualnim okruženjima i instalacijskim upraviteljem `pip`
- Korištenje Modulefile alata za korištenje Isabellinih aplikacija i knjižnica
- Osnove paralelizacije koda korištenjem MPI standarda

### Zadaci
1. Pripremiti virtualno okruženje `venv-mpi4py` korištenjem python modula
   `venv` i instalirati paket `mpi4py` 
2. Paralelizirati prethodni program množenja liste (`double-mpi4py.py`)
   korištenjem MPI standarda putem python knjižnice `mpi4py`

### Bibliografija
- [Python virtualna okruženja](https://realpython.com/python-virtual-environments-a-primer)
- [Pip](https://packaging.python.org/en/latest/tutorials/installing-packages)
- [Korisničke aplikacije i knjižnice](https://wiki.srce.hr/pages/viewpage.action?pageId=25133120)
- [mpi4py](https://mpi4py.readthedocs.io/en/stable/intro.html#what-is-mpi)
