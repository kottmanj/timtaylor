import setuptools

setuptools.setup(
    name                            = "timtaylor",
    packages                        = setuptools.find_packages(where = "python"),
    install_requires                = [ 'tequila @ git+https://github.com/aspuru-guzik-group/tequila.git@master-setup-fix#egg=tequila'],
    package_dir                     = {
        "" : "python"
    },
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
