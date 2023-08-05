"""Collector Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from enum import Enum


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


class ConfigStatus(str, Enum):
    """ConfigStatus."""

    CS_NEW = "CSNew"
    CS_INFLIGHT = "CSInflight"
    CS_SUCCESS = "CSSuccess"
    CS_FAILED = "CSFailed"


class RBACObject(str, Enum):
    """RBACObject."""

    COLLECTOR = "COLLECTOR"
    COLLECTORADMIN = "COLLECTORADMIN"
    DATASOURCE = "DATASOURCE"


class RBACAction(str, Enum):
    """RBACAction."""

    READ = "READ"
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DOWNLOAD = "DOWNLOAD"
    DELETE = "DELETE"
    TAG = "TAG"
    LOGIN = "LOGIN"
    CREDENTIALS = "CREDENTIALS"
    ENDPOINTCREDENTIALS = "ENDPOINTCREDENTIALS"


class DayType(str, Enum):
    """DayType."""

    SUN = "SUN"
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THR = "THR"
    FRI = "FRI"
    SAT = "SAT"


class TimeRange(str, Enum):
    """TimeRange."""

    LASTHOUR = "LASTHOUR"
    LASTDAY = "LASTDAY"
    LAST3_DAYS = "LAST3DAYS"
    LAST7_DAYS = "LAST7DAYS"
    LAST30_DAYS = "LAST30DAYS"


class ClusterType(str, Enum):
    """ClusterType."""

    ONPREM = "ONPREM"
    CLOUD = "CLOUD"


class ImageType(str, Enum):
    """ImageType."""

    AMI = "AMI"
    VHD = "VHD"
    OVA = "OVA"
    AZURE = "AZURE"
    GCP = "GCP"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CloudRegion:
    """CloudRegion."""

    region: Optional[str] = field(default=None, metadata=config(field_name="region"))
    zones: Optional[List[str]] = field(
        default=None, metadata=config(field_name="zones")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Activation:
    """Activation."""

    code: Optional[str] = field(default=None, metadata=config(field_name="code"))
    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    region: Optional[str] = field(default=None, metadata=config(field_name="region"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Deleted:
    """Deleted."""

    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    successful: Optional[bool] = field(
        default=None, metadata=config(field_name="successful")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UpdateDeploymentInput:
    """UpdateDeploymentInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    version: Optional[str] = field(default=None, metadata=config(field_name="version"))
    config_: Optional[dict] = field(default=None, metadata=config(field_name="config"))
    alertable: Optional[bool] = field(
        default=None, metadata=config(field_name="alertable")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EndpointInput:
    """EndpointInput."""

    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    address: Optional[str] = field(default=None, metadata=config(field_name="address"))
    port: Optional[int] = field(default=None, metadata=config(field_name="port"))
    credentials: Optional[Any] = field(
        default=None, metadata=config(field_name="credentials")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ValidityPeriod:
    """ValidityPeriod."""

    from_: Optional[int] = field(default=None, metadata=config(field_name="from"))
    until: Optional[int] = field(default=None, metadata=config(field_name="until"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Image:
    """Image."""

    location: Optional[str] = field(
        default=None, metadata=config(field_name="location")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Registration:
    """Registration."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    region: Optional[str] = field(default=None, metadata=config(field_name="region"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RegistrationInput:
    """RegistrationInput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    region: Optional[str] = field(default=None, metadata=config(field_name="region"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Network:
    """Network."""

    dhcp: Optional[bool] = field(default=None, metadata=config(field_name="dhcp"))
    hostname: Optional[str] = field(
        default=None, metadata=config(field_name="hostname")
    )
    hosts: Optional[dict] = field(default=None, metadata=config(field_name="hosts"))
    address: Optional[str] = field(default=None, metadata=config(field_name="address"))
    mask: Optional[str] = field(default=None, metadata=config(field_name="mask"))
    gateway: Optional[str] = field(default=None, metadata=config(field_name="gateway"))
    dns: Optional[str] = field(default=None, metadata=config(field_name="dns"))
    ntp: Optional[str] = field(default=None, metadata=config(field_name="ntp"))
    proxy: Optional[str] = field(default=None, metadata=config(field_name="proxy"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class HostsInput:
    """HostsInput."""

    address: Optional[str] = field(default=None, metadata=config(field_name="address"))
    hostname: Optional[str] = field(
        default=None, metadata=config(field_name="hostname")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Status:
    """Status."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    status: Optional[dict] = field(default=None, metadata=config(field_name="status"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class StatusInput:
    """StatusInput."""

    deployment_id: Optional[str] = field(
        default=None, metadata=config(field_name="deploymentID")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    status: Optional[dict] = field(default=None, metadata=config(field_name="status"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ChartList:
    """ChartList."""

    api_version: Optional[str] = field(
        default=None, metadata=config(field_name="APIVersion")
    )
    entries: Optional[Any] = field(default=None, metadata=config(field_name="Entries"))
    generated: Optional[str] = field(
        default=None, metadata=config(field_name="Generated")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Chart:
    """Chart."""

    api_version: Optional[str] = field(
        default=None, metadata=config(field_name="apiVersion")
    )
    app_version: Optional[str] = field(
        default=None, metadata=config(field_name="appVersion")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    icon: Optional[str] = field(default=None, metadata=config(field_name="icon"))
    home: Optional[str] = field(default=None, metadata=config(field_name="home"))
    keywords: Optional[List[str]] = field(
        default=None, metadata=config(field_name="keywords")
    )
    annotations: Optional[dict] = field(
        default=None, metadata=config(field_name="annotations")
    )
    version: Optional[str] = field(default=None, metadata=config(field_name="version"))
    digest: Optional[str] = field(default=None, metadata=config(field_name="digest"))
    urls: Optional[List[str]] = field(default=None, metadata=config(field_name="urls"))
    meta_data: Optional[Any] = field(
        default=None, metadata=config(field_name="metaData")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class BillOfMaterials:
    """BillOfMaterials."""

    location: Optional[str] = field(
        default=None, metadata=config(field_name="location")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Credentials:
    """Credentials."""

    password: Optional[str] = field(
        default=None, metadata=config(field_name="password")
    )
    private_key: Optional[str] = field(
        default=None, metadata=config(field_name="privateKey")
    )
    public_key: Optional[str] = field(
        default=None, metadata=config(field_name="publicKey")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CollectorMetrics:
    """CollectorMetrics."""

    last_seen: Optional[Any] = field(
        default=None, metadata=config(field_name="lastSeen")
    )
    average_rate: Optional[Any] = field(
        default=None, metadata=config(field_name="averageRate")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AggregateRateByCollector:
    """AggregateRateByCollector."""

    aggregate_rate: Optional[Any] = field(
        default=None, metadata=config(field_name="aggregateRate")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FlowRate:
    """FlowRate."""

    per_flow_max: Optional[Any] = field(
        default=None, metadata=config(field_name="perFlowMax")
    )
    per_flow_average: Optional[Any] = field(
        default=None, metadata=config(field_name="perFlowAverage")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class LogLastSeenMetric:
    """LogLastSeenMetric."""

    cluster_id: Optional[str] = field(
        default=None, metadata=config(field_name="clusterID")
    )
    cluster_name: Optional[str] = field(
        default=None, metadata=config(field_name="clusterName")
    )
    source_id: Optional[str] = field(
        default=None, metadata=config(field_name="sourceID")
    )
    aliases: Optional[List[str]] = field(
        default=None, metadata=config(field_name="aliases")
    )
    service: Optional[str] = field(default=None, metadata=config(field_name="service"))
    sensor_type: Optional[str] = field(
        default=None, metadata=config(field_name="sensorType")
    )
    last_seen: Optional[str] = field(
        default=None, metadata=config(field_name="lastSeen")
    )
    health: Optional[str] = field(default=None, metadata=config(field_name="health"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DataSourceMetric:
    """DataSourceMetric."""

    cluster_id: Optional[str] = field(
        default=None, metadata=config(field_name="clusterID")
    )
    cluster_name: Optional[str] = field(
        default=None, metadata=config(field_name="clusterName")
    )
    source_id: Optional[str] = field(
        default=None, metadata=config(field_name="sourceID")
    )
    aliases: Optional[List[str]] = field(
        default=None, metadata=config(field_name="aliases")
    )
    service: Optional[str] = field(default=None, metadata=config(field_name="service"))
    sensor_types: Optional[List[str]] = field(
        default=None, metadata=config(field_name="sensorTypes")
    )
    last_seen: Optional[str] = field(
        default=None, metadata=config(field_name="lastSeen")
    )
    health: Optional[str] = field(default=None, metadata=config(field_name="health"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SyslogMessageCountV2:
    """SyslogMessageCountV2."""

    source_id: Optional[str] = field(
        default=None, metadata=config(field_name="sourceID")
    )
    schema_: Optional[str] = field(default=None, metadata=config(field_name="schema"))
    sensor_types: Optional[List[str]] = field(
        default=None, metadata=config(field_name="sensorTypes")
    )
    services: Optional[List[str]] = field(
        default=None, metadata=config(field_name="services")
    )
    collectors: Optional[List[str]] = field(
        default=None, metadata=config(field_name="collectors")
    )
    count: Optional[int] = field(default=None, metadata=config(field_name="count"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AWSDetails:
    """AWSDetails."""

    account_id: Optional[str] = field(
        default=None, metadata=config(field_name="accountID")
    )
    region: Optional[str] = field(default=None, metadata=config(field_name="region"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AWSDetailsV2:
    """AWSDetailsV2."""

    account_id: Optional[int] = field(
        default=None, metadata=config(field_name="accountID")
    )
    region: Optional[str] = field(default=None, metadata=config(field_name="region"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class GCPDetails:
    """GCPDetails."""

    agent_id: Optional[str] = field(default=None, metadata=config(field_name="agentId"))
    cidr: Optional[str] = field(default=None, metadata=config(field_name="cidr"))
    gcp_project: Optional[str] = field(
        default=None, metadata=config(field_name="gcpProject")
    )
    network: Optional[str] = field(default=None, metadata=config(field_name="network"))
    region: Optional[str] = field(default=None, metadata=config(field_name="region"))
    subnet: Optional[str] = field(default=None, metadata=config(field_name="subnet"))
    zone: Optional[str] = field(default=None, metadata=config(field_name="zone"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class GCPDetailsV2:
    """GCPDetailsV2."""

    agent_id: Optional[str] = field(default=None, metadata=config(field_name="agentId"))
    cidr: Optional[str] = field(default=None, metadata=config(field_name="cidr"))
    gcp_project: Optional[str] = field(
        default=None, metadata=config(field_name="gcpProject")
    )
    network: Optional[str] = field(default=None, metadata=config(field_name="network"))
    region: Optional[str] = field(default=None, metadata=config(field_name="region"))
    subnet: Optional[str] = field(default=None, metadata=config(field_name="subnet"))
    zone: Optional[str] = field(default=None, metadata=config(field_name="zone"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class GetDataSourceMetricsArguments:
    """GetDataSourceMetricsArguments."""

    cluster_id: Optional[str] = field(
        default=None, metadata=config(field_name="clusterId")
    )
    source_id: Optional[str] = field(
        default=None, metadata=config(field_name="sourceId")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SyslogMessageCountV2Arguments:
    """SyslogMessageCountV2Arguments."""

    source_id: Optional[str] = field(
        default=None, metadata=config(field_name="sourceId")
    )
    cluster_id: Optional[str] = field(
        default=None, metadata=config(field_name="clusterId")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class OSConfig:
    """OSConfig."""

    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    cluster_id: Optional[str] = field(
        default=None, metadata=config(field_name="clusterID")
    )
    node_name: Optional[str] = field(
        default=None, metadata=config(field_name="nodeName")
    )
    status_message: Optional[str] = field(
        default=None, metadata=config(field_name="statusMessage")
    )
    dhcp: Optional[bool] = field(default=None, metadata=config(field_name="dhcp"))
    hostname: Optional[str] = field(
        default=None, metadata=config(field_name="hostname")
    )
    hosts: Optional[dict] = field(default=None, metadata=config(field_name="hosts"))
    address: Optional[str] = field(default=None, metadata=config(field_name="address"))
    mask: Optional[str] = field(default=None, metadata=config(field_name="mask"))
    gateway: Optional[str] = field(default=None, metadata=config(field_name="gateway"))
    dns: Optional[str] = field(default=None, metadata=config(field_name="dns"))
    ntp: Optional[str] = field(default=None, metadata=config(field_name="ntp"))
    proxy: Optional[str] = field(default=None, metadata=config(field_name="proxy"))
    status: Optional[ConfigStatus] = field(
        default=None, metadata=config(field_name="status")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MaintenanceInput:
    """MaintenanceInput."""

    start_hour: Optional[int] = field(
        default=None, metadata=config(field_name="startHour")
    )
    duration: Optional[int] = field(
        default=None, metadata=config(field_name="duration")
    )
    day: Optional[DayType] = field(default=None, metadata=config(field_name="day"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DeploymentInput:
    """DeploymentInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    chart: Optional[str] = field(default=None, metadata=config(field_name="chart"))
    version: Optional[str] = field(default=None, metadata=config(field_name="version"))
    config_: Optional[dict] = field(default=None, metadata=config(field_name="config"))
    alertable: Optional[bool] = field(
        default=None, metadata=config(field_name="alertable")
    )
    endpoints: Optional[List[EndpointInput]] = field(
        default=None, metadata=config(field_name="endpoints")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Endpoint:
    """Endpoint."""

    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    address: Optional[str] = field(default=None, metadata=config(field_name="address"))
    port: Optional[int] = field(default=None, metadata=config(field_name="port"))
    credentials: Optional[Any] = field(
        default=None, metadata=config(field_name="credentials")
    )
    validity: Optional[ValidityPeriod] = field(
        default=None, metadata=config(field_name="validity")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NetworkInput:
    """NetworkInput."""

    dhcp: Optional[bool] = field(default=None, metadata=config(field_name="dhcp"))
    hostname: Optional[str] = field(
        default=None, metadata=config(field_name="hostname")
    )
    address: Optional[str] = field(default=None, metadata=config(field_name="address"))
    mask: Optional[str] = field(default=None, metadata=config(field_name="mask"))
    gateway: Optional[str] = field(default=None, metadata=config(field_name="gateway"))
    dns: Optional[List[str]] = field(default=None, metadata=config(field_name="dns"))
    ntp: Optional[List[str]] = field(default=None, metadata=config(field_name="ntp"))
    proxy: Optional[str] = field(default=None, metadata=config(field_name="proxy"))
    hosts: Optional[List[HostsInput]] = field(
        default=None, metadata=config(field_name="hosts")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class LogLastSeenMetrics:
    """LogLastSeenMetrics."""

    log_metrics: Optional[List[LogLastSeenMetric]] = field(
        default=None, metadata=config(field_name="logMetrics")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DataSourceMetrics:
    """DataSourceMetrics."""

    metrics: Optional[List[DataSourceMetric]] = field(
        default=None, metadata=config(field_name="metrics")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ClusterNode:
    """ClusterNode."""

    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    health: Optional[str] = field(default=None, metadata=config(field_name="health"))
    host: Optional[str] = field(default=None, metadata=config(field_name="host"))
    network: Optional[Network] = field(
        default=None, metadata=config(field_name="network")
    )
    registration: Optional[Registration] = field(
        default=None, metadata=config(field_name="registration")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class OSConfigInput:
    """OSConfigInput."""

    cluster_id: Optional[str] = field(
        default=None, metadata=config(field_name="clusterID")
    )
    node_name: Optional[str] = field(
        default=None, metadata=config(field_name="nodeName")
    )
    status_message: Optional[str] = field(
        default=None, metadata=config(field_name="statusMessage")
    )
    dhcp: Optional[bool] = field(default=None, metadata=config(field_name="dhcp"))
    hostname: Optional[str] = field(
        default=None, metadata=config(field_name="hostname")
    )
    address: Optional[str] = field(default=None, metadata=config(field_name="address"))
    mask: Optional[str] = field(default=None, metadata=config(field_name="mask"))
    gateway: Optional[str] = field(default=None, metadata=config(field_name="gateway"))
    dns: Optional[List[str]] = field(default=None, metadata=config(field_name="dns"))
    ntp: Optional[List[str]] = field(default=None, metadata=config(field_name="ntp"))
    proxy: Optional[str] = field(default=None, metadata=config(field_name="proxy"))
    status: Optional[ConfigStatus] = field(
        default=None, metadata=config(field_name="status")
    )
    hosts: Optional[List[HostsInput]] = field(
        default=None, metadata=config(field_name="hosts")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ClusterNodeInput:
    """ClusterNodeInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    host: Optional[str] = field(default=None, metadata=config(field_name="host"))
    network: Optional[NetworkInput] = field(
        default=None, metadata=config(field_name="network")
    )
    registration: Optional[RegistrationInput] = field(
        default=None, metadata=config(field_name="registration")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Deployment:
    """Deployment."""

    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    role: Optional[str] = field(default=None, metadata=config(field_name="role"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    chart: Optional[str] = field(default=None, metadata=config(field_name="chart"))
    version: Optional[str] = field(default=None, metadata=config(field_name="version"))
    config_: Optional[dict] = field(default=None, metadata=config(field_name="config"))
    alertable: Optional[bool] = field(
        default=None, metadata=config(field_name="alertable")
    )
    status: Optional[Status] = field(default=None, metadata=config(field_name="status"))
    endpoints: Optional[List[Endpoint]] = field(
        default=None, metadata=config(field_name="endpoints")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ClusterImageInput:
    """ClusterImageInput."""

    cluster_id: Optional[str] = field(
        default=None, metadata=config(field_name="clusterID")
    )
    launch_console: Optional[bool] = field(
        default=None, metadata=config(field_name="launchConsole")
    )
    image_type: Optional[ImageType] = field(
        default=None, metadata=config(field_name="imageType")
    )
    aws_details: Optional[AWSDetailsV2] = field(
        default=None, metadata=config(field_name="awsDetails")
    )
    gcp_details: Optional[GCPDetailsV2] = field(
        default=None, metadata=config(field_name="gcpDetails")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ClusterInput:
    """ClusterInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    role: Optional[str] = field(default=None, metadata=config(field_name="role"))
    is_ha: Optional[bool] = field(default=None, metadata=config(field_name="isHa"))
    ha_cidr_block: Optional[str] = field(
        default=None, metadata=config(field_name="haCidrBlock")
    )
    ha_cidr_block_array: Optional[List[str]] = field(
        default=None, metadata=config(field_name="haCidrBlockArray")
    )
    network: Optional[NetworkInput] = field(
        default=None, metadata=config(field_name="network")
    )
    cluster_type: Optional[ClusterType] = field(
        default=None, metadata=config(field_name="clusterType")
    )
    registration: Optional[RegistrationInput] = field(
        default=None, metadata=config(field_name="registration")
    )
    maintenance: Optional[MaintenanceInput] = field(
        default=None, metadata=config(field_name="maintenance")
    )
    cluster_nodes: Optional[List[ClusterNodeInput]] = field(
        default=None, metadata=config(field_name="clusterNodes")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class HAStaticClusterInput:
    """HAStaticClusterInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    role: Optional[str] = field(default=None, metadata=config(field_name="role"))
    ha_cidr_block: Optional[str] = field(
        default=None, metadata=config(field_name="haCidrBlock")
    )
    ha_cidr_block_array: Optional[List[str]] = field(
        default=None, metadata=config(field_name="haCidrBlockArray")
    )
    network: Optional[NetworkInput] = field(
        default=None, metadata=config(field_name="network")
    )
    cluster_type: Optional[ClusterType] = field(
        default=None, metadata=config(field_name="clusterType")
    )
    registration: Optional[RegistrationInput] = field(
        default=None, metadata=config(field_name="registration")
    )
    maintenance: Optional[MaintenanceInput] = field(
        default=None, metadata=config(field_name="maintenance")
    )
    cluster_nodes: Optional[List[ClusterNodeInput]] = field(
        default=None, metadata=config(field_name="clusterNodes")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Cluster:
    """Cluster."""

    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    role: Optional[str] = field(default=None, metadata=config(field_name="role"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    health: Optional[str] = field(default=None, metadata=config(field_name="health"))
    health_state: Optional[str] = field(
        default=None, metadata=config(field_name="healthState")
    )
    maintenance_start_hour: Optional[int] = field(
        default=None, metadata=config(field_name="maintenanceStartHour")
    )
    maintenance_duration: Optional[int] = field(
        default=None, metadata=config(field_name="maintenanceDuration")
    )
    is_ha: Optional[bool] = field(default=None, metadata=config(field_name="isHa"))
    ha_cidr_block: Optional[str] = field(
        default=None, metadata=config(field_name="haCidrBlock")
    )
    cluster_type: Optional[ClusterType] = field(
        default=None, metadata=config(field_name="clusterType")
    )
    network: Optional[Network] = field(
        default=None, metadata=config(field_name="network")
    )
    deployments: Optional[List[Deployment]] = field(
        default=None, metadata=config(field_name="deployments")
    )
    status: Optional[List[Status]] = field(
        default=None, metadata=config(field_name="status")
    )
    registration: Optional[Registration] = field(
        default=None, metadata=config(field_name="registration")
    )
    maintenance_day: Optional[DayType] = field(
        default=None, metadata=config(field_name="maintenanceDay")
    )
    cluster_nodes: Optional[List[ClusterNode]] = field(
        default=None, metadata=config(field_name="clusterNodes")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CollectorOverview:
    """CollectorOverview."""

    last_seen: Optional[Any] = field(
        default=None, metadata=config(field_name="lastSeen")
    )
    average_rate: Optional[Any] = field(
        default=None, metadata=config(field_name="averageRate")
    )
    cluster: Optional[Cluster] = field(
        default=None, metadata=config(field_name="cluster")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class System:
    """System."""

    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    id: Optional[int] = field(default=None, metadata=config(field_name="id"))
    deployments: Optional[List[Deployment]] = field(
        default=None, metadata=config(field_name="deployments")
    )
