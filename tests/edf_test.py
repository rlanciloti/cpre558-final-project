"""
File: edf_test.py

This file will hold unit test to ensure that the user-implemented EDF scheduler matches the
framework-provided EDF scheduler implementation. While not neccessary, if we know that the
EDF scheduler works, then we have a solid example for the myopic scheduler.

Creation Date: 11/28/21
Last Modified: 11/28/21
Version 1.0
"""

import pytest
from src.SimBuilder import SimBuilder

FPATH_PREFIX = "tests"


@pytest.fixture
def create_user_edf() -> SimBuilder:
	"""
	Function: create_user_edf

	This function will create a new instance of SimBuilder with our implementation of EDF for
	a single core CPU as the scheduler.

	:return: Instance of SimBuilder with EDF_mono as the scheduler
	:rtype: SimBuilder
	"""
	return SimBuilder(f"{FPATH_PREFIX}\\user_edf_test.xml")


@pytest.fixture
def create_provided_edf() -> SimBuilder:
	"""
	Function: create_provided_edf

	This function will create a new instance of SimBuilder with the provided implementation of
	EDF for a single core CPU as the scheduler. This will act as a control.

	:return: Instance of SimBuilder with provided EDF_mono as the scheduler
	:rtype: SimBuilder
	"""
	return SimBuilder(f"{FPATH_PREFIX}\\provided_edf_test.xml")


def test_edf_equivalence(create_provided_edf: SimBuilder, create_user_edf: SimBuilder) -> None:
	"""
	Function: test_equivalence

	This function will test the models using the provided EDF schedule and the user created EDF
	schedule and verify that the output are the same.

	:param create_provided_edf: SimSo EDF implementation
	:type create_provided_edf: SimBuilder
	:param create_user_edf: User create EDF implementation
	:type create_user_edf: SimBuilder
	"""
	pmodel = create_provided_edf.model
	umodel = create_user_edf.model

	pmodel.run_model()
	umodel.run_model()

	assert len(pmodel.logs) == len(umodel.logs)

	assert pmodel.logs == umodel.logs


def false() -> None:
	""" Adding pytest to workflow, this makes sure it fails """
	assert False
