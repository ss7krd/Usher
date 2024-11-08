# Usher

This repository contains the preliminary codes for the system Usher accepted at OSDI 2024. The necessary packages and their versions are as follows:
```
# Name                    Version                   Build
_libgcc_mutex             0.1                        main  
_openmp_mutex             5.1                       1_gnu  
_tflow_select             2.1.0                       gpu  
absl-py                   0.15.0             pyhd3eb1b0_0  
aiohttp                   3.8.1            py37h7f8727e_1  
aiosignal                 1.2.0              pyhd3eb1b0_0  
astor                     0.8.1            py37h06a4308_0  
astunparse                1.6.3                      py_0  
async-timeout             4.0.1              pyhd3eb1b0_0  
asynctest                 0.13.0                     py_0  
attrs                     21.4.0             pyhd3eb1b0_0  
blas                      1.0                         mkl  
blinker                   1.4              py37h06a4308_0  
brotlipy                  0.7.0           py37h27cfd23_1003  
c-ares                    1.18.1               h7f8727e_0  
ca-certificates           2022.07.19           h06a4308_0  
cachetools                4.2.2              pyhd3eb1b0_0  
certifi                   2022.6.15        py37h06a4308_0  
cffi                      1.15.1           py37h74dc2b5_0  
charset-normalizer        2.0.4              pyhd3eb1b0_0  
click                     8.0.4            py37h06a4308_0  
cryptography              37.0.1           py37h9ce1e76_0  
cudatoolkit               10.1.243             h6bb024c_0  
cudnn                     7.6.5                cuda10.1_0  
cupti                     10.1.168                      0  
dataclasses               0.8                pyh6d0b6a4_7  
frozenlist                1.2.0            py37h7f8727e_0  
gast                      0.4.0              pyhd3eb1b0_0  
google-auth               2.6.0              pyhd3eb1b0_0  
google-auth-oauthlib      0.4.4              pyhd3eb1b0_0  
google-pasta              0.2.0              pyhd3eb1b0_0  
grpcio                    1.42.0           py37hce63b2e_0  
h5py                      2.10.0           py37hd6299e0_1  
hdf5                      1.10.6               hb1b8bf9_0  
idna                      3.3                pyhd3eb1b0_0  
importlib-metadata        4.11.3           py37h06a4308_0  
intel-openmp              2021.4.0          h06a4308_3561  
keras-preprocessing       1.1.2              pyhd3eb1b0_0  
ld_impl_linux-64          2.38                 h1181459_1  
libffi                    3.3                  he6710b0_2  
libgcc-ng                 11.2.0               h1234567_1  
libgfortran-ng            7.5.0               ha8ba4b0_17  
libgfortran4              7.5.0               ha8ba4b0_17  
libgomp                   11.2.0               h1234567_1  
libprotobuf               3.20.1               h4ff587b_0  
libstdcxx-ng              11.2.0               h1234567_1  
markdown                  3.3.4            py37h06a4308_0  
mkl                       2021.4.0           h06a4308_640  
mkl-service               2.4.0            py37h7f8727e_0  
mkl_fft                   1.3.1            py37hd3c417c_0  
mkl_random                1.2.2            py37h51133e4_0  
multidict                 5.2.0            py37h7f8727e_2  
ncurses                   6.3                  h5eee18b_3  
numpy                     1.21.5           py37h6c91a56_3  
numpy-base                1.21.5           py37ha15fc14_3  
oauthlib                  3.2.0              pyhd3eb1b0_1  
openssl                   1.1.1q               h7f8727e_0  
opt_einsum                3.3.0              pyhd3eb1b0_1  
pip                       22.1.2           py37h06a4308_0  
protobuf                  3.20.1           py37h295c915_0  
pyasn1                    0.4.8              pyhd3eb1b0_0  
pyasn1-modules            0.2.8                      py_0  
pycparser                 2.21               pyhd3eb1b0_0  
pyjwt                     2.4.0            py37h06a4308_0  
pyopenssl                 22.0.0             pyhd3eb1b0_0  
pysocks                   1.7.1                    py37_1  
python                    3.7.13               h12debd9_0  
python-flatbuffers        2.0                pyhd3eb1b0_0  
readline                  8.1.2                h7f8727e_1  
requests                  2.28.1           py37h06a4308_0  
requests-oauthlib         1.3.0                      py_0  
rsa                       4.7.2              pyhd3eb1b0_1  
scipy                     1.7.3            py37hc147768_0  
setuptools                61.2.0           py37h06a4308_0  
six                       1.16.0             pyhd3eb1b0_1  
sqlite                    3.39.2               h5082296_0  
tensorboard               2.8.0            py37h06a4308_0  
tensorboard-data-server   0.6.0            py37hca6d32c_0  
tensorboard-plugin-wit    1.8.1            py37h06a4308_0  
tensorflow                2.4.1           gpu_py37ha2e99fa_0  
tensorflow-base           2.4.1           gpu_py37h29c2da4_0  
tensorflow-estimator      2.6.0              pyh7b7c402_0  
tensorflow-gpu            2.4.1                h30adc30_0  
termcolor                 1.1.0            py37h06a4308_1  
tk                        8.6.12               h1ccaba5_0  
typing-extensions         4.3.0            py37h06a4308_0  
typing_extensions         4.3.0            py37h06a4308_0  
urllib3                   1.26.11          py37h06a4308_0  
werkzeug                  2.0.3              pyhd3eb1b0_0  
wheel                     0.37.1             pyhd3eb1b0_0  
wrapt                     1.14.1           py37h5eee18b_0  
xz                        5.2.5                h7f8727e_1  
yarl                      1.6.3            py37h27cfd23_0  
zipp                      3.8.0            py37h06a4308_0  
zlib                      1.2.12               h7f8727e_2
```

sm_requirement.py and memory_requirements have the codes for calculating the resource requirements.

scheduling.py has the code for the scheduling policy.

Other files have the codes for the DL models.

A file can be executed with `python3 filename`
