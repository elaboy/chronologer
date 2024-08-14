from setuptools import setup, find_packages

VERSION = '0.0.20' 
DESCRIPTION = 'HI predicting model'
LONG_DESCRIPTION = 'Chronologer is a deep learning model for highly accurate prediction of peptide C18 retention times (reported in % ACN). Chronologer was trained on a new large harmonized database of >2.6 million retention time observations (2.25M unique peptides) constructed from 11 community datasets and natively supports prediction of 17 different modification types. With only a few observations of a new modification type (>10 peptides), Chronologer can be easily re-trained to predict up to 10 user supplied modifications.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="chronologer", 
        version=VERSION,
        author="Code from searlelab, packed by Edwin Laboy",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(where="chronologer"),
        install_requires=["torch", "torchvision", "torchaudio",
                          "pyteomics==4.5.5", "pandas==1.4.3", "scipy"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ],
)