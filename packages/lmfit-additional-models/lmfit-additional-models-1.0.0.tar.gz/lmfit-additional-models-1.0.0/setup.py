from setuptools import setup, find_packages

setup(
    name='lmfit-additional-models',
    version='1.0.0',
    author='Julian Hochhaus',
    author_email='julian.hochhaus@tu-dortmund.de',
    description='This package contains additional models for the lmfit package. '
                'The models are designed for fitting XPS spectra. This package contains '
                'background models such as Shirley, Tougaard and Slope background as well as peak models '
                'such as convoluted Gaussian/Doniach-Sunjic models. In addition, a convolution of a '
                'thermal distribution with a Gaussian is provided for fitting the fermi edge.'
                'The models are based on the lmfit package and can be used in the same way as the models from lmfit.',
    packages=find_packages(),
    install_requires=['scipy', 'numpy', 'lmfit'],
)