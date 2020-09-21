import setuptools

setuptools.setup(
    name                            = "timtaylor",
    packages                        = setuptools.find_packages(where = "python"),
    install_requires                = [ 'tequila @ git+https://github.com/aspuru-guzik-group/tequila.git@master-setup-fix#egg=tequila',
        'z-quantum-core',
        'qe-openfermion', # needed for qe-psi4
        'qe-psi4'],
    package_dir                     = {
        "" : "python"
    },
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
