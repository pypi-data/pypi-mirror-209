"""Comments Mutation."""
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
from taegis_sdk_python.services.comments.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.comments import CommentsService


class TaegisSDKCommentsMutation:
    """Teagis Comments Mutation operations."""

    def __init__(self, service: CommentsService):
        self.service = service

    def mark_comment_read(self, comment_id: str) -> Comment:
        """None."""
        endpoint = "markCommentRead"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "comment_id": prepare_input(comment_id),
            },
            output=build_output_string(Comment),
        )
        if result.get(endpoint) is not None:
            return Comment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation markCommentRead")

    def mark_parent_comments_read(self, parents: List[Parent]) -> List[Comment]:
        """None."""
        endpoint = "markParentCommentsRead"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "parents": prepare_input(parents),
            },
            output=build_output_string(Comment),
        )
        if result.get(endpoint) is not None:
            return Comment.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation markParentCommentsRead")

    def create_comment(self, comment: CommentInput) -> Comment:
        """None."""
        endpoint = "createComment"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "comment": prepare_input(comment),
            },
            output=build_output_string(Comment),
        )
        if result.get(endpoint) is not None:
            return Comment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createComment")

    def update_comment(self, comment_id: str, comment: CommentUpdate) -> Comment:
        """None."""
        endpoint = "updateComment"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "comment_id": prepare_input(comment_id),
                "comment": prepare_input(comment),
            },
            output=build_output_string(Comment),
        )
        if result.get(endpoint) is not None:
            return Comment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateComment")

    def delete_comment(self, comment_id: str) -> Comment:
        """None."""
        endpoint = "deleteComment"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "comment_id": prepare_input(comment_id),
            },
            output=build_output_string(Comment),
        )
        if result.get(endpoint) is not None:
            return Comment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteComment")

    def bulk_restore_comments(self, ids: List[str]) -> List[str]:
        """None."""
        endpoint = "bulkRestoreComments"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation bulkRestoreComments")
