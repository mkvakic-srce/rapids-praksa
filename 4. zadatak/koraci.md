#### instalacija Conda-e:
```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh
# instalacija u /usr/local/miniforge3
```

#### instalacija NVIDIA CUDA drivera (libcuda.so modula za RHEL)
```bash
dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo
```

#### NVIDIA Open GPU Kernel Modules
```bash
dnf module install nvidia-driver:latest-dkms
```

```bash
ls /lib64/ | grep libcuda.so
libcuda.so
libcuda.so.1
libcuda.so.460.27.04
```

#### instalacija rapids-a i CUDA toolkita za Rocky Linux release 8.5
```bash
conda create -n rapids-22.04 -c rapidsai -c nvidia -c conda-forge rapids=22.04 python=3.9 cudatoolkit=11.7
```

#### povezivanje jupyter-a i rapids-a
```bash
conda activate rapids-22.04
python -m ipykernel install --name=rapids-22.04
```
``` bash
Installed kernelspec rapids-22.04 in /usr/local/share/jupyter/kernels/rapids-22.04
```

#### check if installed
```python
import cudf
```

    /usr/local/miniforge3/envs/rapids-22.04/lib/python3.9/site-packages/cudf/utils/gpu_utils.py:142: UserWarning: No NVIDIA GPU detected warnings.warn("No NVIDIA GPU detected")

#### check for GPU
```bash
# emulated GPU na KVM virtualki je Cirrus Logic, niđe eNvidije
(rapids-22.04) [root@jhub-jahusicvsite ~]# lshw -C video
  *-display
       description: VGA compatible controller
       product: GD 5446
       vendor: Cirrus Logic
       physical id: 2
       bus info: pci@0000:00:02.0
       logical name: /dev/fb0
       version: 00
       width: 32 bits
       clock: 33MHz
       capabilities: vga_controller rom fb
       configuration: depth=16 driver=cirrus latency=0 resolution=1024,768
       resources: irq:0 memory:fc000000-fdffffff memory:febd0000-febd0fff memory:c0000-dffff
```

