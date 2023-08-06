Flask-Tenable
=============

[![PyPI version](https://badge.fury.io/py/Flask-Tenable.svg)](https://pypi.org/project/Flask-Tenable)
[![Python version](https://img.shields.io/badge/Python-3.7_%7C_3.8_%7C_3.9_%7C_3.10_%7C_3.11-blue)]()

---

Flask-Tenable is a thin wrapper for [pyTenable](https://pypi.org/project/pyTenable/)
that enables the easy integration of [pyTenable](https://pypi.org/project/pyTenable/)
into [flask](https://pypi.org/project/flask/) applications.

To use the wrapped [pyTenable objects](https://pytenable.readthedocs.io/en/stable/)
app.config must contain the following configs:

| Product   | Required configs                                                          |
|-----------|---------------------------------------------------------------------------|
| Downloads | TENABLE_DOWNLOADS_API_TOKEN                                               |
| Nessus    | TENABLE_NESSUS_HOST, TENABLE_NESSUS_ACCESS_KEY, TENABLE_NESSUS_SECRET_KEY |
| TenableAD | TENABLE_AD_API_KEY                                                        |
| TenableIO | TENABLE_IO_ACCESS_KEY, TENABLE_IO_SECRET_KEY                              |
| TenableOT | TENABLE_OT_API_KEY                                                        |
| TenableSC | TENABLE_SC_HOST, TENABLE_SC_ACCESS_KEY, TENABLE_SC_SECRET_KEY             |
