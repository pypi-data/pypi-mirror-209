import inspect

from orwynn._di.collecting.no_dependencies_for_given_provider_error import (
    NoDependenciesForGivenProviderError,
)
from orwynn._di.collecting.provider_dependencies_map import (
    ProviderDependenciesMap,
)
from orwynn._di.DiContainer import DiContainer
from orwynn._di.is_provider import is_provider
from orwynn._di.MissingDiObjectError import MissingDiObjectError
from orwynn._di.Provider import Provider
from orwynn.base.config import Config
from orwynn.base.module.errors import CircularDependencyError
from orwynn.utils.fmt import format_chain


def init_providers(
    provider_dependencies_map: ProviderDependenciesMap
) -> DiContainer:
    """Traverses through given providers and dependencies initializing them.

    Args:
        providers_dependencies_map:
            Map of providers and their dependencies.

    Returns:
        DI container populated with initialized providers by their names.
    """
    # Note for this module that most validation logic has been already
    # performed at previous stages, so no need to do checks here.

    container: DiContainer = DiContainer()

    for P in provider_dependencies_map.Providers:
        try:
            container.find(P.__name__)
        except MissingDiObjectError:
            _traverse(
                StarterProvider=P,
                mp=provider_dependencies_map,
                container=container,
                chain=[]
            )

    container.finalize_provider_populating()

    return container


def _traverse(
    *,
    StarterProvider: type[Provider],
    mp: ProviderDependenciesMap,
    container: DiContainer,
    chain: list[type[Provider]]
) -> Provider:
    already_initialized_dependencies: list[Provider] = []

    if StarterProvider in chain:
        raise CircularDependencyError(
            # Failed provider is added second time to the chain for
            # error descriptiveness
            f"provider {StarterProvider} occured twice in dependency chain"
            f" {format_chain(chain + [StarterProvider])}"
        )

    try:
        Dependencies: list[type[Provider]] = mp.get_dependencies(
            StarterProvider
        )
    except NoDependenciesForGivenProviderError:
        # Final point in chain, since no dependencies we can initialize
        # without any attributes
        pass
    else:
        chain.append(StarterProvider)

        for D in Dependencies:
            try:
                already_initialized_dependencies.append(
                    container.find(D.__name__)
                )
            except MissingDiObjectError:
                already_initialized_dependencies.append(
                    _traverse(
                        StarterProvider=D,
                        mp=mp,
                        container=container,
                        chain=chain
                    )
                )

        # On object initialization it should be removed from chain, but not for
        # Config since it hasn't been appended
        chain.pop()

    # All dependencies for this provider have been initialized - now initialize
    # this provider. Checks on previous phases should have been validated, that
    # is every provider waits only positional arguments.
    result_provider: Provider
    if issubclass(StarterProvider, Config):
        # For configs we need to prepare names kwargs, so we perform
        # signaturing and container searching here once again. It's not good
        # since we've done it before, so consider refactoring.
        provider_kwargs: dict[str, Provider] = {}

        for param in inspect.signature(StarterProvider).parameters.values():
            if (
                inspect.isclass(param.annotation)
                and is_provider(param.annotation)
            ):
                provider_kwargs[param.name] = container.find(
                    param.annotation.__name__
                )

        result_provider = StarterProvider.load(extra=provider_kwargs)
    else:
        result_provider = StarterProvider(
            *already_initialized_dependencies
        )

    container.add(result_provider)
    return result_provider
