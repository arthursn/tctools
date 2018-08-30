from setuptools import setup

setup(
    name='tctools',
    version='0.1dev',
    description='',
    author='Arthur Nishikawa',
    author_email='nishikawa.poli@gmail.com',
    url='https://github.com/arthursn/tctools',
    packages=['tctools'],
    install_requires=['numpy', 'matplotlib', 'scipy',
                      'pandas', 'periodictable', 'openpyxl'],
    long_description=open('README.md').read(),
)
