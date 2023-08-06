"""
fill in
"""

import abc
from dataclasses import dataclass


class restConfig(abc.ABC):
    """
    fill in

    """

    url = "dev"


@dataclass
class MachineRestConfiguration(restConfig):
    """
    fill in
    """

    url = "dev"


class SalesRestConfiguration(restConfig):
    """
    fill in
    """

    url = "dev"


class BronzeSapBsegRestConfiguration(restConfig):
    """
    fill in
    """

    url = "dev"


Apis = [
    MachineRestConfiguration,
    BronzeSapBsegRestConfiguration,
    SalesRestConfiguration,
]
