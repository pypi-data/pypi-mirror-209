# Claudia
Claudia is a helper utility that allows users to run automated XRPL tests on different networks. It also allows building rippled and launching local running networks.

---

## General prerequisites
Please have the following installed on your machine before proceeding further:
- [Python3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
-  Following is only required if you intend to run Javascript tests.
   - [node](https://nodejs.org/en/download)
   - [npm](https://www.npmjs.com/package/download)

---

## Installation

Install claudia from [PyPi](https://test.pypi.org/project/claudia/), using the following command:

        pip install -i https://test.pypi.org/simple/ claudia

---

## Build Rippled
    More information coming soon...
---

## Launch Local Network
    More information coming soon...
---

## Run tests
This section contains instructions for running the tests. Please follow the instructions mentioned below:

 - [Install claudia](#installation)
 - From your terminal, run: `claudia`
   - Use `--help` option with the CLI to view supported options.
   - Example Usage:
     - `claudia build`: Builds rippled locally.
     - `claudia network`: Launches local network using Rippled. Needs access to built rippled.
     - `claudia run python`: Runs Python tests on local network. Use `--help` to view other supported options. 
     - `claudia run javascript`: Runs Javascript tests on local network. Use `--help` to view other supported options. 
