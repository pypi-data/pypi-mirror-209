from setuptools import setup, find_packages

setup(
    name='pyrc-python-utils',
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    url='',
    license='',
    author='Paul Vienneau',
    author_email='',
    description='Generic set of helper functions',
    install_requires=["O365>=2.0.26", "paramiko>=3.1.0", "pymsteams>=0.2.2"]
)
