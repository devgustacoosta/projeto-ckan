"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.almavivasolutions.logic import validators


def test_almavivasolutions_reauired_with_valid_value():
    assert validators.almavivasolutions_required("value") == "value"


def test_almavivasolutions_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.almavivasolutions_required(None)
