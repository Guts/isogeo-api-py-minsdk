﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module is an abstraction calls about the Isogeo REST API.
    https://www.isogeo.com/
"""

from .isogeo_sdk import Isogeo, version
from .isogeo_sdk_oauth import IsogeoSession
from .checker import IsogeoChecker
# from .models import *
from isogeo_pysdk.models.contact import Contact
from .translator import IsogeoTranslator
from .utils import IsogeoUtils

__version__ = version
VERSION = __version__
