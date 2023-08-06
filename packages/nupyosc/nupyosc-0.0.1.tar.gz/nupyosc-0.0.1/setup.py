from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'NuPy: A new way to numerically compute neutrino oscillations in matter'
LONG_DESCRIPTION = 'We use the recently discovered Eigenvalue-Eigenvector and Adjugate Identities to compute oscillation probabilities with minimal algorithmic steps'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="nupyosc", 
        version=VERSION,
        author="Baalateja Kataru",
        author_email="<kavesbteja@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['numpy'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['probability', 'neutrino', 'oscillations'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)