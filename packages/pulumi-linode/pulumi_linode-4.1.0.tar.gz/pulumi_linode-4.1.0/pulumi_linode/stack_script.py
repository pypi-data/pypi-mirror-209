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

__all__ = ['StackScriptArgs', 'StackScript']

@pulumi.input_type
class StackScriptArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 images: pulumi.Input[Sequence[pulumi.Input[str]]],
                 label: pulumi.Input[str],
                 script: pulumi.Input[str],
                 is_public: Optional[pulumi.Input[bool]] = None,
                 rev_note: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StackScript resource.
        :param pulumi.Input[str] description: A description for the StackScript.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] images: A set of Image IDs representing the Images that this StackScript is compatible for deploying with. `any/all` indicates that all available image distributions, including private images, are accepted. Currently private image IDs are not supported.
               
               - - -
        :param pulumi.Input[str] label: The StackScript's label is for display purposes only.
        :param pulumi.Input[str] script: The script to execute when provisioning a new Linode with this StackScript.
        :param pulumi.Input[bool] is_public: This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. *Changing `is_public` forces the creation of a new StackScript*
        :param pulumi.Input[str] rev_note: This field allows you to add notes for the set of revisions made to this StackScript.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "images", images)
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "script", script)
        if is_public is not None:
            pulumi.set(__self__, "is_public", is_public)
        if rev_note is not None:
            pulumi.set(__self__, "rev_note", rev_note)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        A description for the StackScript.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def images(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A set of Image IDs representing the Images that this StackScript is compatible for deploying with. `any/all` indicates that all available image distributions, including private images, are accepted. Currently private image IDs are not supported.

        - - -
        """
        return pulumi.get(self, "images")

    @images.setter
    def images(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "images", value)

    @property
    @pulumi.getter
    def label(self) -> pulumi.Input[str]:
        """
        The StackScript's label is for display purposes only.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: pulumi.Input[str]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def script(self) -> pulumi.Input[str]:
        """
        The script to execute when provisioning a new Linode with this StackScript.
        """
        return pulumi.get(self, "script")

    @script.setter
    def script(self, value: pulumi.Input[str]):
        pulumi.set(self, "script", value)

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> Optional[pulumi.Input[bool]]:
        """
        This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. *Changing `is_public` forces the creation of a new StackScript*
        """
        return pulumi.get(self, "is_public")

    @is_public.setter
    def is_public(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_public", value)

    @property
    @pulumi.getter(name="revNote")
    def rev_note(self) -> Optional[pulumi.Input[str]]:
        """
        This field allows you to add notes for the set of revisions made to this StackScript.
        """
        return pulumi.get(self, "rev_note")

    @rev_note.setter
    def rev_note(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rev_note", value)


@pulumi.input_type
class _StackScriptState:
    def __init__(__self__, *,
                 created: Optional[pulumi.Input[str]] = None,
                 deployments_active: Optional[pulumi.Input[int]] = None,
                 deployments_total: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 images: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_public: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 rev_note: Optional[pulumi.Input[str]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 updated: Optional[pulumi.Input[str]] = None,
                 user_defined_fields: Optional[pulumi.Input[Sequence[pulumi.Input['StackScriptUserDefinedFieldArgs']]]] = None,
                 user_gravatar_id: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering StackScript resources.
        :param pulumi.Input[str] created: The date this StackScript was created.
        :param pulumi.Input[int] deployments_active: Count of currently active, deployed Linodes created from this StackScript.
        :param pulumi.Input[int] deployments_total: The total number of times this StackScript has been deployed.
        :param pulumi.Input[str] description: A description for the StackScript.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] images: A set of Image IDs representing the Images that this StackScript is compatible for deploying with. `any/all` indicates that all available image distributions, including private images, are accepted. Currently private image IDs are not supported.
               
               - - -
        :param pulumi.Input[bool] is_public: This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. *Changing `is_public` forces the creation of a new StackScript*
        :param pulumi.Input[str] label: The StackScript's label is for display purposes only.
        :param pulumi.Input[str] rev_note: This field allows you to add notes for the set of revisions made to this StackScript.
        :param pulumi.Input[str] script: The script to execute when provisioning a new Linode with this StackScript.
        :param pulumi.Input[str] updated: The date this StackScript was updated.
        :param pulumi.Input[Sequence[pulumi.Input['StackScriptUserDefinedFieldArgs']]] user_defined_fields: This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized parameters during deployment.
        :param pulumi.Input[str] user_gravatar_id: The Gravatar ID for the User who created the StackScript.
        :param pulumi.Input[str] username: The User who created the StackScript.
        """
        if created is not None:
            pulumi.set(__self__, "created", created)
        if deployments_active is not None:
            pulumi.set(__self__, "deployments_active", deployments_active)
        if deployments_total is not None:
            pulumi.set(__self__, "deployments_total", deployments_total)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if images is not None:
            pulumi.set(__self__, "images", images)
        if is_public is not None:
            pulumi.set(__self__, "is_public", is_public)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if rev_note is not None:
            pulumi.set(__self__, "rev_note", rev_note)
        if script is not None:
            pulumi.set(__self__, "script", script)
        if updated is not None:
            pulumi.set(__self__, "updated", updated)
        if user_defined_fields is not None:
            pulumi.set(__self__, "user_defined_fields", user_defined_fields)
        if user_gravatar_id is not None:
            pulumi.set(__self__, "user_gravatar_id", user_gravatar_id)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[str]]:
        """
        The date this StackScript was created.
        """
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter(name="deploymentsActive")
    def deployments_active(self) -> Optional[pulumi.Input[int]]:
        """
        Count of currently active, deployed Linodes created from this StackScript.
        """
        return pulumi.get(self, "deployments_active")

    @deployments_active.setter
    def deployments_active(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "deployments_active", value)

    @property
    @pulumi.getter(name="deploymentsTotal")
    def deployments_total(self) -> Optional[pulumi.Input[int]]:
        """
        The total number of times this StackScript has been deployed.
        """
        return pulumi.get(self, "deployments_total")

    @deployments_total.setter
    def deployments_total(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "deployments_total", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the StackScript.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of Image IDs representing the Images that this StackScript is compatible for deploying with. `any/all` indicates that all available image distributions, including private images, are accepted. Currently private image IDs are not supported.

        - - -
        """
        return pulumi.get(self, "images")

    @images.setter
    def images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "images", value)

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> Optional[pulumi.Input[bool]]:
        """
        This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. *Changing `is_public` forces the creation of a new StackScript*
        """
        return pulumi.get(self, "is_public")

    @is_public.setter
    def is_public(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_public", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        The StackScript's label is for display purposes only.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="revNote")
    def rev_note(self) -> Optional[pulumi.Input[str]]:
        """
        This field allows you to add notes for the set of revisions made to this StackScript.
        """
        return pulumi.get(self, "rev_note")

    @rev_note.setter
    def rev_note(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rev_note", value)

    @property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[str]]:
        """
        The script to execute when provisioning a new Linode with this StackScript.
        """
        return pulumi.get(self, "script")

    @script.setter
    def script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script", value)

    @property
    @pulumi.getter
    def updated(self) -> Optional[pulumi.Input[str]]:
        """
        The date this StackScript was updated.
        """
        return pulumi.get(self, "updated")

    @updated.setter
    def updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated", value)

    @property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackScriptUserDefinedFieldArgs']]]]:
        """
        This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized parameters during deployment.
        """
        return pulumi.get(self, "user_defined_fields")

    @user_defined_fields.setter
    def user_defined_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackScriptUserDefinedFieldArgs']]]]):
        pulumi.set(self, "user_defined_fields", value)

    @property
    @pulumi.getter(name="userGravatarId")
    def user_gravatar_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Gravatar ID for the User who created the StackScript.
        """
        return pulumi.get(self, "user_gravatar_id")

    @user_gravatar_id.setter
    def user_gravatar_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_gravatar_id", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        The User who created the StackScript.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class StackScript(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 images: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_public: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 rev_note: Optional[pulumi.Input[str]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Linode StackScript resource.  This can be used to create, modify, and delete Linode StackScripts.  StackScripts are private or public managed scripts which run within an instance during startup.  StackScripts can include variables whose values are specified when the Instance is created.

        For more information, see [Automate Deployment with StackScripts](https://www.linode.com/docs/platform/stackscripts/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#tag/StackScripts).

        ## Example Usage

        The following example shows how one might use this resource to configure a StackScript attached to a Linode Instance.  As shown below, StackScripts must begin with a shebang (`#!`).  The `<UDF ...>` element provided in the Bash comment block defines a variable whose value is provided when creating the Instance (or disk) using the `stackscript_data` field.

        ```python
        import pulumi
        import pulumi_linode as linode

        foo_stack_script = linode.StackScript("fooStackScript",
            label="foo",
            description="Installs a Package",
            script=\"\"\"#!/bin/bash
        # <UDF name="package" label="System Package to Install" example="nginx" default="">
        apt-get -q update && apt-get -q -y install $PACKAGE
        \"\"\",
            images=[
                "linode/ubuntu18.04",
                "linode/ubuntu16.04lts",
            ],
            rev_note="initial version")
        foo_instance = linode.Instance("fooInstance",
            image="linode/ubuntu18.04",
            label="foo",
            region="us-east",
            type="g6-nanode-1",
            authorized_keys=["..."],
            root_pass="...",
            stackscript_id=foo_stack_script.id,
            stackscript_data={
                "package": "nginx",
            })
        ```

        ## Import

        Linodes StackScripts can be imported using the Linode StackScript `id`, e.g.

        ```sh
         $ pulumi import linode:index/stackScript:StackScript mystackscript 1234567
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description for the StackScript.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] images: A set of Image IDs representing the Images that this StackScript is compatible for deploying with. `any/all` indicates that all available image distributions, including private images, are accepted. Currently private image IDs are not supported.
               
               - - -
        :param pulumi.Input[bool] is_public: This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. *Changing `is_public` forces the creation of a new StackScript*
        :param pulumi.Input[str] label: The StackScript's label is for display purposes only.
        :param pulumi.Input[str] rev_note: This field allows you to add notes for the set of revisions made to this StackScript.
        :param pulumi.Input[str] script: The script to execute when provisioning a new Linode with this StackScript.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StackScriptArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Linode StackScript resource.  This can be used to create, modify, and delete Linode StackScripts.  StackScripts are private or public managed scripts which run within an instance during startup.  StackScripts can include variables whose values are specified when the Instance is created.

        For more information, see [Automate Deployment with StackScripts](https://www.linode.com/docs/platform/stackscripts/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#tag/StackScripts).

        ## Example Usage

        The following example shows how one might use this resource to configure a StackScript attached to a Linode Instance.  As shown below, StackScripts must begin with a shebang (`#!`).  The `<UDF ...>` element provided in the Bash comment block defines a variable whose value is provided when creating the Instance (or disk) using the `stackscript_data` field.

        ```python
        import pulumi
        import pulumi_linode as linode

        foo_stack_script = linode.StackScript("fooStackScript",
            label="foo",
            description="Installs a Package",
            script=\"\"\"#!/bin/bash
        # <UDF name="package" label="System Package to Install" example="nginx" default="">
        apt-get -q update && apt-get -q -y install $PACKAGE
        \"\"\",
            images=[
                "linode/ubuntu18.04",
                "linode/ubuntu16.04lts",
            ],
            rev_note="initial version")
        foo_instance = linode.Instance("fooInstance",
            image="linode/ubuntu18.04",
            label="foo",
            region="us-east",
            type="g6-nanode-1",
            authorized_keys=["..."],
            root_pass="...",
            stackscript_id=foo_stack_script.id,
            stackscript_data={
                "package": "nginx",
            })
        ```

        ## Import

        Linodes StackScripts can be imported using the Linode StackScript `id`, e.g.

        ```sh
         $ pulumi import linode:index/stackScript:StackScript mystackscript 1234567
        ```

        :param str resource_name: The name of the resource.
        :param StackScriptArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StackScriptArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 images: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_public: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 rev_note: Optional[pulumi.Input[str]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StackScriptArgs.__new__(StackScriptArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if images is None and not opts.urn:
                raise TypeError("Missing required property 'images'")
            __props__.__dict__["images"] = images
            __props__.__dict__["is_public"] = is_public
            if label is None and not opts.urn:
                raise TypeError("Missing required property 'label'")
            __props__.__dict__["label"] = label
            __props__.__dict__["rev_note"] = rev_note
            if script is None and not opts.urn:
                raise TypeError("Missing required property 'script'")
            __props__.__dict__["script"] = script
            __props__.__dict__["created"] = None
            __props__.__dict__["deployments_active"] = None
            __props__.__dict__["deployments_total"] = None
            __props__.__dict__["updated"] = None
            __props__.__dict__["user_defined_fields"] = None
            __props__.__dict__["user_gravatar_id"] = None
            __props__.__dict__["username"] = None
        super(StackScript, __self__).__init__(
            'linode:index/stackScript:StackScript',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created: Optional[pulumi.Input[str]] = None,
            deployments_active: Optional[pulumi.Input[int]] = None,
            deployments_total: Optional[pulumi.Input[int]] = None,
            description: Optional[pulumi.Input[str]] = None,
            images: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            is_public: Optional[pulumi.Input[bool]] = None,
            label: Optional[pulumi.Input[str]] = None,
            rev_note: Optional[pulumi.Input[str]] = None,
            script: Optional[pulumi.Input[str]] = None,
            updated: Optional[pulumi.Input[str]] = None,
            user_defined_fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackScriptUserDefinedFieldArgs']]]]] = None,
            user_gravatar_id: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'StackScript':
        """
        Get an existing StackScript resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created: The date this StackScript was created.
        :param pulumi.Input[int] deployments_active: Count of currently active, deployed Linodes created from this StackScript.
        :param pulumi.Input[int] deployments_total: The total number of times this StackScript has been deployed.
        :param pulumi.Input[str] description: A description for the StackScript.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] images: A set of Image IDs representing the Images that this StackScript is compatible for deploying with. `any/all` indicates that all available image distributions, including private images, are accepted. Currently private image IDs are not supported.
               
               - - -
        :param pulumi.Input[bool] is_public: This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. *Changing `is_public` forces the creation of a new StackScript*
        :param pulumi.Input[str] label: The StackScript's label is for display purposes only.
        :param pulumi.Input[str] rev_note: This field allows you to add notes for the set of revisions made to this StackScript.
        :param pulumi.Input[str] script: The script to execute when provisioning a new Linode with this StackScript.
        :param pulumi.Input[str] updated: The date this StackScript was updated.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackScriptUserDefinedFieldArgs']]]] user_defined_fields: This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized parameters during deployment.
        :param pulumi.Input[str] user_gravatar_id: The Gravatar ID for the User who created the StackScript.
        :param pulumi.Input[str] username: The User who created the StackScript.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StackScriptState.__new__(_StackScriptState)

        __props__.__dict__["created"] = created
        __props__.__dict__["deployments_active"] = deployments_active
        __props__.__dict__["deployments_total"] = deployments_total
        __props__.__dict__["description"] = description
        __props__.__dict__["images"] = images
        __props__.__dict__["is_public"] = is_public
        __props__.__dict__["label"] = label
        __props__.__dict__["rev_note"] = rev_note
        __props__.__dict__["script"] = script
        __props__.__dict__["updated"] = updated
        __props__.__dict__["user_defined_fields"] = user_defined_fields
        __props__.__dict__["user_gravatar_id"] = user_gravatar_id
        __props__.__dict__["username"] = username
        return StackScript(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        The date this StackScript was created.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="deploymentsActive")
    def deployments_active(self) -> pulumi.Output[int]:
        """
        Count of currently active, deployed Linodes created from this StackScript.
        """
        return pulumi.get(self, "deployments_active")

    @property
    @pulumi.getter(name="deploymentsTotal")
    def deployments_total(self) -> pulumi.Output[int]:
        """
        The total number of times this StackScript has been deployed.
        """
        return pulumi.get(self, "deployments_total")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A description for the StackScript.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def images(self) -> pulumi.Output[Sequence[str]]:
        """
        A set of Image IDs representing the Images that this StackScript is compatible for deploying with. `any/all` indicates that all available image distributions, including private images, are accepted. Currently private image IDs are not supported.

        - - -
        """
        return pulumi.get(self, "images")

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> pulumi.Output[bool]:
        """
        This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. *Changing `is_public` forces the creation of a new StackScript*
        """
        return pulumi.get(self, "is_public")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        """
        The StackScript's label is for display purposes only.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="revNote")
    def rev_note(self) -> pulumi.Output[str]:
        """
        This field allows you to add notes for the set of revisions made to this StackScript.
        """
        return pulumi.get(self, "rev_note")

    @property
    @pulumi.getter
    def script(self) -> pulumi.Output[str]:
        """
        The script to execute when provisioning a new Linode with this StackScript.
        """
        return pulumi.get(self, "script")

    @property
    @pulumi.getter
    def updated(self) -> pulumi.Output[str]:
        """
        The date this StackScript was updated.
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(self) -> pulumi.Output[Sequence['outputs.StackScriptUserDefinedField']]:
        """
        This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized parameters during deployment.
        """
        return pulumi.get(self, "user_defined_fields")

    @property
    @pulumi.getter(name="userGravatarId")
    def user_gravatar_id(self) -> pulumi.Output[str]:
        """
        The Gravatar ID for the User who created the StackScript.
        """
        return pulumi.get(self, "user_gravatar_id")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        The User who created the StackScript.
        """
        return pulumi.get(self, "username")

