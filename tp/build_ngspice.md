# How to build ngspice from source code


## Setup

Setup a location to install ngspice, for example you can go to your 
home location (`~` represents your home `/home/your_name`) :
```shell
cd ~
```

Create some directory (`mkdir`) that will contains the install :
```shell
mkdir tools
```


## Get source code

Go back to some directory where you will clone ngspice repository. Then 
check ngspice website and find the github mirror repository. Clone it 
into some folder (e. g. ngspice) :
```shell
git clone https://github.com/danchitnis/ngspice-sf-mirror.git ngspice
```

Go into the newly cloned repository :
```shell
cd ngspice
```

Check tags to find a stable version of the code (or keep as is and 
build with the latest modifications) :
```
git tags -n1
```

Take the version you prefer, latest is 43 when writting this file, then 
checkout to this tag commit :
```shell
git checkout ngspice-43
```

The next steps are from the INSTALL file of the repository :
```shell
./autogen.sh
mkdir build
cd build
```

The next step is to configure the build before doing it, the 
recommended arguements are :
```shell
../configure --with-x --enable-cider --enable-predictor --with-readline=yes --disable-debug --prefix=/home/your_name/tools
```
- with-x : enable graphical interface
- enable-cider : recommended (voir INSTALL file)
- enable-predictor : recommended (voir INSTALL file)
- with-readline : allow to manipulate text in the ngspice terminal 
                  (left/right arrows to move between characters, 
                  up/down arrows to move between commands history)
- disable-debug : remove debug element in the produced binary
- prefix : install location of ngspice (three directories are inside : 
           bin, lib, share)

> Ensure to use the right prefix (the one defined at the beginning 
> setup step)

Then build :
```shell
make
make install
```

> At the end you can erase entirely the ngspice cloned directory :
```shell
cd ../..
rm -rf ngspice
```
