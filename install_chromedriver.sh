#!/bin/bash

cd $HOME/Downloads
curl -O https://chromedriver.storage.googleapis.com/2.33/chromedriver_mac64.zip
unzip chromedriver_mac64.zip
mkdir -p $HOME/bin
mv chromedriver $HOME/bin
echo "export PATH=$PATH:$HOME/bin" >> $HOME/.bash_profile
echo "installation done"
