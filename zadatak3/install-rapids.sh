#!/bin/bash

# podigni CUDA knjižnicu
module load cuda/11-2

# aktiviraj condu
source /apps/miniforge3/bin/activate

# stvori virtualno okruženje za rapids
conda create -n rapids-22.04 -c rapidsai -c nvidia -c conda-forge rapids=22.04 python=3.9 cudatoolkit=11.2