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
    'GetKernelResult',
    'AwaitableGetKernelResult',
    'get_kernel',
    'get_kernel_output',
]

@pulumi.output_type
class GetKernelResult:
    """
    A collection of values returned by getKernel.
    """
    def __init__(__self__, architecture=None, deprecated=None, id=None, kvm=None, label=None, pvops=None, version=None, xen=None):
        if architecture and not isinstance(architecture, str):
            raise TypeError("Expected argument 'architecture' to be a str")
        pulumi.set(__self__, "architecture", architecture)
        if deprecated and not isinstance(deprecated, bool):
            raise TypeError("Expected argument 'deprecated' to be a bool")
        pulumi.set(__self__, "deprecated", deprecated)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kvm and not isinstance(kvm, bool):
            raise TypeError("Expected argument 'kvm' to be a bool")
        pulumi.set(__self__, "kvm", kvm)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if pvops and not isinstance(pvops, bool):
            raise TypeError("Expected argument 'pvops' to be a bool")
        pulumi.set(__self__, "pvops", pvops)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)
        if xen and not isinstance(xen, bool):
            raise TypeError("Expected argument 'xen' to be a bool")
        pulumi.set(__self__, "xen", xen)

    @property
    @pulumi.getter
    def architecture(self) -> str:
        """
        The architecture of this Kernel.
        """
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter
    def deprecated(self) -> bool:
        """
        Whether or not this Kernel is deprecated.
        """
        return pulumi.get(self, "deprecated")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kvm(self) -> bool:
        """
        If this Kernel is suitable for KVM Linodes.
        """
        return pulumi.get(self, "kvm")

    @property
    @pulumi.getter
    def label(self) -> str:
        """
        The friendly name of this Kernel.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def pvops(self) -> bool:
        """
        If this Kernel is suitable for paravirtualized operations.
        """
        return pulumi.get(self, "pvops")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Linux Kernel version
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter
    def xen(self) -> bool:
        """
        If this Kernel is suitable for Xen Linodes.
        """
        return pulumi.get(self, "xen")


class AwaitableGetKernelResult(GetKernelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKernelResult(
            architecture=self.architecture,
            deprecated=self.deprecated,
            id=self.id,
            kvm=self.kvm,
            label=self.label,
            pvops=self.pvops,
            version=self.version,
            xen=self.xen)


def get_kernel(id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKernelResult:
    """
    Provides information about a Linode kernel

    ## Example Usage

    The following example shows how one might use this data source to access information about a Linode kernel.

    ```python
    import pulumi
    import pulumi_linode as linode

    latest = linode.get_kernel(id="linode/latest-64bit")
    ```


    :param str id: The unique ID of this Kernel.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('linode:index/getKernel:getKernel', __args__, opts=opts, typ=GetKernelResult).value

    return AwaitableGetKernelResult(
        architecture=__ret__.architecture,
        deprecated=__ret__.deprecated,
        id=__ret__.id,
        kvm=__ret__.kvm,
        label=__ret__.label,
        pvops=__ret__.pvops,
        version=__ret__.version,
        xen=__ret__.xen)


@_utilities.lift_output_func(get_kernel)
def get_kernel_output(id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKernelResult]:
    """
    Provides information about a Linode kernel

    ## Example Usage

    The following example shows how one might use this data source to access information about a Linode kernel.

    ```python
    import pulumi
    import pulumi_linode as linode

    latest = linode.get_kernel(id="linode/latest-64bit")
    ```


    :param str id: The unique ID of this Kernel.
    """
    ...
