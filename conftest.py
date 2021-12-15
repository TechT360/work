import pytest

import app as webapp

import DBcm
from appconfig import config


@pytest.fixture
def app():