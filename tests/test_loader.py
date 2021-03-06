# -*- coding: utf-8 -*-

# TODO: Tests for new file loader method in core/controllers/project_controller::FileLoader
from pathlib import Path

import pytest
from PyQt5.QtTest import QSignalSpy
from pandas import DataFrame


from dgp.core.file_loader import FileLoader

TEST_FILE_GRAV = 'tests/sample_gravity.csv'


def mock_loader(*args, **kwargs):
    # return args, kwargs
    return DataFrame()


def mock_failing_loader(*args, **kwargs):
    raise FileNotFoundError


def test_load_mock(qt_app):
    loader = FileLoader(Path(TEST_FILE_GRAV), mock_loader, qt_app)
    spy_complete = QSignalSpy(loader.loaded)
    spy_error = QSignalSpy(loader.error)

    assert 0 == len(spy_complete)
    assert 0 == len(spy_error)
    assert not loader.isRunning()

    loader.run()

    assert 1 == len(spy_complete)
    assert 0 == len(spy_error)


def test_load_failure(qt_app):
    called = False

    def _error_handler(exception: Exception):
        assert isinstance(exception, Exception)
        nonlocal called
        called = True

    loader = FileLoader(Path(), mock_failing_loader, qt_app)
    loader.error.connect(_error_handler)
    spy_err = QSignalSpy(loader.error)
    assert 0 == len(spy_err)

    loader.run()
    assert 1 == len(spy_err)
    assert called
