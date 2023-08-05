# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DeviceManagedNetworksArgs', 'DeviceManagedNetworks']

@pulumi.input_type
class DeviceManagedNetworksArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 config: pulumi.Input['DeviceManagedNetworksConfigArgs'],
                 name: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        The set of arguments for constructing a DeviceManagedNetworks resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input['DeviceManagedNetworksConfigArgs'] config: The configuration containing information for the WARP client to detect the managed network.
        :param pulumi.Input[str] name: The name of the Device Managed Network. Must be unique.
        :param pulumi.Input[str] type: The type of Device Managed Network. Available values: `tls`.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "config", config)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)

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
    def config(self) -> pulumi.Input['DeviceManagedNetworksConfigArgs']:
        """
        The configuration containing information for the WARP client to detect the managed network.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: pulumi.Input['DeviceManagedNetworksConfigArgs']):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the Device Managed Network. Must be unique.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of Device Managed Network. Available values: `tls`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _DeviceManagedNetworksState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input['DeviceManagedNetworksConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DeviceManagedNetworks resources.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input['DeviceManagedNetworksConfigArgs'] config: The configuration containing information for the WARP client to detect the managed network.
        :param pulumi.Input[str] name: The name of the Device Managed Network. Must be unique.
        :param pulumi.Input[str] type: The type of Device Managed Network. Available values: `tls`.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

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
    def config(self) -> Optional[pulumi.Input['DeviceManagedNetworksConfigArgs']]:
        """
        The configuration containing information for the WARP client to detect the managed network.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input['DeviceManagedNetworksConfigArgs']]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Device Managed Network. Must be unique.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of Device Managed Network. Available values: `tls`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class DeviceManagedNetworks(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['DeviceManagedNetworksConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloudflare Device Managed Network resource. Device managed networks allow for building location-aware device settings policies.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        managed_networks = cloudflare.DeviceManagedNetworks("managedNetworks",
            account_id="f037e56e89293a057740de681ac9abbe",
            config=cloudflare.DeviceManagedNetworksConfigArgs(
                sha256="b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c",
                tls_sockaddr="foobar:1234",
            ),
            name="managed-network-1",
            type="tls")
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/deviceManagedNetworks:DeviceManagedNetworks example <account_id>/<device_managed_networks_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[pulumi.InputType['DeviceManagedNetworksConfigArgs']] config: The configuration containing information for the WARP client to detect the managed network.
        :param pulumi.Input[str] name: The name of the Device Managed Network. Must be unique.
        :param pulumi.Input[str] type: The type of Device Managed Network. Available values: `tls`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeviceManagedNetworksArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare Device Managed Network resource. Device managed networks allow for building location-aware device settings policies.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        managed_networks = cloudflare.DeviceManagedNetworks("managedNetworks",
            account_id="f037e56e89293a057740de681ac9abbe",
            config=cloudflare.DeviceManagedNetworksConfigArgs(
                sha256="b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c",
                tls_sockaddr="foobar:1234",
            ),
            name="managed-network-1",
            type="tls")
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/deviceManagedNetworks:DeviceManagedNetworks example <account_id>/<device_managed_networks_id>
        ```

        :param str resource_name: The name of the resource.
        :param DeviceManagedNetworksArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeviceManagedNetworksArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['DeviceManagedNetworksConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeviceManagedNetworksArgs.__new__(DeviceManagedNetworksArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            if config is None and not opts.urn:
                raise TypeError("Missing required property 'config'")
            __props__.__dict__["config"] = config
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(DeviceManagedNetworks, __self__).__init__(
            'cloudflare:index/deviceManagedNetworks:DeviceManagedNetworks',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            config: Optional[pulumi.Input[pulumi.InputType['DeviceManagedNetworksConfigArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'DeviceManagedNetworks':
        """
        Get an existing DeviceManagedNetworks resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[pulumi.InputType['DeviceManagedNetworksConfigArgs']] config: The configuration containing information for the WARP client to detect the managed network.
        :param pulumi.Input[str] name: The name of the Device Managed Network. Must be unique.
        :param pulumi.Input[str] type: The type of Device Managed Network. Available values: `tls`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DeviceManagedNetworksState.__new__(_DeviceManagedNetworksState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["config"] = config
        __props__.__dict__["name"] = name
        __props__.__dict__["type"] = type
        return DeviceManagedNetworks(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account identifier to target for the resource.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output['outputs.DeviceManagedNetworksConfig']:
        """
        The configuration containing information for the WARP client to detect the managed network.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Device Managed Network. Must be unique.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of Device Managed Network. Available values: `tls`.
        """
        return pulumi.get(self, "type")

