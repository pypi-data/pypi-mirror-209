from orwynn._di.Provider import Provider
from orwynn.base.config import Config
from orwynn.base.service import FrameworkService, Service

"""List of builtin classes in Provider category.

Providers with higher priority cannot inject ones with lower priority.

This list: Lower index => higher priority.
"""
BUILTIN_PROVIDERS: list[type[Provider]] = [
    Config,
    FrameworkService,
    Service
]
