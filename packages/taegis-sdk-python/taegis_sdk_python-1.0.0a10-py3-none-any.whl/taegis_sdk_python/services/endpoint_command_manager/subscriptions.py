"""EndpointCommandManager Subscription."""
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


class TaegisSDKEndpointCommandManagerSubscription:
    """Teagis Endpoint_command_manager Subscription operations."""

    def __init__(self, service: EndpointCommandManagerService):
        self.service = service
