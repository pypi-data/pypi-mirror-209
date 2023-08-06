from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'bigdata-jupyter-templates'
LONG_DESCRIPTION = 'No description'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="bigdata-jupyter-templates",
    version=VERSION,
    author="Akmal Mukhsimov",
    author_email="a.mukhsimov@hamkorlab.club",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['python-dotenv', 'pyspark', 'cx-Oracle',
                      'cryptography', 'psycopg2'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'jupyter']
)