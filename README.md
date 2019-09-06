# tctools

Python tools for manipulation of Thermo-Calc&reg; output data.

# Installation and requirements

tctools runs in python >= 2.7 using the following non-standard python libraries:

- numpy
- matplotlib
- scipy
- pandas
- periodictable
- openpyxl
- xlwt

First clone tctools repository:

```bash
git clone https://github.com/arthursn/tctools
```

Then install tctools by running setup.py with the `--user` option to install tctools in the user folder:

```bash
python setup.py install --user
```

Please notice that `setuptools` must be installed beforehand.

If tctools is installed using `setup.py`, all dependencies should be automatically solved. Otherwise, the required libraries can be installed from the [Python Package Index](https://pypi.org) using pip:

```bash
pip3 install numpy matplotlib scipy pandas periodictable openpyxl xlwt
```

