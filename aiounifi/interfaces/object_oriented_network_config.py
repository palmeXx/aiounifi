"""ObjectOrientedNetworkConfig as part of a UniFi network."""

from ..models.object_oriented_network_config import ObjectOrientedNetworkConfig, ObjectOrientedNetworkConfigListRequest
from .api_handlers import APIHandler


class ObjectOrientedNetworkConfigs(APIHandler[ObjectOrientedNetworkConfig]):
    """Represents ObjectOrientedNetworkConfig configurations."""

    obj_id_key = "id"
    item_cls = ObjectOrientedNetworkConfig
    api_request = ObjectOrientedNetworkConfigListRequest.create()
