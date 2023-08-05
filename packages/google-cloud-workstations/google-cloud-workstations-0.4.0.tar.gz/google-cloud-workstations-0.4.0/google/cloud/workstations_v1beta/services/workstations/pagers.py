# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
)

from google.cloud.workstations_v1beta.types import workstations


class ListWorkstationClustersPager:
    """A pager for iterating through ``list_workstation_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.workstations_v1beta.types.ListWorkstationClustersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``workstation_clusters`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListWorkstationClusters`` requests and continue to iterate
    through the ``workstation_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.workstations_v1beta.types.ListWorkstationClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., workstations.ListWorkstationClustersResponse],
        request: workstations.ListWorkstationClustersRequest,
        response: workstations.ListWorkstationClustersResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.workstations_v1beta.types.ListWorkstationClustersRequest):
                The initial request object.
            response (google.cloud.workstations_v1beta.types.ListWorkstationClustersResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = workstations.ListWorkstationClustersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[workstations.ListWorkstationClustersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[workstations.WorkstationCluster]:
        for page in self.pages:
            yield from page.workstation_clusters

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkstationClustersAsyncPager:
    """A pager for iterating through ``list_workstation_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.workstations_v1beta.types.ListWorkstationClustersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workstation_clusters`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListWorkstationClusters`` requests and continue to iterate
    through the ``workstation_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.workstations_v1beta.types.ListWorkstationClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[workstations.ListWorkstationClustersResponse]],
        request: workstations.ListWorkstationClustersRequest,
        response: workstations.ListWorkstationClustersResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.workstations_v1beta.types.ListWorkstationClustersRequest):
                The initial request object.
            response (google.cloud.workstations_v1beta.types.ListWorkstationClustersResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = workstations.ListWorkstationClustersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[workstations.ListWorkstationClustersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[workstations.WorkstationCluster]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workstation_clusters:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkstationConfigsPager:
    """A pager for iterating through ``list_workstation_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.workstations_v1beta.types.ListWorkstationConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``workstation_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListWorkstationConfigs`` requests and continue to iterate
    through the ``workstation_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.workstations_v1beta.types.ListWorkstationConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., workstations.ListWorkstationConfigsResponse],
        request: workstations.ListWorkstationConfigsRequest,
        response: workstations.ListWorkstationConfigsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.workstations_v1beta.types.ListWorkstationConfigsRequest):
                The initial request object.
            response (google.cloud.workstations_v1beta.types.ListWorkstationConfigsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = workstations.ListWorkstationConfigsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[workstations.ListWorkstationConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[workstations.WorkstationConfig]:
        for page in self.pages:
            yield from page.workstation_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkstationConfigsAsyncPager:
    """A pager for iterating through ``list_workstation_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.workstations_v1beta.types.ListWorkstationConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workstation_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListWorkstationConfigs`` requests and continue to iterate
    through the ``workstation_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.workstations_v1beta.types.ListWorkstationConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[workstations.ListWorkstationConfigsResponse]],
        request: workstations.ListWorkstationConfigsRequest,
        response: workstations.ListWorkstationConfigsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.workstations_v1beta.types.ListWorkstationConfigsRequest):
                The initial request object.
            response (google.cloud.workstations_v1beta.types.ListWorkstationConfigsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = workstations.ListWorkstationConfigsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[workstations.ListWorkstationConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[workstations.WorkstationConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workstation_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUsableWorkstationConfigsPager:
    """A pager for iterating through ``list_usable_workstation_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.workstations_v1beta.types.ListUsableWorkstationConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``workstation_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUsableWorkstationConfigs`` requests and continue to iterate
    through the ``workstation_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.workstations_v1beta.types.ListUsableWorkstationConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., workstations.ListUsableWorkstationConfigsResponse],
        request: workstations.ListUsableWorkstationConfigsRequest,
        response: workstations.ListUsableWorkstationConfigsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.workstations_v1beta.types.ListUsableWorkstationConfigsRequest):
                The initial request object.
            response (google.cloud.workstations_v1beta.types.ListUsableWorkstationConfigsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = workstations.ListUsableWorkstationConfigsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[workstations.ListUsableWorkstationConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[workstations.WorkstationConfig]:
        for page in self.pages:
            yield from page.workstation_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUsableWorkstationConfigsAsyncPager:
    """A pager for iterating through ``list_usable_workstation_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.workstations_v1beta.types.ListUsableWorkstationConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workstation_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUsableWorkstationConfigs`` requests and continue to iterate
    through the ``workstation_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.workstations_v1beta.types.ListUsableWorkstationConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[workstations.ListUsableWorkstationConfigsResponse]
        ],
        request: workstations.ListUsableWorkstationConfigsRequest,
        response: workstations.ListUsableWorkstationConfigsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.workstations_v1beta.types.ListUsableWorkstationConfigsRequest):
                The initial request object.
            response (google.cloud.workstations_v1beta.types.ListUsableWorkstationConfigsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = workstations.ListUsableWorkstationConfigsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[workstations.ListUsableWorkstationConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[workstations.WorkstationConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workstation_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkstationsPager:
    """A pager for iterating through ``list_workstations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.workstations_v1beta.types.ListWorkstationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``workstations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListWorkstations`` requests and continue to iterate
    through the ``workstations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.workstations_v1beta.types.ListWorkstationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., workstations.ListWorkstationsResponse],
        request: workstations.ListWorkstationsRequest,
        response: workstations.ListWorkstationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.workstations_v1beta.types.ListWorkstationsRequest):
                The initial request object.
            response (google.cloud.workstations_v1beta.types.ListWorkstationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = workstations.ListWorkstationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[workstations.ListWorkstationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[workstations.Workstation]:
        for page in self.pages:
            yield from page.workstations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkstationsAsyncPager:
    """A pager for iterating through ``list_workstations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.workstations_v1beta.types.ListWorkstationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workstations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListWorkstations`` requests and continue to iterate
    through the ``workstations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.workstations_v1beta.types.ListWorkstationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[workstations.ListWorkstationsResponse]],
        request: workstations.ListWorkstationsRequest,
        response: workstations.ListWorkstationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.workstations_v1beta.types.ListWorkstationsRequest):
                The initial request object.
            response (google.cloud.workstations_v1beta.types.ListWorkstationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = workstations.ListWorkstationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[workstations.ListWorkstationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[workstations.Workstation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workstations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUsableWorkstationsPager:
    """A pager for iterating through ``list_usable_workstations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.workstations_v1beta.types.ListUsableWorkstationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``workstations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUsableWorkstations`` requests and continue to iterate
    through the ``workstations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.workstations_v1beta.types.ListUsableWorkstationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., workstations.ListUsableWorkstationsResponse],
        request: workstations.ListUsableWorkstationsRequest,
        response: workstations.ListUsableWorkstationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.workstations_v1beta.types.ListUsableWorkstationsRequest):
                The initial request object.
            response (google.cloud.workstations_v1beta.types.ListUsableWorkstationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = workstations.ListUsableWorkstationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[workstations.ListUsableWorkstationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[workstations.Workstation]:
        for page in self.pages:
            yield from page.workstations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUsableWorkstationsAsyncPager:
    """A pager for iterating through ``list_usable_workstations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.workstations_v1beta.types.ListUsableWorkstationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workstations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUsableWorkstations`` requests and continue to iterate
    through the ``workstations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.workstations_v1beta.types.ListUsableWorkstationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[workstations.ListUsableWorkstationsResponse]],
        request: workstations.ListUsableWorkstationsRequest,
        response: workstations.ListUsableWorkstationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.workstations_v1beta.types.ListUsableWorkstationsRequest):
                The initial request object.
            response (google.cloud.workstations_v1beta.types.ListUsableWorkstationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = workstations.ListUsableWorkstationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[workstations.ListUsableWorkstationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[workstations.Workstation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workstations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
