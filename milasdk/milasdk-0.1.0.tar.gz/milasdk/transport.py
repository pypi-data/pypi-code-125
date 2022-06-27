import io
import json
import logging
from typing import Any, AsyncGenerator, Dict, Optional, Tuple, Type

import aiohttp
from aiohttp.client_exceptions import ClientResponseError
from graphql import DocumentNode, ExecutionResult, print_ast
from multidict import CIMultiDictProxy

from gql.transport import AsyncTransport
from gql.utils import extract_files
from gql.transport.exceptions import (
    TransportClosed,
    TransportProtocolError,
    TransportServerError,
)

from .auth import AbstractAsyncSession

log = logging.getLogger(__name__)

class AuthenticatedAIOHTTPTransport(AsyncTransport):
    """:ref:`Async Transport <async_transports>` to execute GraphQL queries
    on remote servers with an authenticated HTTP connection.

    This transport use the aiohttp library with asyncio.
    """

    file_classes: Tuple[Type[Any], ...] = (
        io.IOBase,
        aiohttp.StreamReader,
        AsyncGenerator,
    )

    def __init__(
        self,
        url: str,
        session: AbstractAsyncSession = None
    ) -> None:
        """Initialize the transport with the given aiohttp parameters.

        :param url: The GraphQL server URL. Example: 'https://server.com:PORT/path'.
        :param session: The authenticated session to utilize

        """
        self.url: str = url
        self.session: AbstractAsyncSession = session
        self.response_headers: Optional[CIMultiDictProxy[str]]

    async def connect(self) -> None:
        """Coroutine which will create an aiohttp ClientSession() as self.session.

        Don't call this coroutine directly on the transport, instead use
        :code:`async with` on the client and this coroutine will be executed
        to create the session.

        Should be cleaned with a call to the close coroutine.
        """
        # session management not performed by this transport

    async def close(self) -> None:
        """Coroutine which will close the aiohttp session.

        Don't call this coroutine directly on the transport, instead use
        :code:`async with` on the client and this coroutine will be executed
        when you exit the async context manager.
        """
        # session management not performed by this transport

    async def execute(
        self,
        document: DocumentNode,
        variable_values: Optional[Dict[str, Any]] = None,
        operation_name: Optional[str] = None,
        extra_args: Dict[str, Any] = None,
        upload_files: bool = False,
    ) -> ExecutionResult:
        """Execute the provided document AST against the configured remote server
        using the current session.
        This uses the aiohttp library to perform a HTTP POST request asynchronously
        to the remote server.

        Don't call this coroutine directly on the transport, instead use
        :code:`execute` on a client or a session.

        :param document: the parsed GraphQL request
        :param variable_values: An optional Dict of variable values
        :param operation_name: An optional Operation name for the request
        :param extra_args: additional arguments to send to the aiohttp post method
        :param upload_files: Set to True if you want to put files in the variable values
        :returns: an ExecutionResult object.
        """

        query_str = print_ast(document)

        payload: Dict[str, Any] = {
            "query": query_str,
        }

        if operation_name:
            payload["operationName"] = operation_name

        if upload_files:

            # If the upload_files flag is set, then we need variable_values
            assert variable_values is not None

            # If we upload files, we will extract the files present in the
            # variable_values dict and replace them by null values
            nulled_variable_values, files = extract_files(
                variables=variable_values,
                file_classes=self.file_classes,
            )

            # Save the nulled variable values in the payload
            payload["variables"] = nulled_variable_values

            # Prepare aiohttp to send multipart-encoded data
            data = aiohttp.FormData()

            # Generate the file map
            # path is nested in a list because the spec allows multiple pointers
            # to the same file. But we don't support that.
            # Will generate something like {"0": ["variables.file"]}
            file_map = {str(i): [path] for i, path in enumerate(files)}

            # Enumerate the file streams
            # Will generate something like {'0': <_io.BufferedReader ...>}
            file_streams = {str(i): files[path] for i, path in enumerate(files)}

            # Add the payload to the operations field
            operations_str = json.dumps(payload)
            log.debug("operations %s", operations_str)
            data.add_field(
                "operations", operations_str, content_type="application/json"
            )

            # Add the file map field
            file_map_str = json.dumps(file_map)
            log.debug("file_map %s", file_map_str)
            data.add_field("map", file_map_str, content_type="application/json")

            # Add the extracted files as remaining fields
            for k, v in file_streams.items():
                data.add_field(k, v, filename=getattr(v, "name", k))

            post_args: Dict[str, Any] = {"data": data}

        else:
            if variable_values:
                payload["variables"] = variable_values

            if log.isEnabledFor(logging.INFO):
                log.info(">>> %s", json.dumps(payload))

            post_args = {"json": payload}

        # Pass post_args to aiohttp post method
        if extra_args:
            post_args.update(extra_args)

        if self.session is None:
            raise TransportClosed("Transport is not connected")

        async with await self.session.post(self.url, **post_args) as resp:

            async def raise_response_error(resp: aiohttp.ClientResponse, reason: str):
                # We raise a TransportServerError if the status code is 400 or higher
                # We raise a TransportProtocolError in the other cases

                try:
                    # Raise a ClientResponseError if response status is 400 or higher
                    resp.raise_for_status()
                except ClientResponseError as e:
                    raise TransportServerError(str(e), e.status) from e

                result_text = await resp.text()
                raise TransportProtocolError(
                    f"Server did not return a GraphQL result: "
                    f"{reason}: "
                    f"{result_text}"
                )

            try:
                result = await resp.json(content_type=None)

                if log.isEnabledFor(logging.INFO):
                    result_text = await resp.text()
                    log.info("<<< %s", result_text)

            except Exception:
                await raise_response_error(resp, "Not a JSON answer")

            if "errors" not in result and "data" not in result:
                await raise_response_error(resp, 'No "data" or "errors" keys in answer')

            # Saving latest response headers in the transport
            self.response_headers = resp.headers

            return ExecutionResult(
                errors=result.get("errors"),
                data=result.get("data"),
                extensions=result.get("extensions"),
            )

    def subscribe(
        self,
        document: DocumentNode,
        variable_values: Optional[Dict[str, Any]] = None,
        operation_name: Optional[str] = None,
    ) -> AsyncGenerator[ExecutionResult, None]:
        """Subscribe is not supported on HTTP.

        :meta private:
        """
        raise NotImplementedError(" The HTTP transport does not support subscriptions")