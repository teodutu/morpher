#! /bin/bash

cd Morpher_DFG_Generator
mkdir build
cd build
cmake ..
make all -j `nproc`
cd ../../Morpher_CGRA_Mapper
mkdir build
cd build
cmake ..
make all -j `nproc`
cd ../../hycube_simulator
cd src
mkdir build
cd build
cmake ..
make all -j `nproc`
echo "buld success!!!"
