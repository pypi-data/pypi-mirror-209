"""
Flask-Tenable is a thin wrapper for pyTenable that enables the easy integration of pyTenable into flask applications.

To use the wrapped pyTenable objects app.config must contain:
    - TenableAD: TENABLE_AD_API_KEY
    - Downloads: TENABLE_DOWNLOADS_API_TOKEN
    - TenableIO: TENABLE_IO_ACCESS_KEY, TENABLE_IO_SECRET_KEY
    - Nessus: TENABLE_NESSUS_HOST, TENABLE_NESSUS_ACCESS_KEY, TENABLE_NESSUS_SECRET_KEY
    - TenableOT: TENABLE_OT_API_KEY
    - TenableSC: TENABLE_SC_HOST, TENABLE_SC_ACCESS_KEY, TENABLE_SC_SECRET_KEY
"""

from .ad import TenableAD
from .dl import Downloads
from .io import TenableIO
from .nessus import Nessus
from .ot import TenableOT
from .sc import TenableSC

__all__ = [
    'Downloads',
    'Nessus',
    'TenableAD',
    'TenableIO',
    'TenableOT',
    'TenableSC',
]
