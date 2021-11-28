# cpre558-final-project

## Overview

This repository will eventually hold the source code for a myopic scheduler implementation using the SimSo framework. At this point (11/27/21), it's the code for a user implemented EDF scheduler on a single core processor. 

## Setup Conda Environment

Provided in this repo is a conda-environment.yml file. This can be used to spin up a conda environment that has all of the neccessary dependencies to run the project. If conda is installed, simply run `conda env create -f conda-environment.yml` and it will create the environment. Next, run `conda activate cpre558-final-proj` and this will set conda to use the newly created virtual environment. To leave this virtual environment. run `conda deactivate`. As long as the virtual enviornment hasn't been removed and installed successfully, it can be used by running the `conda activate cpre558-final-proj` command when it's not active. To delete this enviroment, run `conda remove --name cpre558-final-proj --all`.

Conversly, if conda is not installed, running `pip install requirements.txt`.

## Pylint

Pylint is setup to run on push to any repo and on pull-request to master. This is not optional and without passing pylint checks, no PR will make it into master. Currently there are a handful of rules disabled, however this can be changed to either remove or add more. The list of disabled rules are below:

- `W0311`: Allows the use of tab (subject to change if spaces are prefered by both developers)
- `W0211`: Allows class variables to be definied outside of the `__init__` function
- `E0401`: Ignores import errors. Couldn't figure out how to satisfy import paths for both pylint and main.py
- `unspecified-encoding`: Allows the use of `open()` without specifying `UTF-8`
- `invalid-name`: Allows for classes to not follow Pascal casing and python files to not follow camel_casing. Although, please keep it somewhat consistent.

## Running the Myopic Scheduler

To run the myopic scheduler, simply run `main.py` with a config file as an optional command line argument. Examples will be provided below for both windows and unix systems. For both of thsee examples, the commands will be executed from the **project root directory** which is `cpre558-final-project`. **NOTE: Currently main.py does nothing, so provided below is how to use test.py**

- Windows: `src\\test.py graphic_config\\edf_test.xml`
- Unix: `src/test.py graphic_config/edf_test.xml`

If no file is specified, then only the graphical interface will launch. To run a scenario within the graphical interface, open a saved configuration from the `graphic_config` directory.

## How to Create More Scenarios

Creating scenarios **should** be done via the graphical interface for SimSo. Using the gui is self explanitory, however once it's configured to the user's needs, save the config in the `graphic_config` directory. The file will save as an XML file which can be read in via a command line argument.

## Schedulers

At this point, only EDF_mono exists. However this directory will eventually hold a myopic scheduler. For more information on how to builder a scheduler, visit the [Simso Documentation](http://projects.laas.fr/simso/doc/). 

## Utility Files

### SimBuilder

This file contains a class which will build a simulation model from a config XML file. When a user created a scenario via the SimSo GUI and saves the file to the graphic_config directory, that file can be passed in as a constructor argument for SimBuilder and it will create model which **should** run in the command line exactly as it had in the SimSo gui. This allows for futher data analytics of the model/scenario.
