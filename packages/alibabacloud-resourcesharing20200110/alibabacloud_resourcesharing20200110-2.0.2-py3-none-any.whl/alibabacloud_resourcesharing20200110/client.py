# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_resourcesharing20200110 import models as resource_sharing_20200110_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('resourcesharing', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def accept_resource_share_invitation_with_options(
        self,
        request: resource_sharing_20200110_models.AcceptResourceShareInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.AcceptResourceShareInvitationResponse:
        """
        The ID of the resource sharing invitation.
        You can call the [ListResourceShareInvitations](~~450564~~) operation to obtain the ID of a resource sharing invitation.
        
        @param request: AcceptResourceShareInvitationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptResourceShareInvitationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptResourceShareInvitation',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AcceptResourceShareInvitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_resource_share_invitation_with_options_async(
        self,
        request: resource_sharing_20200110_models.AcceptResourceShareInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.AcceptResourceShareInvitationResponse:
        """
        The ID of the resource sharing invitation.
        You can call the [ListResourceShareInvitations](~~450564~~) operation to obtain the ID of a resource sharing invitation.
        
        @param request: AcceptResourceShareInvitationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptResourceShareInvitationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptResourceShareInvitation',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AcceptResourceShareInvitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_resource_share_invitation(
        self,
        request: resource_sharing_20200110_models.AcceptResourceShareInvitationRequest,
    ) -> resource_sharing_20200110_models.AcceptResourceShareInvitationResponse:
        """
        The ID of the resource sharing invitation.
        You can call the [ListResourceShareInvitations](~~450564~~) operation to obtain the ID of a resource sharing invitation.
        
        @param request: AcceptResourceShareInvitationRequest
        @return: AcceptResourceShareInvitationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.accept_resource_share_invitation_with_options(request, runtime)

    async def accept_resource_share_invitation_async(
        self,
        request: resource_sharing_20200110_models.AcceptResourceShareInvitationRequest,
    ) -> resource_sharing_20200110_models.AcceptResourceShareInvitationResponse:
        """
        The ID of the resource sharing invitation.
        You can call the [ListResourceShareInvitations](~~450564~~) operation to obtain the ID of a resource sharing invitation.
        
        @param request: AcceptResourceShareInvitationRequest
        @return: AcceptResourceShareInvitationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.accept_resource_share_invitation_with_options_async(request, runtime)

    def associate_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.AssociateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.AssociateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to AssociateResourceShare.
        
        @param request: AssociateResourceShareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_names):
            query['PermissionNames'] = request.permission_names
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AssociateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.AssociateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.AssociateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to AssociateResourceShare.
        
        @param request: AssociateResourceShareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_names):
            query['PermissionNames'] = request.permission_names
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AssociateResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_resource_share(
        self,
        request: resource_sharing_20200110_models.AssociateResourceShareRequest,
    ) -> resource_sharing_20200110_models.AssociateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to AssociateResourceShare.
        
        @param request: AssociateResourceShareRequest
        @return: AssociateResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_resource_share_with_options(request, runtime)

    async def associate_resource_share_async(
        self,
        request: resource_sharing_20200110_models.AssociateResourceShareRequest,
    ) -> resource_sharing_20200110_models.AssociateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to AssociateResourceShare.
        
        @param request: AssociateResourceShareRequest
        @return: AssociateResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_resource_share_with_options_async(request, runtime)

    def associate_resource_share_permission_with_options(
        self,
        request: resource_sharing_20200110_models.AssociateResourceSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.AssociateResourceSharePermissionResponse:
        """
        The name of the permission.
        
        @param request: AssociateResourceSharePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateResourceSharePermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateResourceSharePermission',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AssociateResourceSharePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_resource_share_permission_with_options_async(
        self,
        request: resource_sharing_20200110_models.AssociateResourceSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.AssociateResourceSharePermissionResponse:
        """
        The name of the permission.
        
        @param request: AssociateResourceSharePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateResourceSharePermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateResourceSharePermission',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AssociateResourceSharePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_resource_share_permission(
        self,
        request: resource_sharing_20200110_models.AssociateResourceSharePermissionRequest,
    ) -> resource_sharing_20200110_models.AssociateResourceSharePermissionResponse:
        """
        The name of the permission.
        
        @param request: AssociateResourceSharePermissionRequest
        @return: AssociateResourceSharePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_resource_share_permission_with_options(request, runtime)

    async def associate_resource_share_permission_async(
        self,
        request: resource_sharing_20200110_models.AssociateResourceSharePermissionRequest,
    ) -> resource_sharing_20200110_models.AssociateResourceSharePermissionResponse:
        """
        The name of the permission.
        
        @param request: AssociateResourceSharePermissionRequest
        @return: AssociateResourceSharePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_resource_share_permission_with_options_async(request, runtime)

    def create_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.CreateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.CreateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to CreateResourceShare.
        
        @param request: CreateResourceShareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not UtilClient.is_unset(request.permission_names):
            query['PermissionNames'] = request.permission_names
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.CreateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.CreateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.CreateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to CreateResourceShare.
        
        @param request: CreateResourceShareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not UtilClient.is_unset(request.permission_names):
            query['PermissionNames'] = request.permission_names
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.CreateResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_share(
        self,
        request: resource_sharing_20200110_models.CreateResourceShareRequest,
    ) -> resource_sharing_20200110_models.CreateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to CreateResourceShare.
        
        @param request: CreateResourceShareRequest
        @return: CreateResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_share_with_options(request, runtime)

    async def create_resource_share_async(
        self,
        request: resource_sharing_20200110_models.CreateResourceShareRequest,
    ) -> resource_sharing_20200110_models.CreateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to CreateResourceShare.
        
        @param request: CreateResourceShareRequest
        @return: CreateResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_share_with_options_async(request, runtime)

    def delete_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.DeleteResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DeleteResourceShareResponse:
        """
        The operation that you want to perform. Set the value to DeleteResourceShare.
        
        @param request: DeleteResourceShareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DeleteResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.DeleteResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DeleteResourceShareResponse:
        """
        The operation that you want to perform. Set the value to DeleteResourceShare.
        
        @param request: DeleteResourceShareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DeleteResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_share(
        self,
        request: resource_sharing_20200110_models.DeleteResourceShareRequest,
    ) -> resource_sharing_20200110_models.DeleteResourceShareResponse:
        """
        The operation that you want to perform. Set the value to DeleteResourceShare.
        
        @param request: DeleteResourceShareRequest
        @return: DeleteResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_share_with_options(request, runtime)

    async def delete_resource_share_async(
        self,
        request: resource_sharing_20200110_models.DeleteResourceShareRequest,
    ) -> resource_sharing_20200110_models.DeleteResourceShareResponse:
        """
        The operation that you want to perform. Set the value to DeleteResourceShare.
        
        @param request: DeleteResourceShareRequest
        @return: DeleteResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_share_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: resource_sharing_20200110_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: resource_sharing_20200110_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: resource_sharing_20200110_models.DescribeRegionsRequest,
    ) -> resource_sharing_20200110_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: resource_sharing_20200110_models.DescribeRegionsRequest,
    ) -> resource_sharing_20200110_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def disassociate_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DisassociateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to DisassociateResourceShare.
        
        @param request: DisassociateResourceShareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisassociateResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DisassociateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DisassociateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to DisassociateResourceShare.
        
        @param request: DisassociateResourceShareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisassociateResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DisassociateResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_resource_share(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceShareRequest,
    ) -> resource_sharing_20200110_models.DisassociateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to DisassociateResourceShare.
        
        @param request: DisassociateResourceShareRequest
        @return: DisassociateResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disassociate_resource_share_with_options(request, runtime)

    async def disassociate_resource_share_async(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceShareRequest,
    ) -> resource_sharing_20200110_models.DisassociateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to DisassociateResourceShare.
        
        @param request: DisassociateResourceShareRequest
        @return: DisassociateResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_resource_share_with_options_async(request, runtime)

    def disassociate_resource_share_permission_with_options(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DisassociateResourceSharePermissionResponse:
        """
        This topic provides an example on how to call the API operation to disassociate the `AliyunRSDefaultPermissionVSwitch` permission from the `rs-6GRmdD3X***` resource share in the `cn-hangzhou` region.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: DisassociateResourceSharePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisassociateResourceSharePermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateResourceSharePermission',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DisassociateResourceSharePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_resource_share_permission_with_options_async(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DisassociateResourceSharePermissionResponse:
        """
        This topic provides an example on how to call the API operation to disassociate the `AliyunRSDefaultPermissionVSwitch` permission from the `rs-6GRmdD3X***` resource share in the `cn-hangzhou` region.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: DisassociateResourceSharePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisassociateResourceSharePermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateResourceSharePermission',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DisassociateResourceSharePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_resource_share_permission(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceSharePermissionRequest,
    ) -> resource_sharing_20200110_models.DisassociateResourceSharePermissionResponse:
        """
        This topic provides an example on how to call the API operation to disassociate the `AliyunRSDefaultPermissionVSwitch` permission from the `rs-6GRmdD3X***` resource share in the `cn-hangzhou` region.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: DisassociateResourceSharePermissionRequest
        @return: DisassociateResourceSharePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disassociate_resource_share_permission_with_options(request, runtime)

    async def disassociate_resource_share_permission_async(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceSharePermissionRequest,
    ) -> resource_sharing_20200110_models.DisassociateResourceSharePermissionResponse:
        """
        This topic provides an example on how to call the API operation to disassociate the `AliyunRSDefaultPermissionVSwitch` permission from the `rs-6GRmdD3X***` resource share in the `cn-hangzhou` region.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: DisassociateResourceSharePermissionRequest
        @return: DisassociateResourceSharePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_resource_share_permission_with_options_async(request, runtime)

    def enable_sharing_with_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse:
        """
        The operation that you want to perform. Set the value to EnableSharingWithResourceDirectory.
        
        @param request: EnableSharingWithResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSharingWithResourceDirectoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableSharingWithResourceDirectory',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_sharing_with_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse:
        """
        The operation that you want to perform. Set the value to EnableSharingWithResourceDirectory.
        
        @param request: EnableSharingWithResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSharingWithResourceDirectoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableSharingWithResourceDirectory',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_sharing_with_resource_directory(self) -> resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse:
        """
        The operation that you want to perform. Set the value to EnableSharingWithResourceDirectory.
        
        @return: EnableSharingWithResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_sharing_with_resource_directory_with_options(runtime)

    async def enable_sharing_with_resource_directory_async(self) -> resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse:
        """
        The operation that you want to perform. Set the value to EnableSharingWithResourceDirectory.
        
        @return: EnableSharingWithResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_sharing_with_resource_directory_with_options_async(runtime)

    def get_permission_with_options(
        self,
        request: resource_sharing_20200110_models.GetPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.GetPermissionResponse:
        """
        The version of the permission.
        
        @param request: GetPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not UtilClient.is_unset(request.permission_version):
            query['PermissionVersion'] = request.permission_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPermission',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.GetPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_permission_with_options_async(
        self,
        request: resource_sharing_20200110_models.GetPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.GetPermissionResponse:
        """
        The version of the permission.
        
        @param request: GetPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not UtilClient.is_unset(request.permission_version):
            query['PermissionVersion'] = request.permission_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPermission',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.GetPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_permission(
        self,
        request: resource_sharing_20200110_models.GetPermissionRequest,
    ) -> resource_sharing_20200110_models.GetPermissionResponse:
        """
        The version of the permission.
        
        @param request: GetPermissionRequest
        @return: GetPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_permission_with_options(request, runtime)

    async def get_permission_async(
        self,
        request: resource_sharing_20200110_models.GetPermissionRequest,
    ) -> resource_sharing_20200110_models.GetPermissionResponse:
        """
        The version of the permission.
        
        @param request: GetPermissionRequest
        @return: GetPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_permission_with_options_async(request, runtime)

    def list_permission_versions_with_options(
        self,
        request: resource_sharing_20200110_models.ListPermissionVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListPermissionVersionsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListPermissionVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPermissionVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPermissionVersions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListPermissionVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permission_versions_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListPermissionVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListPermissionVersionsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListPermissionVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPermissionVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPermissionVersions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListPermissionVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permission_versions(
        self,
        request: resource_sharing_20200110_models.ListPermissionVersionsRequest,
    ) -> resource_sharing_20200110_models.ListPermissionVersionsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListPermissionVersionsRequest
        @return: ListPermissionVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_permission_versions_with_options(request, runtime)

    async def list_permission_versions_async(
        self,
        request: resource_sharing_20200110_models.ListPermissionVersionsRequest,
    ) -> resource_sharing_20200110_models.ListPermissionVersionsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListPermissionVersionsRequest
        @return: ListPermissionVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_permission_versions_with_options_async(request, runtime)

    def list_permissions_with_options(
        self,
        request: resource_sharing_20200110_models.ListPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListPermissionsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListPermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPermissions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permissions_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListPermissionsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListPermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPermissions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permissions(
        self,
        request: resource_sharing_20200110_models.ListPermissionsRequest,
    ) -> resource_sharing_20200110_models.ListPermissionsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListPermissionsRequest
        @return: ListPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_permissions_with_options(request, runtime)

    async def list_permissions_async(
        self,
        request: resource_sharing_20200110_models.ListPermissionsRequest,
    ) -> resource_sharing_20200110_models.ListPermissionsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListPermissionsRequest
        @return: ListPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_permissions_with_options_async(request, runtime)

    def list_resource_share_associations_with_options(
        self,
        request: resource_sharing_20200110_models.ListResourceShareAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceShareAssociationsResponse:
        """
        This topic provides an example on how to call the API operation to query the association records of the resource shares that are created by using the current Alibaba Cloud account in the `cn-hangzhou` region. The response shows the following records:
        *   The resource `vsw-bp1upw03qyz8n7us9****` of the `VSwitch` type has been associated with the resource share `rs-6GRmdD3X****`. The resource is in the `Associated` state. This indicates that the resource is being shared.
        *   The resource `vsw-bp183p93qs667muql****` of the `VSwitch` type has been disassociated from the resource share `rs-6GRmdD3X****`. The resource is in the `Disassociated` state. This indicates that the sharing of the resource is stopped.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: ListResourceShareAssociationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceShareAssociationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.association_status):
            query['AssociationStatus'] = request.association_status
        if not UtilClient.is_unset(request.association_type):
            query['AssociationType'] = request.association_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShareAssociations',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceShareAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_share_associations_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListResourceShareAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceShareAssociationsResponse:
        """
        This topic provides an example on how to call the API operation to query the association records of the resource shares that are created by using the current Alibaba Cloud account in the `cn-hangzhou` region. The response shows the following records:
        *   The resource `vsw-bp1upw03qyz8n7us9****` of the `VSwitch` type has been associated with the resource share `rs-6GRmdD3X****`. The resource is in the `Associated` state. This indicates that the resource is being shared.
        *   The resource `vsw-bp183p93qs667muql****` of the `VSwitch` type has been disassociated from the resource share `rs-6GRmdD3X****`. The resource is in the `Disassociated` state. This indicates that the sharing of the resource is stopped.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: ListResourceShareAssociationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceShareAssociationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.association_status):
            query['AssociationStatus'] = request.association_status
        if not UtilClient.is_unset(request.association_type):
            query['AssociationType'] = request.association_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShareAssociations',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceShareAssociationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_share_associations(
        self,
        request: resource_sharing_20200110_models.ListResourceShareAssociationsRequest,
    ) -> resource_sharing_20200110_models.ListResourceShareAssociationsResponse:
        """
        This topic provides an example on how to call the API operation to query the association records of the resource shares that are created by using the current Alibaba Cloud account in the `cn-hangzhou` region. The response shows the following records:
        *   The resource `vsw-bp1upw03qyz8n7us9****` of the `VSwitch` type has been associated with the resource share `rs-6GRmdD3X****`. The resource is in the `Associated` state. This indicates that the resource is being shared.
        *   The resource `vsw-bp183p93qs667muql****` of the `VSwitch` type has been disassociated from the resource share `rs-6GRmdD3X****`. The resource is in the `Disassociated` state. This indicates that the sharing of the resource is stopped.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: ListResourceShareAssociationsRequest
        @return: ListResourceShareAssociationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_share_associations_with_options(request, runtime)

    async def list_resource_share_associations_async(
        self,
        request: resource_sharing_20200110_models.ListResourceShareAssociationsRequest,
    ) -> resource_sharing_20200110_models.ListResourceShareAssociationsResponse:
        """
        This topic provides an example on how to call the API operation to query the association records of the resource shares that are created by using the current Alibaba Cloud account in the `cn-hangzhou` region. The response shows the following records:
        *   The resource `vsw-bp1upw03qyz8n7us9****` of the `VSwitch` type has been associated with the resource share `rs-6GRmdD3X****`. The resource is in the `Associated` state. This indicates that the resource is being shared.
        *   The resource `vsw-bp183p93qs667muql****` of the `VSwitch` type has been disassociated from the resource share `rs-6GRmdD3X****`. The resource is in the `Disassociated` state. This indicates that the sharing of the resource is stopped.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: ListResourceShareAssociationsRequest
        @return: ListResourceShareAssociationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_share_associations_with_options_async(request, runtime)

    def list_resource_share_invitations_with_options(
        self,
        request: resource_sharing_20200110_models.ListResourceShareInvitationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceShareInvitationsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListResourceShareInvitationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceShareInvitationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_share_invitation_ids):
            query['ResourceShareInvitationIds'] = request.resource_share_invitation_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShareInvitations',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceShareInvitationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_share_invitations_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListResourceShareInvitationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceShareInvitationsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListResourceShareInvitationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceShareInvitationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_share_invitation_ids):
            query['ResourceShareInvitationIds'] = request.resource_share_invitation_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShareInvitations',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceShareInvitationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_share_invitations(
        self,
        request: resource_sharing_20200110_models.ListResourceShareInvitationsRequest,
    ) -> resource_sharing_20200110_models.ListResourceShareInvitationsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListResourceShareInvitationsRequest
        @return: ListResourceShareInvitationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_share_invitations_with_options(request, runtime)

    async def list_resource_share_invitations_async(
        self,
        request: resource_sharing_20200110_models.ListResourceShareInvitationsRequest,
    ) -> resource_sharing_20200110_models.ListResourceShareInvitationsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListResourceShareInvitationsRequest
        @return: ListResourceShareInvitationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_share_invitations_with_options_async(request, runtime)

    def list_resource_share_permissions_with_options(
        self,
        request: resource_sharing_20200110_models.ListResourceSharePermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceSharePermissionsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListResourceSharePermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceSharePermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceSharePermissions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceSharePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_share_permissions_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListResourceSharePermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceSharePermissionsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListResourceSharePermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceSharePermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceSharePermissions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceSharePermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_share_permissions(
        self,
        request: resource_sharing_20200110_models.ListResourceSharePermissionsRequest,
    ) -> resource_sharing_20200110_models.ListResourceSharePermissionsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListResourceSharePermissionsRequest
        @return: ListResourceSharePermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_share_permissions_with_options(request, runtime)

    async def list_resource_share_permissions_async(
        self,
        request: resource_sharing_20200110_models.ListResourceSharePermissionsRequest,
    ) -> resource_sharing_20200110_models.ListResourceSharePermissionsResponse:
        """
        The maximum number of entries to return for a single request.
        Valid values: 1 to 100. Default value: 20.
        
        @param request: ListResourceSharePermissionsRequest
        @return: ListResourceSharePermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_share_permissions_with_options_async(request, runtime)

    def list_resource_shares_with_options(
        self,
        request: resource_sharing_20200110_models.ListResourceSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceSharesResponse:
        """
        The operation that you want to perform. Set the value to ListResourceShares.
        
        @param request: ListResourceSharesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceSharesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not UtilClient.is_unset(request.resource_share_status):
            query['ResourceShareStatus'] = request.resource_share_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShares',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceSharesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_shares_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListResourceSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceSharesResponse:
        """
        The operation that you want to perform. Set the value to ListResourceShares.
        
        @param request: ListResourceSharesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceSharesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not UtilClient.is_unset(request.resource_share_status):
            query['ResourceShareStatus'] = request.resource_share_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShares',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceSharesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_shares(
        self,
        request: resource_sharing_20200110_models.ListResourceSharesRequest,
    ) -> resource_sharing_20200110_models.ListResourceSharesResponse:
        """
        The operation that you want to perform. Set the value to ListResourceShares.
        
        @param request: ListResourceSharesRequest
        @return: ListResourceSharesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_shares_with_options(request, runtime)

    async def list_resource_shares_async(
        self,
        request: resource_sharing_20200110_models.ListResourceSharesRequest,
    ) -> resource_sharing_20200110_models.ListResourceSharesResponse:
        """
        The operation that you want to perform. Set the value to ListResourceShares.
        
        @param request: ListResourceSharesRequest
        @return: ListResourceSharesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_shares_with_options_async(request, runtime)

    def list_shared_resources_with_options(
        self,
        request: resource_sharing_20200110_models.ListSharedResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListSharedResourcesResponse:
        """
        This topic provides an example on how to call the API operation to query the resources that you share with other accounts in the `cn-hangzhou` region. The response shows that in the resource share `rs-6GRmdD3X***`, you share the `vsw-bp1upw03qyz8n7us9****` resource of the `VSwitch` type with other accounts.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: ListSharedResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSharedResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedResources',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListSharedResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_shared_resources_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListSharedResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListSharedResourcesResponse:
        """
        This topic provides an example on how to call the API operation to query the resources that you share with other accounts in the `cn-hangzhou` region. The response shows that in the resource share `rs-6GRmdD3X***`, you share the `vsw-bp1upw03qyz8n7us9****` resource of the `VSwitch` type with other accounts.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: ListSharedResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSharedResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedResources',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListSharedResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_shared_resources(
        self,
        request: resource_sharing_20200110_models.ListSharedResourcesRequest,
    ) -> resource_sharing_20200110_models.ListSharedResourcesResponse:
        """
        This topic provides an example on how to call the API operation to query the resources that you share with other accounts in the `cn-hangzhou` region. The response shows that in the resource share `rs-6GRmdD3X***`, you share the `vsw-bp1upw03qyz8n7us9****` resource of the `VSwitch` type with other accounts.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: ListSharedResourcesRequest
        @return: ListSharedResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_shared_resources_with_options(request, runtime)

    async def list_shared_resources_async(
        self,
        request: resource_sharing_20200110_models.ListSharedResourcesRequest,
    ) -> resource_sharing_20200110_models.ListSharedResourcesResponse:
        """
        This topic provides an example on how to call the API operation to query the resources that you share with other accounts in the `cn-hangzhou` region. The response shows that in the resource share `rs-6GRmdD3X***`, you share the `vsw-bp1upw03qyz8n7us9****` resource of the `VSwitch` type with other accounts.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: ListSharedResourcesRequest
        @return: ListSharedResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_shared_resources_with_options_async(request, runtime)

    def list_shared_targets_with_options(
        self,
        request: resource_sharing_20200110_models.ListSharedTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListSharedTargetsResponse:
        """
        If you are a resource owner, you can query the principals with which you share your resources.
        If you are a principal, you can query the resources that are shared with you.
        This topic provides an example on how to call the API operation to query the principals with which you share your resources in the `cn-hangzhou` region. The response shows that you share your resources with the principals `114240524784****` and `172050525300****`.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: ListSharedTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSharedTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedTargets',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListSharedTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_shared_targets_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListSharedTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListSharedTargetsResponse:
        """
        If you are a resource owner, you can query the principals with which you share your resources.
        If you are a principal, you can query the resources that are shared with you.
        This topic provides an example on how to call the API operation to query the principals with which you share your resources in the `cn-hangzhou` region. The response shows that you share your resources with the principals `114240524784****` and `172050525300****`.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: ListSharedTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSharedTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedTargets',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListSharedTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_shared_targets(
        self,
        request: resource_sharing_20200110_models.ListSharedTargetsRequest,
    ) -> resource_sharing_20200110_models.ListSharedTargetsResponse:
        """
        If you are a resource owner, you can query the principals with which you share your resources.
        If you are a principal, you can query the resources that are shared with you.
        This topic provides an example on how to call the API operation to query the principals with which you share your resources in the `cn-hangzhou` region. The response shows that you share your resources with the principals `114240524784****` and `172050525300****`.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: ListSharedTargetsRequest
        @return: ListSharedTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_shared_targets_with_options(request, runtime)

    async def list_shared_targets_async(
        self,
        request: resource_sharing_20200110_models.ListSharedTargetsRequest,
    ) -> resource_sharing_20200110_models.ListSharedTargetsResponse:
        """
        If you are a resource owner, you can query the principals with which you share your resources.
        If you are a principal, you can query the resources that are shared with you.
        This topic provides an example on how to call the API operation to query the principals with which you share your resources in the `cn-hangzhou` region. The response shows that you share your resources with the principals `114240524784****` and `172050525300****`.
        ## Limits
        You can call this operation up to 20 times per second per account. This operation is globally limited to 500 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: ListSharedTargetsRequest
        @return: ListSharedTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_shared_targets_with_options_async(request, runtime)

    def reject_resource_share_invitation_with_options(
        self,
        request: resource_sharing_20200110_models.RejectResourceShareInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.RejectResourceShareInvitationResponse:
        """
        The ID of the resource sharing invitation.
        You can call the [ListResourceShareInvitations](~~450564~~) operation to obtain the ID of a resource sharing invitation.
        
        @param request: RejectResourceShareInvitationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RejectResourceShareInvitationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectResourceShareInvitation',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.RejectResourceShareInvitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_resource_share_invitation_with_options_async(
        self,
        request: resource_sharing_20200110_models.RejectResourceShareInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.RejectResourceShareInvitationResponse:
        """
        The ID of the resource sharing invitation.
        You can call the [ListResourceShareInvitations](~~450564~~) operation to obtain the ID of a resource sharing invitation.
        
        @param request: RejectResourceShareInvitationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RejectResourceShareInvitationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectResourceShareInvitation',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.RejectResourceShareInvitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_resource_share_invitation(
        self,
        request: resource_sharing_20200110_models.RejectResourceShareInvitationRequest,
    ) -> resource_sharing_20200110_models.RejectResourceShareInvitationResponse:
        """
        The ID of the resource sharing invitation.
        You can call the [ListResourceShareInvitations](~~450564~~) operation to obtain the ID of a resource sharing invitation.
        
        @param request: RejectResourceShareInvitationRequest
        @return: RejectResourceShareInvitationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reject_resource_share_invitation_with_options(request, runtime)

    async def reject_resource_share_invitation_async(
        self,
        request: resource_sharing_20200110_models.RejectResourceShareInvitationRequest,
    ) -> resource_sharing_20200110_models.RejectResourceShareInvitationResponse:
        """
        The ID of the resource sharing invitation.
        You can call the [ListResourceShareInvitations](~~450564~~) operation to obtain the ID of a resource sharing invitation.
        
        @param request: RejectResourceShareInvitationRequest
        @return: RejectResourceShareInvitationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reject_resource_share_invitation_with_options_async(request, runtime)

    def update_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.UpdateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.UpdateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to UpdateResourceShare.
        
        @param request: UpdateResourceShareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.UpdateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.UpdateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.UpdateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to UpdateResourceShare.
        
        @param request: UpdateResourceShareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.UpdateResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_share(
        self,
        request: resource_sharing_20200110_models.UpdateResourceShareRequest,
    ) -> resource_sharing_20200110_models.UpdateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to UpdateResourceShare.
        
        @param request: UpdateResourceShareRequest
        @return: UpdateResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_resource_share_with_options(request, runtime)

    async def update_resource_share_async(
        self,
        request: resource_sharing_20200110_models.UpdateResourceShareRequest,
    ) -> resource_sharing_20200110_models.UpdateResourceShareResponse:
        """
        The operation that you want to perform. Set the value to UpdateResourceShare.
        
        @param request: UpdateResourceShareRequest
        @return: UpdateResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_share_with_options_async(request, runtime)
