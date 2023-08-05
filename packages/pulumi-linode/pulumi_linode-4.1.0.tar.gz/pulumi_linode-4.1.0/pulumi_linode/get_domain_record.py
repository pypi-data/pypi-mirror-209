# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetDomainRecordResult',
    'AwaitableGetDomainRecordResult',
    'get_domain_record',
    'get_domain_record_output',
]

@pulumi.output_type
class GetDomainRecordResult:
    """
    A collection of values returned by getDomainRecord.
    """
    def __init__(__self__, domain_id=None, id=None, name=None, port=None, priority=None, protocol=None, service=None, tag=None, target=None, ttl_sec=None, type=None, weight=None):
        if domain_id and not isinstance(domain_id, int):
            raise TypeError("Expected argument 'domain_id' to be a int")
        pulumi.set(__self__, "domain_id", domain_id)
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if service and not isinstance(service, str):
            raise TypeError("Expected argument 'service' to be a str")
        pulumi.set(__self__, "service", service)
        if tag and not isinstance(tag, str):
            raise TypeError("Expected argument 'tag' to be a str")
        pulumi.set(__self__, "tag", tag)
        if target and not isinstance(target, str):
            raise TypeError("Expected argument 'target' to be a str")
        pulumi.set(__self__, "target", target)
        if ttl_sec and not isinstance(ttl_sec, int):
            raise TypeError("Expected argument 'ttl_sec' to be a int")
        pulumi.set(__self__, "ttl_sec", ttl_sec)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if weight and not isinstance(weight, int):
            raise TypeError("Expected argument 'weight' to be a int")
        pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> int:
        """
        The associated domain's unique ID.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[int]:
        """
        The unique ID of the Domain Record.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the Record.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        The port this Record points to.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        The priority of the target host. Lower values are preferred.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        The protocol this Record's service communicates with. Only valid for SRV records.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def service(self) -> str:
        """
        The service this Record identified. Only valid for SRV records.
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter
    def tag(self) -> str:
        """
        The tag portion of a CAA record.
        """
        return pulumi.get(self, "tag")

    @property
    @pulumi.getter
    def target(self) -> str:
        """
        The target for this Record. This field's actual usage depends on the type of record this represents. For A and AAAA records, this is the address the named Domain should resolve to.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter(name="ttlSec")
    def ttl_sec(self) -> int:
        """
        The amount of time in seconds that this Domain's records may be cached by resolvers or other domain servers.
        """
        return pulumi.get(self, "ttl_sec")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of Record this is in the DNS system. See all record types [here](https://www.linode.com/docs/api/domains/#domain-records-list__responses).
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def weight(self) -> int:
        """
        The relative weight of this Record. Higher values are preferred.
        """
        return pulumi.get(self, "weight")


class AwaitableGetDomainRecordResult(GetDomainRecordResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainRecordResult(
            domain_id=self.domain_id,
            id=self.id,
            name=self.name,
            port=self.port,
            priority=self.priority,
            protocol=self.protocol,
            service=self.service,
            tag=self.tag,
            target=self.target,
            ttl_sec=self.ttl_sec,
            type=self.type,
            weight=self.weight)


def get_domain_record(domain_id: Optional[int] = None,
                      id: Optional[int] = None,
                      name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainRecordResult:
    """
    Provides information about a Linode Domain Record.

    ## Example Usage

    The following example shows how one might use this data source to access information about a Linode Domain Record.

    ```python
    import pulumi
    import pulumi_linode as linode

    my_record = linode.get_domain_record(domain_id=3150401,
        id=14950401)
    my_www_record = linode.get_domain_record(domain_id=3150401,
        name="www")
    ```


    :param int domain_id: The associated domain's unique ID.
    :param int id: The unique ID of the Domain Record.
    :param str name: The name of the Record.
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('linode:index/getDomainRecord:getDomainRecord', __args__, opts=opts, typ=GetDomainRecordResult).value

    return AwaitableGetDomainRecordResult(
        domain_id=__ret__.domain_id,
        id=__ret__.id,
        name=__ret__.name,
        port=__ret__.port,
        priority=__ret__.priority,
        protocol=__ret__.protocol,
        service=__ret__.service,
        tag=__ret__.tag,
        target=__ret__.target,
        ttl_sec=__ret__.ttl_sec,
        type=__ret__.type,
        weight=__ret__.weight)


@_utilities.lift_output_func(get_domain_record)
def get_domain_record_output(domain_id: Optional[pulumi.Input[int]] = None,
                             id: Optional[pulumi.Input[Optional[int]]] = None,
                             name: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainRecordResult]:
    """
    Provides information about a Linode Domain Record.

    ## Example Usage

    The following example shows how one might use this data source to access information about a Linode Domain Record.

    ```python
    import pulumi
    import pulumi_linode as linode

    my_record = linode.get_domain_record(domain_id=3150401,
        id=14950401)
    my_www_record = linode.get_domain_record(domain_id=3150401,
        name="www")
    ```


    :param int domain_id: The associated domain's unique ID.
    :param int id: The unique ID of the Domain Record.
    :param str name: The name of the Record.
    """
    ...
