#!/usr/bin/env python3
"""This module contain """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return the element length"""
    return [(i, len(i)) for i in lst]
