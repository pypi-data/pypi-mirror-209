from setuptools import setup, find_packages

VERSION = "0.0.1"
NAME = "ml_hyperparameters"
DESCRIPTION = "A basic library to help find the best hyperparameters in sklearn"
LONG_DESCRIPTION = "A library that uses magic to find the best hyperparameters in a modular way"

setup(
    name=NAME,
    version=VERSION,
    author="Tom Neumann",
    author_email="tomn505@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "numpy",
        "progressbar",
        "scikit-learn"
    ],

    keywords=['python', 'sklearn', 'hyperparameter finder'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ]
)
