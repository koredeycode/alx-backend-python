#!/usr/bin/env python3
"""This module contain the safe first element function"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """safe_first_element function"""
    if lst:
        return lst[0]
    else:
        return None
