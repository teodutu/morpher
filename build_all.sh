cd Morpher_DFG_Generator
mkdir build
cd build
cmake ..
make all -j 8
cd ../../Morpher_CGRA_Mapper
mkdir build
cd build
cmake ..
make all -j8
cd ../../hycube_simulator
cd src
mkdir build
cd build
cmake ..
make all -j8
echo "buld success!!!"
