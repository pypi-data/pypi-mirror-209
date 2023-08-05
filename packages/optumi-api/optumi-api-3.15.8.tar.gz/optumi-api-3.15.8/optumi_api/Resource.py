##
## Copyright (C) Optumi Inc - All rights reserved.
##
## You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
## To receive a copy of the licensing terms please write to contact@optumi.com or visit us at https://www.optumi.com.
##

from .Server import Server
from .Provider import Provider
from .Providers import Providers

from typing import Union, List

from optumi_core.exceptions import (
    OptumiException,
)


class Resource:
    """A class for creating resource specifications to be used when running scripts, notebooks or containers."""

    def __init__(self, providers: Union[List[str], List[Provider]] = [], gpu: Union[bool, str] = True, memory_per_gpu: int = 0, num_gpus: int = 0):
        """Constructor for the Resource class.

        Args:
            providers (list of str or list of Provider): The providers that can be used. Defaults to [], which means any provider can be used.
            gpu (bool or str): The type of graphics card to be used, either True to allow any graphics card, or a specific string value representing one of the types in gpus(). Default is True.
            memory_per_gpu (int): Memory allocated per graphics card. Default is 0.
            num_gpus (int): The number of gpu cards. Defaults 1 gpu is specified, otherwise 0.

        Raises:
            OptumiException: Raised if an unsupported GPU card is specified.
        """
        if type(gpu) is str and not gpu.lower() in [x.lower() for x in Server.gpus()]:
            gpus = Server.gpus()
            if len(gpus) == 0:
                if len([p for p in Providers.list() if p.is_activated()]) == 0:
                    raise OptumiException("No activated providers. Contact Optumi for more information.")
                if len(Server.inventory()) == 0:
                    raise OptumiException("Machine inventory is empty. Contact Optumi for more information.")
                raise OptumiException("No GPU machines in inventory.")
            raise OptumiException("Unexpected GPU type '" + gpu + "', expected one of " + str(gpus))

        self._providers = []
        for provider in providers:
            if type(provider) is Provider:
                self._providers.append(provider)
            else:
                self._providers.append(Provider(provider))

        self._gpu = gpu
        self._memory_per_gpu = memory_per_gpu
        self._num_gpus = 1 if num_gpus == 0 and gpu else num_gpus

    @property
    def providers(self):
        """Obtain the list of the providers that can be used.

        Returns:
            list of Provider: The list of providers that can be used. Defaults to [], which means any provider.
        """
        return self._providers

    @property
    def gpu(self):
        """Obtain the type of graphics card to be used, either True for any, or a specific string value representing one of the types in gpus()

        Returns:
            bool or str: The type of graphics card to be used, either True for any graphics card, or a specific string value representing one of the types in gpus()
        """
        return self._gpu

    @property
    def memory_per_gpu(self):
        """Obtain the memory required per graphics card.

        Returns:
            int: The memory required per graphics card, specified in GB.
        """
        return self._memory_per_gpu

    @property
    def num_gpus(self):
        """Obtain the number of gpu cards.

        Returns:
            int: The number of gpu cards.
        """
        return self._num_gpus

    def __str__(self):
        return "gpu=" + str(self.gpu)
