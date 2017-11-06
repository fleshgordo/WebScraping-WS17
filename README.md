# Datenströme analysieren, bearbeiten und programmieren

Interactives Python notebook mit Basic Python crash course für Anfänger und Fokus auf Web-Scraping Techniken, Browser Fremdsteuerung, Tips und Tricks wie man Daten aus dem Internet zieht und in andere Formate bringt.

## Installation

### Installation Mac

Zunächst bitte Anaconda installieren. Hier der Download [Link](https://conda.io/miniconda.html) 

Danach installiere wir noch einige zusätzliche Python Pakete. Das Skript install_anaconda.sh auf den Desktop herunterladen. Danach Terminal öffnen und folgendes eintippen:

~~~
cd Desktop
chmod +x install_anaconda.sh
./install_anaconda.sh
~~~

Alles mit __yes__ beantworten. Das dauert etwas aber sollte ohne Fehler nach einigen Minuten fertig sein.

Danach muss man die neue virtuelle Python Umgebung aktivieren:
```
source activate blockwoche
```

Jetzt müsste in eurer Terminal Zeile immer Blockwoche vor dem Befehl stehen.

Wechselt nun in das Verzeichnis wo ihr das Zip File entpackt habt. Im Terminal folgendes tippen:

```
cd
```

Und aus dem Finder das aktuelle Verzeichnis mit der Maus hineinziehen (drag&drop). Bei mir ergibt das beispielsweise folgendes:

```
cd Desktop/2017_zhdkblock/Code/
```

Danach könnt ihr einfach Jupyter starten

```
jupyter-notebook
```

### Permanente Installation osX

Mit Anaconda kreiert man eine virtuelle Python Instanz. Falls ihr diese nicht aktiviert mit __source activate blockwoche__ habt ihr nicht dieselbe Pakete zur Verfügung. Falls ihr alle permanent auf euren Rechner installieren wollt, dann verwendet am besten pip

```
sudo easy_install pip
pip install selenium -—user
pip install tweepy -—user
pip install bs4 --user
pip install googlemaps --user
pip install markovify --user
pip install jupyter --user
pip install ipython --user
```

### Installation Linux

```
sudo apt-get install python-pip
sudo pip install jupyter
sudo pip install selenium
sudo pip install tweepy
sudo pip install bs4
sudo pip install googlemaps
sudo pip install markovify
```
### Installation Windows

### Windows

Download miniconda 2.7 Version hier: https://conda.io/miniconda.html

Danach kann man in Windows das Programm **anaconda Prompt** öffnen.

Folgende Befehle muss man ausfuehren (Zeile für Zeile und mit Enter bestätigen)

```
conda create -y -n blockwoche python=2.7
conda install -y -n blockwoche jupyter
conda install -y -n blockwoche ipython
conda install -y -n blockwoche -c conda-forge markovify
conda install -y -n blockwoche -c conda-forge tweepy
conda install -y -n blockwoche -c conda-forge selenium
conda install -y -n blockwoche beautifulsoup4
conda install -y -n blockwoche -c conda-forge googlemaps
activate blockwoche
jupyter-notebook
```

### Selenium IDE

Selenium IDE Firefox plugin https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/
Funktioniert nur mit Firefox < version 54
Download hier: https://ftp.mozilla.org/pub/firefox/releases/54.0/mac/en-GB/

### Notes on python2 and python3

The interactive notebook is written for python2, hence they won't work if your notebook is interpreting them in python3. To install python2 for jupyter follow this procedure in terminal:

~~~
python2 -m pip install --upgrade ipykernel # install the kernel package for Python 2
python2 -m ipykernel install # register the Python 2 kernelspec
~~~
