from importlib import import_module

from naya import *
from naya.modules import loadModule


async def loadprem():
    modules = loadModule()
    for mod in modules:
        imported_module = import_module(f"naya.modules.{mod}")
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                CMD_HELP[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module
