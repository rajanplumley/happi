__all__ = ['Device', 'EntryInfo', 'Client', 'from_container',
           'load_devices', 'cache', 'HappiItem']
import logging

from ._version import get_versions
from .client import Client
from .device import Device, EntryInfo, HappiItem
from .loader import cache, from_container, load_devices

__version__ = get_versions()['version']
del get_versions

# Generic Logging Setup
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
