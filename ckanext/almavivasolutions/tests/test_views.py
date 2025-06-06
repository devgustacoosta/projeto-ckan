"""Tests for views.py."""

import pytest

import ckanext.almavivasolutions.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "almavivasolutions")
@pytest.mark.usefixtures("with_plugins")
def test_almavivasolutions_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("almavivasolutions.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, almavivasolutions!"
