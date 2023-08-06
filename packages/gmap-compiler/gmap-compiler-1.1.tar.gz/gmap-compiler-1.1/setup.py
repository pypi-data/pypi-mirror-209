from setuptools import setup, find_packages

setup(
    name='gmap-compiler',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'networkx',
        'numba',
        'scipy',
        'simanneal',
    ],
    author='Jimmy Weber',
    author_email='jimmy.weber@ini.ethz.ch',
    description='A versatile, easy-to-use and open-source compiler that can efficiently map any arbitrary connectivity matrix to various hardware architectures.',
    url='https://github.com/EIS-Hub/GMap',
)

# To update the package, run "python setup.py sdist"
# twine upload dist/gmap-compiler-0.3.tar.gz --verbose
