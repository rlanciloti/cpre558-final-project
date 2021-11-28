# cpre558-final-project
[![Linting](https://github.com/rlanciloti/cpre558-final-project/actions/workflows/main.yml/badge.svg)](https://github.com/rlanciloti/cpre558-final-project/actions/workflows/main.yml)

## Overview

This repository will eventually hold the source code for a myopic scheduler implementation using the SimSo framework. At this point (11/27/21), it's the code for a user implemented EDF scheduler on a single core processor. 

## Setup Conda Environment

Provided in this repo is a conda-environment.yml file. This can be used to spin up a conda environment that has all of the neccessary dependencies to run the project. If conda is installed, simply run `conda env create -f conda-environment.yml` and it will create the environment. Next, run `conda activate cpre558-final-proj` and this will set conda to use the newly created virtual environment. To leave this virtual environment. run `conda deactivate`. As long as the virtual enviornment hasn't been removed and installed successfully, it can be used by running the `conda activate cpre558-final-proj` command when it's not active. To delete this enviroment, run `conda remove --name cpre558-final-proj --all`.

Conversly, if conda is not installed, run `pip install requirements.txt` to install necessary python packages.

## Flake8

Flake8 is setup to run on push to any repo and on pull-request to master. This is not optional and without passing flake8 checks, no PR will make it into master. Currently there are a handful of configuration modification, these can be changed later if need be. The list of disabled rules and modified configs are below:

- `max-line-length`: This was changed to 96 because 79 feels too restrictive.
- `W191`: Allows the use of tabs. This can be disabled later if the developers decide to go with spaces.
- `E251`: Allows for multi-line parameters to be passed into functions. Nicer formatting.
- `ANN101`: Allows for `self` argument to exclude typing
- `D400`: Allows first line of docstring to not end with a period
- `D202`: Allows for blank line to exist after docstring
- `D401`: Allows the first line to not be in the imperative mood
- `SC200`: Won't do spell check on code

***I HIGHLY recommend integrating Flake8 with your text editor of choice. It's very easy to set up with VSCode. I will not provide a walkthough with setting up flake8 with VSCode, I'll leave that as an exercise to the reader***

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
