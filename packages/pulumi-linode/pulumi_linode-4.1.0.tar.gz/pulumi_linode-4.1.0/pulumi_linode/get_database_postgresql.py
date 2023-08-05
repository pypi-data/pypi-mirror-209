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

__all__ = [
    'GetDatabasePostgresqlResult',
    'AwaitableGetDatabasePostgresqlResult',
    'get_database_postgresql',
    'get_database_postgresql_output',
]

@pulumi.output_type
class GetDatabasePostgresqlResult:
    """
    A collection of values returned by getDatabasePostgresql.
    """
    def __init__(__self__, allow_lists=None, ca_cert=None, cluster_size=None, created=None, database_id=None, encrypted=None, engine=None, engine_id=None, host_primary=None, host_secondary=None, id=None, label=None, port=None, region=None, replication_commit_type=None, replication_type=None, root_password=None, root_username=None, ssl_connection=None, status=None, type=None, updated=None, updates=None, version=None):
        if allow_lists and not isinstance(allow_lists, list):
            raise TypeError("Expected argument 'allow_lists' to be a list")
        pulumi.set(__self__, "allow_lists", allow_lists)
        if ca_cert and not isinstance(ca_cert, str):
            raise TypeError("Expected argument 'ca_cert' to be a str")
        pulumi.set(__self__, "ca_cert", ca_cert)
        if cluster_size and not isinstance(cluster_size, int):
            raise TypeError("Expected argument 'cluster_size' to be a int")
        pulumi.set(__self__, "cluster_size", cluster_size)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if database_id and not isinstance(database_id, int):
            raise TypeError("Expected argument 'database_id' to be a int")
        pulumi.set(__self__, "database_id", database_id)
        if encrypted and not isinstance(encrypted, bool):
            raise TypeError("Expected argument 'encrypted' to be a bool")
        pulumi.set(__self__, "encrypted", encrypted)
        if engine and not isinstance(engine, str):
            raise TypeError("Expected argument 'engine' to be a str")
        pulumi.set(__self__, "engine", engine)
        if engine_id and not isinstance(engine_id, str):
            raise TypeError("Expected argument 'engine_id' to be a str")
        pulumi.set(__self__, "engine_id", engine_id)
        if host_primary and not isinstance(host_primary, str):
            raise TypeError("Expected argument 'host_primary' to be a str")
        pulumi.set(__self__, "host_primary", host_primary)
        if host_secondary and not isinstance(host_secondary, str):
            raise TypeError("Expected argument 'host_secondary' to be a str")
        pulumi.set(__self__, "host_secondary", host_secondary)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if replication_commit_type and not isinstance(replication_commit_type, str):
            raise TypeError("Expected argument 'replication_commit_type' to be a str")
        pulumi.set(__self__, "replication_commit_type", replication_commit_type)
        if replication_type and not isinstance(replication_type, str):
            raise TypeError("Expected argument 'replication_type' to be a str")
        pulumi.set(__self__, "replication_type", replication_type)
        if root_password and not isinstance(root_password, str):
            raise TypeError("Expected argument 'root_password' to be a str")
        pulumi.set(__self__, "root_password", root_password)
        if root_username and not isinstance(root_username, str):
            raise TypeError("Expected argument 'root_username' to be a str")
        pulumi.set(__self__, "root_username", root_username)
        if ssl_connection and not isinstance(ssl_connection, bool):
            raise TypeError("Expected argument 'ssl_connection' to be a bool")
        pulumi.set(__self__, "ssl_connection", ssl_connection)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        pulumi.set(__self__, "updated", updated)
        if updates and not isinstance(updates, list):
            raise TypeError("Expected argument 'updates' to be a list")
        pulumi.set(__self__, "updates", updates)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="allowLists")
    def allow_lists(self) -> Sequence[str]:
        """
        A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.
        """
        return pulumi.get(self, "allow_lists")

    @property
    @pulumi.getter(name="caCert")
    def ca_cert(self) -> str:
        """
        The base64-encoded SSL CA certificate for the Managed Database instance.
        """
        return pulumi.get(self, "ca_cert")

    @property
    @pulumi.getter(name="clusterSize")
    def cluster_size(self) -> int:
        """
        The number of Linode Instance nodes deployed to the Managed Database.
        """
        return pulumi.get(self, "cluster_size")

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        When this Managed Database was created.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> int:
        return pulumi.get(self, "database_id")

    @property
    @pulumi.getter
    def encrypted(self) -> bool:
        """
        Whether the Managed Databases is encrypted.
        """
        return pulumi.get(self, "encrypted")

    @property
    @pulumi.getter
    def engine(self) -> str:
        """
        The Managed Database engine. (e.g. `postgresql`)
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> str:
        """
        The Managed Database engine in engine/version format. (e.g. `postgresql/13.2`)
        """
        return pulumi.get(self, "engine_id")

    @property
    @pulumi.getter(name="hostPrimary")
    def host_primary(self) -> str:
        """
        The primary host for the Managed Database.
        """
        return pulumi.get(self, "host_primary")

    @property
    @pulumi.getter(name="hostSecondary")
    def host_secondary(self) -> str:
        """
        The secondary/private network host for the Managed Database.
        """
        return pulumi.get(self, "host_secondary")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def label(self) -> str:
        """
        A unique, user-defined string referring to the Managed Database.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def port(self) -> int:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region that hosts this Linode Managed Database.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="replicationCommitType")
    def replication_commit_type(self) -> str:
        """
        (Optional) The synchronization level of the replicating server. (`on`, `local`, `remote_write`, `remote_apply`, `off`)
        """
        return pulumi.get(self, "replication_commit_type")

    @property
    @pulumi.getter(name="replicationType")
    def replication_type(self) -> str:
        """
        The replication method used for the Managed Database. (`none`, `asynch`, `semi_synch`)
        """
        return pulumi.get(self, "replication_type")

    @property
    @pulumi.getter(name="rootPassword")
    def root_password(self) -> str:
        """
        The randomly-generated root password for the Managed Database instance.
        """
        return pulumi.get(self, "root_password")

    @property
    @pulumi.getter(name="rootUsername")
    def root_username(self) -> str:
        """
        The root username for the Managed Database instance.
        """
        return pulumi.get(self, "root_username")

    @property
    @pulumi.getter(name="sslConnection")
    def ssl_connection(self) -> bool:
        """
        Whether to require SSL credentials to establish a connection to the Managed Database.
        """
        return pulumi.get(self, "ssl_connection")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The operating status of the Managed Database.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The Linode Instance type used for the nodes of the  Managed Database instance.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def updated(self) -> str:
        """
        When this Managed Database was last updated.
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter
    def updates(self) -> Sequence['outputs.GetDatabasePostgresqlUpdateResult']:
        return pulumi.get(self, "updates")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The Managed Database engine version. (e.g. `v8.0.26`)
        """
        return pulumi.get(self, "version")


class AwaitableGetDatabasePostgresqlResult(GetDatabasePostgresqlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabasePostgresqlResult(
            allow_lists=self.allow_lists,
            ca_cert=self.ca_cert,
            cluster_size=self.cluster_size,
            created=self.created,
            database_id=self.database_id,
            encrypted=self.encrypted,
            engine=self.engine,
            engine_id=self.engine_id,
            host_primary=self.host_primary,
            host_secondary=self.host_secondary,
            id=self.id,
            label=self.label,
            port=self.port,
            region=self.region,
            replication_commit_type=self.replication_commit_type,
            replication_type=self.replication_type,
            root_password=self.root_password,
            root_username=self.root_username,
            ssl_connection=self.ssl_connection,
            status=self.status,
            type=self.type,
            updated=self.updated,
            updates=self.updates,
            version=self.version)


def get_database_postgresql(database_id: Optional[int] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabasePostgresqlResult:
    """
    Provides information about a Linode PostgreSQL Database.

    ## Example Usage

    Get information about a PostgreSQL database:

    ```python
    import pulumi
    import pulumi_linode as linode

    my_db = linode.get_database_postgresql(database_id=12345)
    ```
    ## updates

    The following arguments are exported by the `updates` specification block:

    * `day_of_week` - The day to perform maintenance. (`monday`, `tuesday`, ...)

    * `duration` - The maximum maintenance window time in hours. (`1`..`3`)

    * `frequency` - Whether maintenance occurs on a weekly or monthly basis. (`weekly`, `monthly`)

    * `hour_of_day` - The hour to begin maintenance based in UTC time. (`0`..`23`)

    * `week_of_month` - The week of the month to perform monthly frequency updates. Required for `monthly` frequency updates. (`1`..`4`)


    :param int database_id: The ID of the PostgreSQL database.
    """
    __args__ = dict()
    __args__['databaseId'] = database_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('linode:index/getDatabasePostgresql:getDatabasePostgresql', __args__, opts=opts, typ=GetDatabasePostgresqlResult).value

    return AwaitableGetDatabasePostgresqlResult(
        allow_lists=__ret__.allow_lists,
        ca_cert=__ret__.ca_cert,
        cluster_size=__ret__.cluster_size,
        created=__ret__.created,
        database_id=__ret__.database_id,
        encrypted=__ret__.encrypted,
        engine=__ret__.engine,
        engine_id=__ret__.engine_id,
        host_primary=__ret__.host_primary,
        host_secondary=__ret__.host_secondary,
        id=__ret__.id,
        label=__ret__.label,
        port=__ret__.port,
        region=__ret__.region,
        replication_commit_type=__ret__.replication_commit_type,
        replication_type=__ret__.replication_type,
        root_password=__ret__.root_password,
        root_username=__ret__.root_username,
        ssl_connection=__ret__.ssl_connection,
        status=__ret__.status,
        type=__ret__.type,
        updated=__ret__.updated,
        updates=__ret__.updates,
        version=__ret__.version)


@_utilities.lift_output_func(get_database_postgresql)
def get_database_postgresql_output(database_id: Optional[pulumi.Input[int]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabasePostgresqlResult]:
    """
    Provides information about a Linode PostgreSQL Database.

    ## Example Usage

    Get information about a PostgreSQL database:

    ```python
    import pulumi
    import pulumi_linode as linode

    my_db = linode.get_database_postgresql(database_id=12345)
    ```
    ## updates

    The following arguments are exported by the `updates` specification block:

    * `day_of_week` - The day to perform maintenance. (`monday`, `tuesday`, ...)

    * `duration` - The maximum maintenance window time in hours. (`1`..`3`)

    * `frequency` - Whether maintenance occurs on a weekly or monthly basis. (`weekly`, `monthly`)

    * `hour_of_day` - The hour to begin maintenance based in UTC time. (`0`..`23`)

    * `week_of_month` - The week of the month to perform monthly frequency updates. Required for `monthly` frequency updates. (`1`..`4`)


    :param int database_id: The ID of the PostgreSQL database.
    """
    ...
