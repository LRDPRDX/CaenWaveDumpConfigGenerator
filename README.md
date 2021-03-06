# GUI for generation of CAEN WaveDump configuration files

## Introduction
This is a graphical user interface for generation of configuration files for the CAEN
[WaveDump](https://www.caen.it/products/caen-wavedump/) software written in python and based on
the Tkinter package.

## Disclaimer
For now, it contains *ONLY* the configuration options that are
available for *ALL* CAEN digitizers (particularly because I am able to test it on the
N6720A board only). Also it doesn't contain the register's operations yet.

## System requirements
  * Python 2.7.x or Python 3.x
  * Packages for Python:
    - Tkinter (ttk, tkFileDialog, tkFont in case of Python 2)

## Installation
Change to the `package_dir/src`. Make executable:
```
$ chmod +x caenccf
```
Add the executable into the standard location:
```
$ cp caenccf /usr/bin/
```
Extend the `PYTHONPATH` by adding the following line into your `.profile` (or `.bash_profile` if that is what you have):
```
if [[ -n "$PYTHONPATH" ]]; then
    PYTHONPATH=$PYTHONPATH:/path/to/<package_dir>/src
else
    export PYTHONPATH=/path/to/<package_dir>/src
fi;
```
Now log out and login back and run:
```
$ caenccf
```
You should see the starting page:

<p float="center">
  <img src="pictures/documentation/gui/start_page.png" height="500">
</p>

## Usage
For the usage see the documentation (Sec. **Usage**).

## Documentation
The documentation is available [here](/doc/users_guide.pdf).

## Feedback
Report bugs and/or suggest to paradox1859@gmail.com

## TODO's
- [ ] Add board identifier (for the proper time scale)
- [ ] Add register's operations
- [ ] Add configure options for VME and 742 series digitizers
