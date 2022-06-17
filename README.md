# Rapids praksa

## Zadatak 1 - Osnove Isabelle i pythona

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

## Zadatak 4 - Rapids i CUDA na HTC-u

Ovaj zadatak posvećen je osnovama sistemske administracije HTC servisa i
pripremanju okoline za korištenje knjižnice `rapids`. Kao i u prošlom zadatku,
oslanjati ćemo se na instalacijski paket `conda` i knjižnicu za GPU ubrzanje
`CUDA`, no ovaj put instalacijom svih paketa na virtualni čvor kao `root`
korisnik. Na kraju, pripremiti ćemo i testirati JupyterLab okolinu koja
omogućuje razvoj aplikacija korištenjem knjižnice `rapids`.

- Upoznavanje s tehnologijom HTC
- Upoznavanje s JupyterLabom i njegovom implementacijom na klasteru Isabella
- Osnove sistemske administracije Red-Hat/CentOS distribucije
- Upoznavanje s konfiguracijom JupyterLab servisa pomoću IPython kernela

### Zadaci
1. Kreirati račun za HTC servis, spojiti se na <https://jupyter-dev.cro-ngi.hr>
   s instancom `XLarge` i ulogirati se kao `root`
2. Instalirati `condu` putem Miniforgea u `/usr/local/miniforge3`
3. Instalirati knjižnicu `CUDA` za distribuciju `Rocky Linux release 8.5 (Green Obsidian)`
4. Pripremiti `rapids-22.04` virtualno okruženje putem instalacijskog paketa `conda`
5. Pripremiti JupyterLab kernel povezan na `rapids-22.04` okruženje putem
   knjižnice `ipykernel`
6. Testirati uspješnost instalacije knjižnice `rapids` u JupyterLab notebooku
   pozivanjem knjižnice `cudf`

### Bibliografija
- [HTC na Isabelli](https://wiki.srce.hr/display/CRONGI/HTC+Cloud)
- [JupyterLab](https://docs.jupyter.org/en/latest/)
- [JupyterLab na Isabelli](https://wiki.srce.hr/display/CRONGI/JupyterLab+servisi)
- [Miniforge](https://github.com/conda-forge/miniforge)
- [Instalacija knjižnice CUDA](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
- [IPython kernel](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)

## Zadatak 5 - Optimizacija znanstvene aplikacije korištenjem CUDA-e

Zadnji zadatak posvećen je optimizaciji znanstvene aplikacije korištenjem MPI i
CUDA sučelja. Nakon laganog upoznavanja s problematikom simulacije n-tijela
(kroz najednostavniju inačicu programa) pripremiti ćemo okruženje za
paralelizaciju python koda i pokušati ga učiniti efikasnijim.

- Upoznavanje s problematikom simulacije n-tijela
- Upoznavanje s python knjižnicom `numba`
- Paralelizacija koda korištenjem sučelja MPI i CUDA

### Zadaci
1. Pripremiti virtualnu okolinu s knjižnicom `numba`
2. Proučiti program `nbody.py` i identificirati način optimizacije koda
3. Paralelizirati program sučeljima MPI pomoću `mpi4py` (`nbody-mpi4py.py`) i
   CUDA pomoću `numbe` (`nbody-numba.py`)
4. Usporediti vrijeme izvršavanja različitih verzija programa sa serijskom

### Bibliografija
- [Simulacija n-tijela](https://www.astrosen.unam.mx/~aguilar/MySite/Teaching_files/GH06_Intro_NBody.pdf)
- [CUDA pomoću numbe](https://numba.pydata.org/numba-doc/latest/cuda/index.html)
- [CUDA simulacija n-tijela](https://developer.nvidia.com/gpugems/gpugems3/part-v-physics-simulation/chapter-31-fast-n-body-simulation-cuda)
