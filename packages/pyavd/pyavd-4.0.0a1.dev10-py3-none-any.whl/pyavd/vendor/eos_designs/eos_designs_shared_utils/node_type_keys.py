from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd.vendor.j2.filter.convert_dicts import convert_dicts
from pyavd.vendor.errors import AristaAvdMissingVariableError
from pyavd.vendor.utils import get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils

DEFAULT_NODE_TYPE_KEYS = {
    "l3ls-evpn": {
        "spine": {
            "type": "spine",
            "default_evpn_role": "server",
            "default_ptp_priority1": 20,
        },
        "l3leaf": {
            "type": "l3leaf",
            "connected_endpoints": True,
            "default_evpn_role": "client",
            "mlag_support": True,
            "network_services": {
                "l2": True,
                "l3": True,
            },
            "vtep": True,
            "default_ptp_priority1": 30,
        },
        "l2leaf": {
            "type": "l2leaf",
            "connected_endpoints": True,
            "mlag_support": True,
            "network_services": {
                "l2": True,
            },
            "underlay_router": False,
            "uplink_type": "port-channel",
        },
        "super_spine": {
            "type": "super-spine",
        },
        "overlay_controller": {
            "type": "overlay-controller",
            "default_evpn_role": "server",
        },
    },
    "mpls": {
        "p": {
            "type": "p",
            "mpls_lsr": True,
            "default_mpls_overlay_role": "none",
            "default_overlay_routing_protocol": "ibgp",
            "default_underlay_routing_protocol": "isis-sr",
        },
        "pe": {
            "type": "pe",
            "mpls_lsr": True,
            "connected_endpoints": True,
            "default_mpls_overlay_role": "client",
            "default_evpn_role": "client",
            "network_services": {
                "l1": True,
                "l2": True,
                "l3": True,
            },
            "default_overlay_routing_protocol": "ibgp",
            "default_underlay_routing_protocol": "isis-sr",
            "default_overlay_address_families": ["vpn-ipv4"],
            "default_evpn_encapsulation": "mpls",
        },
        "rr": {
            "type": "rr",
            "mpls_lsr": True,
            "default_mpls_overlay_role": "server",
            "default_evpn_role": "server",
            "default_overlay_routing_protocol": "ibgp",
            "default_underlay_routing_protocol": "isis-sr",
            "default_overlay_address_families": ["vpn-ipv4"],
            "default_evpn_encapsulation": "mpls",
        },
    },
    "l2ls": {
        "l3spine": {
            "type": "l3spine",
            "connected_endpoints": True,
            "mlag_support": True,
            "network_services": {
                "l2": True,
                "l3": True,
            },
            "default_overlay_routing_protocol": "none",
            "default_underlay_routing_protocol": "none",
        },
        "spine": {
            "type": "spine",
            "connected_endpoints": True,
            "mlag_support": True,
            "network_services": {
                "l2": True,
            },
            "underlay_router": False,
            "uplink_type": "port-channel",
        },
        "leaf": {
            "type": "leaf",
            "connected_endpoints": True,
            "mlag_support": True,
            "network_services": {
                "l2": True,
            },
            "underlay_router": False,
            "uplink_type": "port-channel",
        },
    },
}


class NodeTypeKeysMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def node_type_keys(self: SharedUtils) -> list:
        """
        NOTE: This method is called _before_ any schema validation, since we need to resolve node_type_keys dynamically
        """
        design_type = get(self.hostvars, "design.type", default="l3ls-evpn")
        default_node_type_keys_for_our_design = get(DEFAULT_NODE_TYPE_KEYS, design_type)
        node_type_keys = get(self.hostvars, "node_type_keys", default=default_node_type_keys_for_our_design)
        node_type_keys = convert_dicts(node_type_keys, "key")
        return node_type_keys

    @cached_property
    def node_type_key_data(self: SharedUtils) -> dict:
        """
        node_type_key_data containing settings for this node_type.
        """
        for node_type_key in self.node_type_keys:
            if node_type_key["type"] == self.type:
                return node_type_key

        # Not found
        raise AristaAvdMissingVariableError(f"node_type_keys.[type=={self.type}]")
