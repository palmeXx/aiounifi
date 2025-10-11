"""ObjectOrientedNetwork Config as part of a UniFi network."""

from dataclasses import dataclass
from typing import NotRequired, Self, TypedDict

from .api import ApiItem, ApiRequestV2

class ObjectOrientedNetworkConfigLimit(TypedDict):
    """Limit for ObjectOrientedNetwork config."""

    enabled: bool
    burst: str
    limit: int

class ObjectOrientedNetworkConfigApps(TypedDict):
    """Apps for ObjectOrientedNetwork config."""

    enabled: bool
    values: list[int]

class ObjectOrientedNetworkConfigDomains(TypedDict):
    """Domains for ObjectOrientedNetwork config."""

    enabled: bool
    values: list[str]

class ObjectOrientedNetworkConfigIpAddresses(TypedDict):
    """Ip addresses for ObjectOrientedNetwork config."""

    enabled: bool
    values: list[str]

class ObjectOrientedNetworkConfigRegions(TypedDict):
    """Region for ObjectOrientedNetwork config."""

    enabled: bool
    values: list[str]

class ObjectOrientedNetworkConfigSchedule(TypedDict):
    """Schedule for ObjectOrientedNetwork config."""

    mode: str
    time_range_start: NotRequired[str]
    time_range_end: NotRequired[str]

class ObjectOrientedNetworkConfigQos(TypedDict):
    """QOS settings for ObjectOrientedNetwork config."""

    enabled: bool
    all_traffic: bool
    mode: str
    schedule: ObjectOrientedNetworkConfigSchedule
    download_limit: ObjectOrientedNetworkConfigLimit
    upload_limit: ObjectOrientedNetworkConfigLimit

    apps: ObjectOrientedNetworkConfigApps
    domains: ObjectOrientedNetworkConfigDomains
    ip_addresses: ObjectOrientedNetworkConfigIpAddresses
    regions: ObjectOrientedNetworkConfigRegions


class ObjectOrientedNetworkConfigRoute(TypedDict):
    """Route settings for ObjectOrientedNetwork config."""

    enabled: bool
    all_traffic: NotRequired[bool]

    apps: ObjectOrientedNetworkConfigApps
    domains: ObjectOrientedNetworkConfigDomains
    ip_addresses: ObjectOrientedNetworkConfigIpAddresses
    regions: ObjectOrientedNetworkConfigRegions

class ObjectOrientedNetworkConfigSecureZone(TypedDict):
    """Internet for ObjectOrientedNetwork config."""

    everything: bool
    mode: str
    schedule: ObjectOrientedNetworkConfigSchedule

    apps: ObjectOrientedNetworkConfigApps
    domains: ObjectOrientedNetworkConfigDomains
    ip_addresses: ObjectOrientedNetworkConfigIpAddresses
    regions: ObjectOrientedNetworkConfigRegions

class ObjectOrientedNetworkConfigSecure(TypedDict):
    """Secure settings for ObjectOrientedNetwork config."""

    enabled: bool
    internet: NotRequired[ObjectOrientedNetworkConfigSecureZone]
    local: NotRequired[ObjectOrientedNetworkConfigSecureZone]

class TypedObjectOrientedNetworkConfig(TypedDict):
    """ObjectOrientedNetwork Config type definition."""

    enabled: bool
    id: str
    name: str
    qos: ObjectOrientedNetworkConfigQos
    route: ObjectOrientedNetworkConfigRoute
    secure: ObjectOrientedNetworkConfigSecure
    target_type: str
    targets: list[str]


class ObjectOrientedNetworkConfig(ApiItem):
    """Represent a ObjectOrientedNetwork config."""

    raw: TypedObjectOrientedNetworkConfig

    @property
    def enabled(self) -> bool:
        """ObjectOrientedNetwork config is enabled."""
        return self.raw["enabled"]

    @enabled.setter
    def enabled(self, value: bool) -> None:
        """Set enabled status of ObjectOrientedNetwork config."""
        self.raw["enabled"] = value

    @property
    def id(self) -> str:
        """Unique ID of ObjectOrientedNetwork config."""
        return self.raw["id"]

    @property
    def name(self) -> str:
        """ObjectOrientedNetwork config name."""
        return self.raw["name"]

    @property
    def target_type(self) -> str:
        """Target type of ObjectOrientedNetwork config"""
        return self.raw["target_type"]

    @property
    def targets(self) -> list[str]:
        """Targets oof ObjectOrientedNetwork config."""
        return self.raw["targets"]

    @property
    def qos(self) -> ObjectOrientedNetworkConfigQos:
        """QOS Definition of ObjectOrientedNetwork config."""
        return self.raw["qos"]

    @property
    def route(self) -> ObjectOrientedNetworkConfigRoute:
        """Route Definition of ObjectOrientedNetwork config."""
        return self.raw.get("route")

    @property
    def secure(self) -> ObjectOrientedNetworkConfigSecure:
        """Secure Definition of ObjectOrientedNetwork config."""
        return self.raw.get("secure")


@dataclass
class ObjectOrientedNetworkConfigListRequest(ApiRequestV2):
    """Request object for listing ObjectOrientedNetwork configs."""

    @classmethod
    def create(cls) -> Self:
        """Create ObjectOrientedNetwork config list request."""
        return cls(
            method="get", 
            path="/object-oriented-network-configs", 
            data=None)

@dataclass
class ObjectOrientedNetworkConfigUpdateRequest(ApiRequestV2):
    """Request object for updating a ObjectOrientedNetwork config."""

    @classmethod
    def create(cls, oonc: TypedObjectOrientedNetworkConfig) -> Self:
        """Create ObjectOrientedNetwork config update request."""
        return cls(
            method="put",
            path=f"/object-oriented-network-config/{oonc['id']}",
            data=oonc,
        )
