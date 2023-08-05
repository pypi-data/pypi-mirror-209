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

__all__ = ['LkeClusterArgs', 'LkeCluster']

@pulumi.input_type
class LkeClusterArgs:
    def __init__(__self__, *,
                 k8s_version: pulumi.Input[str],
                 label: pulumi.Input[str],
                 pools: pulumi.Input[Sequence[pulumi.Input['LkeClusterPoolArgs']]],
                 region: pulumi.Input[str],
                 control_plane: Optional[pulumi.Input['LkeClusterControlPlaneArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a LkeCluster resource.
        :param pulumi.Input[str] k8s_version: The desired Kubernetes version for this Kubernetes cluster in the format of `major.minor` (e.g. `1.21`), and the latest supported patch version will be deployed.
        :param pulumi.Input[str] label: This Kubernetes cluster's unique label.
        :param pulumi.Input[Sequence[pulumi.Input['LkeClusterPoolArgs']]] pools: Additional nested attributes:
        :param pulumi.Input[str] region: This Kubernetes cluster's location.
               
               * `pool` - (Required) The Node Pool specifications for the Kubernetes cluster. At least one Node Pool is required.
               
               * `control_plane` (Optional) Defines settings for the Kubernetes Control Plane.
        :param pulumi.Input['LkeClusterControlPlaneArgs'] control_plane: Defines settings for the Kubernetes Control Plane.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.
        """
        pulumi.set(__self__, "k8s_version", k8s_version)
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "pools", pools)
        pulumi.set(__self__, "region", region)
        if control_plane is not None:
            pulumi.set(__self__, "control_plane", control_plane)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="k8sVersion")
    def k8s_version(self) -> pulumi.Input[str]:
        """
        The desired Kubernetes version for this Kubernetes cluster in the format of `major.minor` (e.g. `1.21`), and the latest supported patch version will be deployed.
        """
        return pulumi.get(self, "k8s_version")

    @k8s_version.setter
    def k8s_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "k8s_version", value)

    @property
    @pulumi.getter
    def label(self) -> pulumi.Input[str]:
        """
        This Kubernetes cluster's unique label.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: pulumi.Input[str]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def pools(self) -> pulumi.Input[Sequence[pulumi.Input['LkeClusterPoolArgs']]]:
        """
        Additional nested attributes:
        """
        return pulumi.get(self, "pools")

    @pools.setter
    def pools(self, value: pulumi.Input[Sequence[pulumi.Input['LkeClusterPoolArgs']]]):
        pulumi.set(self, "pools", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        This Kubernetes cluster's location.

        * `pool` - (Required) The Node Pool specifications for the Kubernetes cluster. At least one Node Pool is required.

        * `control_plane` (Optional) Defines settings for the Kubernetes Control Plane.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> Optional[pulumi.Input['LkeClusterControlPlaneArgs']]:
        """
        Defines settings for the Kubernetes Control Plane.
        """
        return pulumi.get(self, "control_plane")

    @control_plane.setter
    def control_plane(self, value: Optional[pulumi.Input['LkeClusterControlPlaneArgs']]):
        pulumi.set(self, "control_plane", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _LkeClusterState:
    def __init__(__self__, *,
                 api_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 control_plane: Optional[pulumi.Input['LkeClusterControlPlaneArgs']] = None,
                 dashboard_url: Optional[pulumi.Input[str]] = None,
                 k8s_version: Optional[pulumi.Input[str]] = None,
                 kubeconfig: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 pools: Optional[pulumi.Input[Sequence[pulumi.Input['LkeClusterPoolArgs']]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering LkeCluster resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] api_endpoints: The endpoints for the Kubernetes API server.
        :param pulumi.Input['LkeClusterControlPlaneArgs'] control_plane: Defines settings for the Kubernetes Control Plane.
        :param pulumi.Input[str] dashboard_url: The Kubernetes Dashboard access URL for this cluster.
        :param pulumi.Input[str] k8s_version: The desired Kubernetes version for this Kubernetes cluster in the format of `major.minor` (e.g. `1.21`), and the latest supported patch version will be deployed.
        :param pulumi.Input[str] kubeconfig: The base64 encoded kubeconfig for the Kubernetes cluster.
        :param pulumi.Input[str] label: This Kubernetes cluster's unique label.
        :param pulumi.Input[Sequence[pulumi.Input['LkeClusterPoolArgs']]] pools: Additional nested attributes:
        :param pulumi.Input[str] region: This Kubernetes cluster's location.
               
               * `pool` - (Required) The Node Pool specifications for the Kubernetes cluster. At least one Node Pool is required.
               
               * `control_plane` (Optional) Defines settings for the Kubernetes Control Plane.
        :param pulumi.Input[str] status: The status of the node. (`ready`, `not_ready`)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.
        """
        if api_endpoints is not None:
            pulumi.set(__self__, "api_endpoints", api_endpoints)
        if control_plane is not None:
            pulumi.set(__self__, "control_plane", control_plane)
        if dashboard_url is not None:
            pulumi.set(__self__, "dashboard_url", dashboard_url)
        if k8s_version is not None:
            pulumi.set(__self__, "k8s_version", k8s_version)
        if kubeconfig is not None:
            pulumi.set(__self__, "kubeconfig", kubeconfig)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if pools is not None:
            pulumi.set(__self__, "pools", pools)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="apiEndpoints")
    def api_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The endpoints for the Kubernetes API server.
        """
        return pulumi.get(self, "api_endpoints")

    @api_endpoints.setter
    def api_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "api_endpoints", value)

    @property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> Optional[pulumi.Input['LkeClusterControlPlaneArgs']]:
        """
        Defines settings for the Kubernetes Control Plane.
        """
        return pulumi.get(self, "control_plane")

    @control_plane.setter
    def control_plane(self, value: Optional[pulumi.Input['LkeClusterControlPlaneArgs']]):
        pulumi.set(self, "control_plane", value)

    @property
    @pulumi.getter(name="dashboardUrl")
    def dashboard_url(self) -> Optional[pulumi.Input[str]]:
        """
        The Kubernetes Dashboard access URL for this cluster.
        """
        return pulumi.get(self, "dashboard_url")

    @dashboard_url.setter
    def dashboard_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_url", value)

    @property
    @pulumi.getter(name="k8sVersion")
    def k8s_version(self) -> Optional[pulumi.Input[str]]:
        """
        The desired Kubernetes version for this Kubernetes cluster in the format of `major.minor` (e.g. `1.21`), and the latest supported patch version will be deployed.
        """
        return pulumi.get(self, "k8s_version")

    @k8s_version.setter
    def k8s_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "k8s_version", value)

    @property
    @pulumi.getter
    def kubeconfig(self) -> Optional[pulumi.Input[str]]:
        """
        The base64 encoded kubeconfig for the Kubernetes cluster.
        """
        return pulumi.get(self, "kubeconfig")

    @kubeconfig.setter
    def kubeconfig(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubeconfig", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        This Kubernetes cluster's unique label.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LkeClusterPoolArgs']]]]:
        """
        Additional nested attributes:
        """
        return pulumi.get(self, "pools")

    @pools.setter
    def pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LkeClusterPoolArgs']]]]):
        pulumi.set(self, "pools", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        This Kubernetes cluster's location.

        * `pool` - (Required) The Node Pool specifications for the Kubernetes cluster. At least one Node Pool is required.

        * `control_plane` (Optional) Defines settings for the Kubernetes Control Plane.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the node. (`ready`, `not_ready`)
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class LkeCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 control_plane: Optional[pulumi.Input[pulumi.InputType['LkeClusterControlPlaneArgs']]] = None,
                 k8s_version: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LkeClusterPoolArgs']]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages an LKE cluster.

        ## Example Usage

        Creating a basic LKE cluster:

        ```python
        import pulumi
        import pulumi_linode as linode

        my_cluster = linode.LkeCluster("my-cluster",
            k8s_version="1.21",
            label="my-cluster",
            pools=[linode.LkeClusterPoolArgs(
                count=3,
                type="g6-standard-2",
            )],
            region="us-central",
            tags=["prod"])
        ```

        Creating an LKE cluster with autoscaler:

        ```python
        import pulumi
        import pulumi_linode as linode

        my_cluster = linode.LkeCluster("my-cluster",
            label="my-cluster",
            k8s_version="1.21",
            region="us-central",
            tags=["prod"],
            pools=[linode.LkeClusterPoolArgs(
                type="g6-standard-2",
                count=3,
                autoscaler=linode.LkeClusterPoolAutoscalerArgs(
                    min=3,
                    max=10,
                ),
            )])
        ```

        ## Import

        LKE Clusters can be imported using the `id`, e.g.

        ```sh
         $ pulumi import linode:index/lkeCluster:LkeCluster my_cluster 12345
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['LkeClusterControlPlaneArgs']] control_plane: Defines settings for the Kubernetes Control Plane.
        :param pulumi.Input[str] k8s_version: The desired Kubernetes version for this Kubernetes cluster in the format of `major.minor` (e.g. `1.21`), and the latest supported patch version will be deployed.
        :param pulumi.Input[str] label: This Kubernetes cluster's unique label.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LkeClusterPoolArgs']]]] pools: Additional nested attributes:
        :param pulumi.Input[str] region: This Kubernetes cluster's location.
               
               * `pool` - (Required) The Node Pool specifications for the Kubernetes cluster. At least one Node Pool is required.
               
               * `control_plane` (Optional) Defines settings for the Kubernetes Control Plane.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LkeClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an LKE cluster.

        ## Example Usage

        Creating a basic LKE cluster:

        ```python
        import pulumi
        import pulumi_linode as linode

        my_cluster = linode.LkeCluster("my-cluster",
            k8s_version="1.21",
            label="my-cluster",
            pools=[linode.LkeClusterPoolArgs(
                count=3,
                type="g6-standard-2",
            )],
            region="us-central",
            tags=["prod"])
        ```

        Creating an LKE cluster with autoscaler:

        ```python
        import pulumi
        import pulumi_linode as linode

        my_cluster = linode.LkeCluster("my-cluster",
            label="my-cluster",
            k8s_version="1.21",
            region="us-central",
            tags=["prod"],
            pools=[linode.LkeClusterPoolArgs(
                type="g6-standard-2",
                count=3,
                autoscaler=linode.LkeClusterPoolAutoscalerArgs(
                    min=3,
                    max=10,
                ),
            )])
        ```

        ## Import

        LKE Clusters can be imported using the `id`, e.g.

        ```sh
         $ pulumi import linode:index/lkeCluster:LkeCluster my_cluster 12345
        ```

        :param str resource_name: The name of the resource.
        :param LkeClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LkeClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 control_plane: Optional[pulumi.Input[pulumi.InputType['LkeClusterControlPlaneArgs']]] = None,
                 k8s_version: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LkeClusterPoolArgs']]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LkeClusterArgs.__new__(LkeClusterArgs)

            __props__.__dict__["control_plane"] = control_plane
            if k8s_version is None and not opts.urn:
                raise TypeError("Missing required property 'k8s_version'")
            __props__.__dict__["k8s_version"] = k8s_version
            if label is None and not opts.urn:
                raise TypeError("Missing required property 'label'")
            __props__.__dict__["label"] = label
            if pools is None and not opts.urn:
                raise TypeError("Missing required property 'pools'")
            __props__.__dict__["pools"] = pools
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["tags"] = tags
            __props__.__dict__["api_endpoints"] = None
            __props__.__dict__["dashboard_url"] = None
            __props__.__dict__["kubeconfig"] = None
            __props__.__dict__["status"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["kubeconfig"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(LkeCluster, __self__).__init__(
            'linode:index/lkeCluster:LkeCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            control_plane: Optional[pulumi.Input[pulumi.InputType['LkeClusterControlPlaneArgs']]] = None,
            dashboard_url: Optional[pulumi.Input[str]] = None,
            k8s_version: Optional[pulumi.Input[str]] = None,
            kubeconfig: Optional[pulumi.Input[str]] = None,
            label: Optional[pulumi.Input[str]] = None,
            pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LkeClusterPoolArgs']]]]] = None,
            region: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'LkeCluster':
        """
        Get an existing LkeCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] api_endpoints: The endpoints for the Kubernetes API server.
        :param pulumi.Input[pulumi.InputType['LkeClusterControlPlaneArgs']] control_plane: Defines settings for the Kubernetes Control Plane.
        :param pulumi.Input[str] dashboard_url: The Kubernetes Dashboard access URL for this cluster.
        :param pulumi.Input[str] k8s_version: The desired Kubernetes version for this Kubernetes cluster in the format of `major.minor` (e.g. `1.21`), and the latest supported patch version will be deployed.
        :param pulumi.Input[str] kubeconfig: The base64 encoded kubeconfig for the Kubernetes cluster.
        :param pulumi.Input[str] label: This Kubernetes cluster's unique label.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LkeClusterPoolArgs']]]] pools: Additional nested attributes:
        :param pulumi.Input[str] region: This Kubernetes cluster's location.
               
               * `pool` - (Required) The Node Pool specifications for the Kubernetes cluster. At least one Node Pool is required.
               
               * `control_plane` (Optional) Defines settings for the Kubernetes Control Plane.
        :param pulumi.Input[str] status: The status of the node. (`ready`, `not_ready`)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LkeClusterState.__new__(_LkeClusterState)

        __props__.__dict__["api_endpoints"] = api_endpoints
        __props__.__dict__["control_plane"] = control_plane
        __props__.__dict__["dashboard_url"] = dashboard_url
        __props__.__dict__["k8s_version"] = k8s_version
        __props__.__dict__["kubeconfig"] = kubeconfig
        __props__.__dict__["label"] = label
        __props__.__dict__["pools"] = pools
        __props__.__dict__["region"] = region
        __props__.__dict__["status"] = status
        __props__.__dict__["tags"] = tags
        return LkeCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiEndpoints")
    def api_endpoints(self) -> pulumi.Output[Sequence[str]]:
        """
        The endpoints for the Kubernetes API server.
        """
        return pulumi.get(self, "api_endpoints")

    @property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> pulumi.Output['outputs.LkeClusterControlPlane']:
        """
        Defines settings for the Kubernetes Control Plane.
        """
        return pulumi.get(self, "control_plane")

    @property
    @pulumi.getter(name="dashboardUrl")
    def dashboard_url(self) -> pulumi.Output[str]:
        """
        The Kubernetes Dashboard access URL for this cluster.
        """
        return pulumi.get(self, "dashboard_url")

    @property
    @pulumi.getter(name="k8sVersion")
    def k8s_version(self) -> pulumi.Output[str]:
        """
        The desired Kubernetes version for this Kubernetes cluster in the format of `major.minor` (e.g. `1.21`), and the latest supported patch version will be deployed.
        """
        return pulumi.get(self, "k8s_version")

    @property
    @pulumi.getter
    def kubeconfig(self) -> pulumi.Output[str]:
        """
        The base64 encoded kubeconfig for the Kubernetes cluster.
        """
        return pulumi.get(self, "kubeconfig")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        """
        This Kubernetes cluster's unique label.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def pools(self) -> pulumi.Output[Sequence['outputs.LkeClusterPool']]:
        """
        Additional nested attributes:
        """
        return pulumi.get(self, "pools")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        This Kubernetes cluster's location.

        * `pool` - (Required) The Node Pool specifications for the Kubernetes cluster. At least one Node Pool is required.

        * `control_plane` (Optional) Defines settings for the Kubernetes Control Plane.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the node. (`ready`, `not_ready`)
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.
        """
        return pulumi.get(self, "tags")

