#!/bin/bash

# pripremiti knjižnicu za MPI
module load mpi/openmpi41-x86_64

# stvoriti virtualno okruženje za mpi4py
python3 -m venv --system-site-packages venv-mpi4py

# aktivacija virtualnog okruženja
source venv-mpi4py/bin/activate

# instalirati mpi4py sa pipom 
pip install mpi4py

# deaktivacija virtualnog okruženja
deactivate
