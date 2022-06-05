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
olakšavaju razvoj aplikacija putem izoliranih instalacijskih okolina (python
modul `venv`). Korištenjem virtualnog okruženja, pripremiti okolinu koja će
omogućiti razvoj i izvršavanje prethodnog programa na više čvorova pomoću
standarda MPI. Vještine koje bi se usvojile su:

- Upoznavanje s Python virtualnim okruženjima i instalacijskim upraviteljem `pip`
- Korištenje Modulefile alata za korištenje Isabellinih aplikacija i knjižnica
- Paralelizacija koda korištenjem standarda MPI

### Zadaci
1. Pripremiti virtualno okruženje `venv-mpi4py` korištenjem python modula
   `venv` i instalirati paket `mpi4py` korištenjem `pip`-a
2. Paralelizirati prethodni program množenja liste (`double-mpi4py.py`)
   korištenjem MPI standarda putem python knjižnice `mpi4py`
3. Podnijeti posao putem sistema SGE (`double-mpi4py.py`) i provjeriti vrijeme
   izvršavanja u ovisnosti o broju jezgri (npr. 1, 2, 4, 8)

### Bibliografija
- [Python virtualna okruženja](https://realpython.com/python-virtual-environments-a-primer)
- [Pip](https://packaging.python.org/en/latest/tutorials/installing-packages)
- [Korisničke aplikacije i knjižnice](https://wiki.srce.hr/pages/viewpage.action?pageId=25133120)
- [mpi4py](https://mpi4py.readthedocs.io/en/stable/intro.html#what-is-mpi)

## Zadatak 3 - Conda virtualna okruženja i rapids

Ovaj zadatak posvetiti će se pripremi i razvoju aplikacija ubrzanih GPU
jezgrama. Kao i u prošlom zadatku, stvoriti će se virtualno okruženje, no ovaj
put korištenjem instalacijskog upravitelja `conda`. Program množenja prevesti će
se korištenjem python knjižnice `rapids` i podnijeti na čvorove s grafičkim
procesorima. Vještine koje bi se usvojile su:

- Upoznavanje s instalacijskih upraviteljem `conda`
- Upoznavanje sa sučeljem CUDA i knjižnicom `rapids`
- Paralelizacija koda korištenjem GPU jezgri
- Podnošenje poslova na čvorove s GPU jezgrama

### Zadaci
1. Pripremiti virtualno okruženje `venv-rapids` korištenjem instalacijskog
   upravitelja `conda` i instalirati knjižnicu `rapids`
2. Paralelizirati program množenja liste (`double-rapids.py`) korištenjem
   `rapids`-ovog modula `cuDF` i funkcije `apply_rows`
3. Podnijeti posao putem sistema SGE (`double-rapids.sge`) i provjeriti vrijeme
   izvršavanja

### Bibliografija
- [Conda na Isabelli](https://wiki.srce.hr/display/RKI/Conda)
- [GPU na Isabelli](https://wiki.srce.hr/pages/viewpage.action?pageId=27690375)
- [Uvod u CUDU](https://developer.nvidia.com/blog/even-easier-introduction-cuda)
- [rapids](https://rapids.ai/start.html)
- [cuDF](https://docs.rapids.ai/api/cudf/stable/index.html)
