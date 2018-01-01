# Python Spine Mini Services Library

A Python package for interacting with NHS Digital Spine Mini Services

https://nhsconnect.github.io/spine-smsp/

Currently this package just contains a set of models for building the ITK payloads.

Functions to wrap that payload in an ITK envelope and send it somewhere are not yet available

## Installing

If all you want to do is use the libray then all you need is:

   python setup.py install

If you wish to use the build script which will download the requirements pack and build the models you'll also need:

   pip install -r requirements.txt

## Usage of the smsp module

   The sub module smsp.requests contains a function to build a request payload for each of the smsp functions.
   
## Usage of the build script

The package includes a Bash script called build_structures.sh. This script downloads the requirements pack
and uses the excellent generateDS package to build data models from the xds files.

The file cleanup.py merges the various models built for each services into the smsp module.

### Prerequisites

The build scripts requires wget

## Running the tests

Run the test using pytest

## Limitations
*  the "local identifier" paramater is not currently supported

## TODO
* Better tests - tests currently just build requests. They don't get validated.
* Functions to wrap the payload in an ITK envelope
* Functions to actually call the smsp - including auth etc etc.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

* The folk at NHS Digital for their work in the Spine Mini Service Provider and OpenTest
* Dave Kuhlman for https://pypi.python.org/pypi/generateDS
