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
from google.cloud.workstations_v1beta import gapic_version as package_version

__version__ = package_version.__version__


from .services.workstations import WorkstationsAsyncClient, WorkstationsClient
from .types.workstations import (
    CreateWorkstationClusterRequest,
    CreateWorkstationConfigRequest,
    CreateWorkstationRequest,
    DeleteWorkstationClusterRequest,
    DeleteWorkstationConfigRequest,
    DeleteWorkstationRequest,
    GenerateAccessTokenRequest,
    GenerateAccessTokenResponse,
    GetWorkstationClusterRequest,
    GetWorkstationConfigRequest,
    GetWorkstationRequest,
    ListUsableWorkstationConfigsRequest,
    ListUsableWorkstationConfigsResponse,
    ListUsableWorkstationsRequest,
    ListUsableWorkstationsResponse,
    ListWorkstationClustersRequest,
    ListWorkstationClustersResponse,
    ListWorkstationConfigsRequest,
    ListWorkstationConfigsResponse,
    ListWorkstationsRequest,
    ListWorkstationsResponse,
    OperationMetadata,
    StartWorkstationRequest,
    StopWorkstationRequest,
    UpdateWorkstationClusterRequest,
    UpdateWorkstationConfigRequest,
    UpdateWorkstationRequest,
    Workstation,
    WorkstationCluster,
    WorkstationConfig,
)

__all__ = (
    "WorkstationsAsyncClient",
    "CreateWorkstationClusterRequest",
    "CreateWorkstationConfigRequest",
    "CreateWorkstationRequest",
    "DeleteWorkstationClusterRequest",
    "DeleteWorkstationConfigRequest",
    "DeleteWorkstationRequest",
    "GenerateAccessTokenRequest",
    "GenerateAccessTokenResponse",
    "GetWorkstationClusterRequest",
    "GetWorkstationConfigRequest",
    "GetWorkstationRequest",
    "ListUsableWorkstationConfigsRequest",
    "ListUsableWorkstationConfigsResponse",
    "ListUsableWorkstationsRequest",
    "ListUsableWorkstationsResponse",
    "ListWorkstationClustersRequest",
    "ListWorkstationClustersResponse",
    "ListWorkstationConfigsRequest",
    "ListWorkstationConfigsResponse",
    "ListWorkstationsRequest",
    "ListWorkstationsResponse",
    "OperationMetadata",
    "StartWorkstationRequest",
    "StopWorkstationRequest",
    "UpdateWorkstationClusterRequest",
    "UpdateWorkstationConfigRequest",
    "UpdateWorkstationRequest",
    "Workstation",
    "WorkstationCluster",
    "WorkstationConfig",
    "WorkstationsClient",
)
