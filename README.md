# pcrawler

Written in Python 2.7. Tested in Windows 8.1 and Ubuntu 16.04.

## Requirements

If you don't have pip installed, [do it](https://pip.pypa.io/en/stable/installing/).

Altough not necessary, I advise you to use a [virtual environment](https://packaging.python.org/installing/#creating-and-using-virtual-environments).

Ok, now, in a terminal, go to the root of the project and enter:

`pip install -r requirements.txt`

This will install all the dependencies needed to run the program. If you're on Windows, the installation of [lxml](http://lxml.de/) will probably raise an error. If this happens, go to this [page](http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) and download the file that corresponds to your needs. I, for example, downloaded the file called `lxml-3.6.4-cp27-cp27m-win32.whl`. In a terminal, go to the folder where you saved this file and enter this:

`pip install lxml-3.6.4-cp27-cp27m-win32.whl`

Then go back to the root of the project and do `pip install -r requirements.txt` once again, so that everything is installed correctly.

## How to run the program

You'll have to run the program in a shell that supports bash. I've tested in Cygwin (2.5.2) and Git BASH. Go to the root of the project and enter:

`python pcrawler_service.py`

This will start a flask server on http://localhost:5001/passatempos . You can go to this URL to check if everything is working alright. You should see a JSON. If it takes a while to load it could be because it's running all the spiders.

The webservice only accepts GET requests to the URL above. You can find a front-end interface for this project [here](https://github.com/LLCampos/lazy_passatempos).

