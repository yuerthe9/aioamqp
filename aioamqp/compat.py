"""
    Compatibility between python or package versions
"""
# pylint: disable=unused-import

import asyncio
import sys

if sys.version_info[:3] > (3, 4, 2):
    from asyncio import ensure_future
else:
    ensure_future = asyncio.async
