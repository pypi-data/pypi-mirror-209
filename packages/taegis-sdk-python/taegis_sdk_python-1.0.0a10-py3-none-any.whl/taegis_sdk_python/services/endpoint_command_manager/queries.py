"""EndpointCommandManager Query."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Dict, Optional, Tuple, Union

from taegis_sdk_python.utils import (
    build_output_string,
    prepare_input,
    parse_union_result,
)
from taegis_sdk_python.services.endpoint_command_manager.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.endpoint_command_manager import (
        EndpointCommandManagerService,
    )


class TaegisSDKEndpointCommandManagerQuery:
    """Teagis Endpoint_command_manager Query operations."""

    def __init__(self, service: EndpointCommandManagerService):
        self.service = service

    def endpoint_uninstall_status(self, arguments: UninstallStateArguments) -> bool:
        """Retrieve the endpoint uninstall status."""
        endpoint = "endpointUninstallStatus"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query endpointUninstallStatus")

    def endpoint_command_history(
        self, arguments: CommandHistoryArguments
    ) -> List[HistoryEntry]:
        """Retrieve endpoint command histories."""
        endpoint = "endpointCommandHistory"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(HistoryEntry),
        )
        if result.get(endpoint) is not None:
            return HistoryEntry.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query endpointCommandHistory")

    def endpoint_command_history_paged(
        self, arguments: CommandHistoryPagedArguments
    ) -> HistoryPagedOutput:
        """Retrieve paged endpoint command histories."""
        endpoint = "endpointCommandHistoryPaged"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(HistoryPagedOutput),
        )
        if result.get(endpoint) is not None:
            return HistoryPagedOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query endpointCommandHistoryPaged")

    def endpoint_isolation_exclusion_rules(self) -> List[IsolationExclusionRule]:
        """Retrieve all isolation exclusion rules."""
        endpoint = "endpointIsolationExclusionRules"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(IsolationExclusionRule),
        )
        if result.get(endpoint) is not None:
            return IsolationExclusionRule.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query endpointIsolationExclusionRules")
