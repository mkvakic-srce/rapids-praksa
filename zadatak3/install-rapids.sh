#!/bin/bash

# podigni CUDU 11.2
module load cuda/11-2

# aktiviraj condu
source /apps/miniforge3/bin/activate

# stvori virtualno okruženje za rapids
conda create --prefix venv-rapids \
    -c rapidsai -c nvidia -c conda-forge  \
    rapids=22.04 python=3.8
