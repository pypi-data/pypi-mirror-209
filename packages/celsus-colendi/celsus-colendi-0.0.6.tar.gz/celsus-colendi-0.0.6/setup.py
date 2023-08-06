from setuptools import setup, find_packages

VERSION = '0.0.6' 
DESCRIPTION = 'Colendi data team package'
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="celsus-colendi", 
        version=VERSION,
        author="Caner Taş",
        author_email="<caner.tas@colendi.com>",
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        url='http://gitlab.colendi.com/data-team/data_package.git',
        install_requires=["Werkzeug","setuptools","pandas","datetime"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)