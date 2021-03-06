#Introduction to Geospatial Development

This is a brief introduction to Geographic Information Systems (GIS) for 
undergraduate students in computer science. It covers what I think are the 
essentials one should know when working with spatial data: 

1. data types
2. scale
3. projections

After a brief survey of these topics, a few reasons for why computer science
students may want to learn about GIS are presented. Finally, we'll make a 
simple web map application using Python, Leaflet, and the Yelp API.

##Downloading the project and Configuring Python

###Cloning the repository
Use the `git clone` command to fetch the contents of this repository:
```bash
git clone https://github.com/egoddard/geospatial_colloquium.git
```

###Move into the directory containing the tutorial
####Linux/OSX:
```bash
cd geospatial_colloquium/tutorial
```
####Windows:
```bash
cd geospatial_colloquium\tutorial
```

###Create a Python virtual Environment
####OSX
```bash
pyvenv venv
```
####Linux
If you are not using a Debian or Ubuntu derivative, the OSX command above 
should work for you. Unfortunately, Debian and Ubuntu (and Linux Mint) ship 
with a broken pyvenv. We can still use it, but we have to manually install pip: 
```bash
#Debian/Ubuntu/Mint append the python version to the end of pyvenv
pyvenv-3.4 --without-pip venv
curl https://bootstrap.pypa.io/get-pip.py | venv/bin/python
```
####Windows
Windows usually does not add the python interpreter to the environment path, 
so you have to use the full path name for the interpreter and the script:
```bash
c:\Python34\python c:\Python34\Tools\Scripts\pyvenv.py venv
```

###Activate the virtual environment
####Linux/OSX
```bash
source venv/bin/activate
```
####Windows
On Windows, please use cmd.exe, not Powershell. Script execution is disabled 
by default in Powershell, which causes activation of the virtual environment 
to fail.
```batchfile
venv\Scripts\activate.bat
```

###Install the required Python libraries
Once the virtual environment is activated, python can be run from the command 
line by invoking `python` and will work on all platforms. To install the 
python libraries we'll be using, run `pip install -r requirements.txt`.

###Deactivating the virtual environment
The Python virtual environment is only applied to the terminal in which it was 
activated. Closing the terminal will kill the virtual environment. If you want 
to use it again, run the activation command above for your platform.

To close the virtual environment without closing the terminal, use the 
`deactivate` command.
