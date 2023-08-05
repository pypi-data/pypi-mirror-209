# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['FirewallDeviceInitArgs', 'FirewallDevice']

@pulumi.input_type
class FirewallDeviceInitArgs:
    def __init__(__self__, *,
                 entity_id: pulumi.Input[int],
                 firewall_id: pulumi.Input[int],
                 entity_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FirewallDevice resource.
        :param pulumi.Input[int] entity_id: The unique ID of the entity to attach.
        :param pulumi.Input[int] firewall_id: The unique ID of the target Firewall.
        :param pulumi.Input[str] entity_type: The type of the entity to attach. (default: `linode`)
        """
        pulumi.set(__self__, "entity_id", entity_id)
        pulumi.set(__self__, "firewall_id", firewall_id)
        if entity_type is not None:
            pulumi.set(__self__, "entity_type", entity_type)

    @property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> pulumi.Input[int]:
        """
        The unique ID of the entity to attach.
        """
        return pulumi.get(self, "entity_id")

    @entity_id.setter
    def entity_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "entity_id", value)

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> pulumi.Input[int]:
        """
        The unique ID of the target Firewall.
        """
        return pulumi.get(self, "firewall_id")

    @firewall_id.setter
    def firewall_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "firewall_id", value)

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the entity to attach. (default: `linode`)
        """
        return pulumi.get(self, "entity_type")

    @entity_type.setter
    def entity_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entity_type", value)


@pulumi.input_type
class _FirewallDeviceState:
    def __init__(__self__, *,
                 created: Optional[pulumi.Input[str]] = None,
                 entity_id: Optional[pulumi.Input[int]] = None,
                 entity_type: Optional[pulumi.Input[str]] = None,
                 firewall_id: Optional[pulumi.Input[int]] = None,
                 updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FirewallDevice resources.
        :param pulumi.Input[str] created: When the Firewall Device was last created.
        :param pulumi.Input[int] entity_id: The unique ID of the entity to attach.
        :param pulumi.Input[str] entity_type: The type of the entity to attach. (default: `linode`)
        :param pulumi.Input[int] firewall_id: The unique ID of the target Firewall.
        :param pulumi.Input[str] updated: When the Firewall Device was last updated.
        """
        if created is not None:
            pulumi.set(__self__, "created", created)
        if entity_id is not None:
            pulumi.set(__self__, "entity_id", entity_id)
        if entity_type is not None:
            pulumi.set(__self__, "entity_type", entity_type)
        if firewall_id is not None:
            pulumi.set(__self__, "firewall_id", firewall_id)
        if updated is not None:
            pulumi.set(__self__, "updated", updated)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[str]]:
        """
        When the Firewall Device was last created.
        """
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> Optional[pulumi.Input[int]]:
        """
        The unique ID of the entity to attach.
        """
        return pulumi.get(self, "entity_id")

    @entity_id.setter
    def entity_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "entity_id", value)

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the entity to attach. (default: `linode`)
        """
        return pulumi.get(self, "entity_type")

    @entity_type.setter
    def entity_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entity_type", value)

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> Optional[pulumi.Input[int]]:
        """
        The unique ID of the target Firewall.
        """
        return pulumi.get(self, "firewall_id")

    @firewall_id.setter
    def firewall_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "firewall_id", value)

    @property
    @pulumi.getter
    def updated(self) -> Optional[pulumi.Input[str]]:
        """
        When the Firewall Device was last updated.
        """
        return pulumi.get(self, "updated")

    @updated.setter
    def updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated", value)


class FirewallDevice(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 entity_id: Optional[pulumi.Input[int]] = None,
                 entity_type: Optional[pulumi.Input[str]] = None,
                 firewall_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Manages a Linode Firewall Device.

        **NOTICE:** Attaching a Linode Firewall Device to a `Firewall` resource with user-defined `linodes` may cause device conflicts.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_linode as linode

        my_firewall = linode.Firewall("myFirewall",
            label="my_firewall",
            inbounds=[linode.FirewallInboundArgs(
                label="http",
                action="ACCEPT",
                protocol="TCP",
                ports="80",
                ipv4s=["0.0.0.0/0"],
                ipv6s=["::/0"],
            )],
            inbound_policy="DROP",
            outbound_policy="ACCEPT")
        my_instance = linode.Instance("myInstance",
            label="my_instance",
            region="us-southeast",
            type="g6-standard-1")
        my_device = linode.FirewallDevice("myDevice",
            firewall_id=my_firewall.id,
            entity_id=my_instance.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] entity_id: The unique ID of the entity to attach.
        :param pulumi.Input[str] entity_type: The type of the entity to attach. (default: `linode`)
        :param pulumi.Input[int] firewall_id: The unique ID of the target Firewall.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallDeviceInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Linode Firewall Device.

        **NOTICE:** Attaching a Linode Firewall Device to a `Firewall` resource with user-defined `linodes` may cause device conflicts.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_linode as linode

        my_firewall = linode.Firewall("myFirewall",
            label="my_firewall",
            inbounds=[linode.FirewallInboundArgs(
                label="http",
                action="ACCEPT",
                protocol="TCP",
                ports="80",
                ipv4s=["0.0.0.0/0"],
                ipv6s=["::/0"],
            )],
            inbound_policy="DROP",
            outbound_policy="ACCEPT")
        my_instance = linode.Instance("myInstance",
            label="my_instance",
            region="us-southeast",
            type="g6-standard-1")
        my_device = linode.FirewallDevice("myDevice",
            firewall_id=my_firewall.id,
            entity_id=my_instance.id)
        ```

        :param str resource_name: The name of the resource.
        :param FirewallDeviceInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallDeviceInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 entity_id: Optional[pulumi.Input[int]] = None,
                 entity_type: Optional[pulumi.Input[str]] = None,
                 firewall_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallDeviceInitArgs.__new__(FirewallDeviceInitArgs)

            if entity_id is None and not opts.urn:
                raise TypeError("Missing required property 'entity_id'")
            __props__.__dict__["entity_id"] = entity_id
            __props__.__dict__["entity_type"] = entity_type
            if firewall_id is None and not opts.urn:
                raise TypeError("Missing required property 'firewall_id'")
            __props__.__dict__["firewall_id"] = firewall_id
            __props__.__dict__["created"] = None
            __props__.__dict__["updated"] = None
        super(FirewallDevice, __self__).__init__(
            'linode:index/firewallDevice:FirewallDevice',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created: Optional[pulumi.Input[str]] = None,
            entity_id: Optional[pulumi.Input[int]] = None,
            entity_type: Optional[pulumi.Input[str]] = None,
            firewall_id: Optional[pulumi.Input[int]] = None,
            updated: Optional[pulumi.Input[str]] = None) -> 'FirewallDevice':
        """
        Get an existing FirewallDevice resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created: When the Firewall Device was last created.
        :param pulumi.Input[int] entity_id: The unique ID of the entity to attach.
        :param pulumi.Input[str] entity_type: The type of the entity to attach. (default: `linode`)
        :param pulumi.Input[int] firewall_id: The unique ID of the target Firewall.
        :param pulumi.Input[str] updated: When the Firewall Device was last updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FirewallDeviceState.__new__(_FirewallDeviceState)

        __props__.__dict__["created"] = created
        __props__.__dict__["entity_id"] = entity_id
        __props__.__dict__["entity_type"] = entity_type
        __props__.__dict__["firewall_id"] = firewall_id
        __props__.__dict__["updated"] = updated
        return FirewallDevice(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        When the Firewall Device was last created.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> pulumi.Output[int]:
        """
        The unique ID of the entity to attach.
        """
        return pulumi.get(self, "entity_id")

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the entity to attach. (default: `linode`)
        """
        return pulumi.get(self, "entity_type")

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> pulumi.Output[int]:
        """
        The unique ID of the target Firewall.
        """
        return pulumi.get(self, "firewall_id")

    @property
    @pulumi.getter
    def updated(self) -> pulumi.Output[str]:
        """
        When the Firewall Device was last updated.
        """
        return pulumi.get(self, "updated")

