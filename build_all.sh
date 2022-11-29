cd Morpher_DFG_Generator
mkdir build
cd build
cmake ..
make  -j 12
cd ../../Morpher_CGRA_Mapper
mkdir build
cd build
cmake ..
make all -j 12
cd ../../hycube_simulator
cd src
mkdir build
cd build
cmake ..
make all -j 12
echo "buld success!!!"
