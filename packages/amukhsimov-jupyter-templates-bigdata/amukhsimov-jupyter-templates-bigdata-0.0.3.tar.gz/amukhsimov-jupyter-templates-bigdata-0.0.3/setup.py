from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'amukhsimov-jupyter-templates-bigdata'
LONG_DESCRIPTION = 'No description'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="amukhsimov-jupyter-templates-bigdata",
    version=VERSION,
    author="Akmal Mukhsimov",
    author_email="a.mukhsimov@hamkorlab.club",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['python-dotenv', 'pyspark', 'cx-Oracle',
                      'cryptography', 'psycopg2'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["amukhsimov_jupyter_templates_bigdata"],
    package_dir={'': 'src/amukhsimov_jupyter_templates_bigdata'},
    python_requires=">=3.6"
)