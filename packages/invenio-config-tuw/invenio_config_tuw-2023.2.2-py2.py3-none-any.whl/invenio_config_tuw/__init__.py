# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2023 TU Wien.
#
# Invenio Config TUW is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module containing some customizations and configuration for TU Wien."""

from .ext import InvenioConfigTUW

__version__ = "2023.2.2"

__all__ = ("__version__", "InvenioConfigTUW")
