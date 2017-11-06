#!/bin/bash
if [[ $# -eq 0 ]] ; then
   NAME="blockwoche"
else
  NAME=$1
fi

# FILE="Miniconda2-latest-MacOSX-x86_64.sh "
# if [ -f $FILE ]; then
#    echo "Miniconda File Miniconda2-latest-MacOSX-x86_64.sh liegt im Ordner. Alles gut"
#    sh $FILE
# else
#    echo "Miniconda File Miniconda2-latest-MacOSX-x86_64.sh liegt nicht im Ordner."
#    echo "Bitte in diesen Folder kopieren:"; pwd
#    exit
# fi
# remove anaconda environment
conda remove -y --name $NAME --all

# change to anaconda3 folder
#cd ~/anaconda3/bin/

# install stuff
conda create -y -n $NAME python=2.7
conda install -y -n $NAME jupyter
conda install -y -n $NAME ipython
conda install -y -n $NAME -c conda-forge markovify
conda install -y -n $NAME -c conda-forge selenium
conda install -y -n $NAME -c conda-forge tweepy
conda install -y -n $NAME beautifulsoup4
conda install -y -n $NAME -c conda-forge googlemaps
conda install -y -n $NAME -c anaconda pycairo
conda install -y -n $NAME -c anaconda cairo

#echo 'export PATH=$HOME/anaconda3/bin:$PATH' >> ~/.bash_profile
