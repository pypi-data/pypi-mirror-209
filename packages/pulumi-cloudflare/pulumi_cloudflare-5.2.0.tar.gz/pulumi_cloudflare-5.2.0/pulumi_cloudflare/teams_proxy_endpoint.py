# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TeamsProxyEndpointArgs', 'TeamsProxyEndpoint']

@pulumi.input_type
class TeamsProxyEndpointArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 ips: pulumi.Input[Sequence[pulumi.Input[str]]],
                 name: pulumi.Input[str]):
        """
        The set of arguments for constructing a TeamsProxyEndpoint resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: The networks CIDRs that will be allowed to initiate proxy connections.
        :param pulumi.Input[str] name: Name of the teams proxy endpoint.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "ips", ips)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        The account identifier to target for the resource.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def ips(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The networks CIDRs that will be allowed to initiate proxy connections.
        """
        return pulumi.get(self, "ips")

    @ips.setter
    def ips(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "ips", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the teams proxy endpoint.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _TeamsProxyEndpointState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 subdomain: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TeamsProxyEndpoint resources.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: The networks CIDRs that will be allowed to initiate proxy connections.
        :param pulumi.Input[str] name: Name of the teams proxy endpoint.
        :param pulumi.Input[str] subdomain: The FQDN that proxy clients should be pointed at.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if ips is not None:
            pulumi.set(__self__, "ips", ips)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if subdomain is not None:
            pulumi.set(__self__, "subdomain", subdomain)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account identifier to target for the resource.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The networks CIDRs that will be allowed to initiate proxy connections.
        """
        return pulumi.get(self, "ips")

    @ips.setter
    def ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ips", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the teams proxy endpoint.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def subdomain(self) -> Optional[pulumi.Input[str]]:
        """
        The FQDN that proxy clients should be pointed at.
        """
        return pulumi.get(self, "subdomain")

    @subdomain.setter
    def subdomain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subdomain", value)


class TeamsProxyEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloudflare Teams Proxy Endpoint resource. Teams Proxy
        Endpoints are used for pointing proxy clients at Cloudflare Secure
        Gateway.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.TeamsProxyEndpoint("example",
            account_id="f037e56e89293a057740de681ac9abbe",
            ips=["192.0.2.0/24"],
            name="office")
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/teamsProxyEndpoint:TeamsProxyEndpoint example <account_id>/<proxy_endpoint_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: The networks CIDRs that will be allowed to initiate proxy connections.
        :param pulumi.Input[str] name: Name of the teams proxy endpoint.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TeamsProxyEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare Teams Proxy Endpoint resource. Teams Proxy
        Endpoints are used for pointing proxy clients at Cloudflare Secure
        Gateway.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.TeamsProxyEndpoint("example",
            account_id="f037e56e89293a057740de681ac9abbe",
            ips=["192.0.2.0/24"],
            name="office")
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/teamsProxyEndpoint:TeamsProxyEndpoint example <account_id>/<proxy_endpoint_id>
        ```

        :param str resource_name: The name of the resource.
        :param TeamsProxyEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TeamsProxyEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TeamsProxyEndpointArgs.__new__(TeamsProxyEndpointArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            if ips is None and not opts.urn:
                raise TypeError("Missing required property 'ips'")
            __props__.__dict__["ips"] = ips
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["subdomain"] = None
        super(TeamsProxyEndpoint, __self__).__init__(
            'cloudflare:index/teamsProxyEndpoint:TeamsProxyEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            subdomain: Optional[pulumi.Input[str]] = None) -> 'TeamsProxyEndpoint':
        """
        Get an existing TeamsProxyEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: The networks CIDRs that will be allowed to initiate proxy connections.
        :param pulumi.Input[str] name: Name of the teams proxy endpoint.
        :param pulumi.Input[str] subdomain: The FQDN that proxy clients should be pointed at.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TeamsProxyEndpointState.__new__(_TeamsProxyEndpointState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["ips"] = ips
        __props__.__dict__["name"] = name
        __props__.__dict__["subdomain"] = subdomain
        return TeamsProxyEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account identifier to target for the resource.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def ips(self) -> pulumi.Output[Sequence[str]]:
        """
        The networks CIDRs that will be allowed to initiate proxy connections.
        """
        return pulumi.get(self, "ips")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the teams proxy endpoint.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def subdomain(self) -> pulumi.Output[str]:
        """
        The FQDN that proxy clients should be pointed at.
        """
        return pulumi.get(self, "subdomain")

