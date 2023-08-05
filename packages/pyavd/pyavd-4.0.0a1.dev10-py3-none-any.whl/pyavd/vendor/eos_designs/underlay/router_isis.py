from __future__ import annotations

from functools import cached_property

from pyavd.vendor.errors import AristaAvdMissingVariableError
from pyavd.vendor.utils import default, get

from .utils import UtilsMixin


class RouterIsisMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_isis(self) -> dict | None:
        """
        return structured config for router_isis
        """
        if self.shared_utils.underlay_isis is not True:
            return None

        router_isis = {
            "instance": self.shared_utils.isis_instance_name,
            "log_adjacency_changes": True,
            "net": self._isis_net,
            "router_id": self.shared_utils.router_id,
            "is_type": self._is_type,
            "address_family": ["ipv4 unicast"],
            "isis_af_defaults": [f"maximum-paths {get(self._hostvars, 'isis_maximum_paths', default=4)}"],
        }

        # no passive interfaces
        no_passive_interfaces = [link["interface"] for link in self._underlay_links if link["type"] == "underlay_p2p"]

        if self.shared_utils.mlag_l3:
            mlag_l3_vlan = default(self.shared_utils.mlag_peer_l3_vlan, self.shared_utils.mlag_peer_vlan)
            no_passive_interfaces.append(f"Vlan{mlag_l3_vlan}")

        if self.shared_utils.overlay_vtep is True:
            no_passive_interfaces.append(self.shared_utils.vtep_loopback)

        if no_passive_interfaces:
            router_isis["no_passive_interfaces"] = no_passive_interfaces

        if self.shared_utils.underlay_ldp is True:
            router_isis["mpls_ldp_sync_default"] = True

        # TI-LFA
        if get(self._hostvars, "isis_ti_lfa.enabled") is True:
            router_isis["timers"] = {
                "local_convergence": {
                    "delay": get(self._hostvars, "isis_ti_lfa.local_convergence_delay", default="10000"),
                    "protected_prefixes": True,
                }
            }
        ti_lfa_protection = get(self._hostvars, "isis_ti_lfa.protection")
        if ti_lfa_protection == "link":
            router_isis["isis_af_defaults"].append("fast-reroute ti-lfa mode link-protection")
        elif ti_lfa_protection == "node":
            router_isis["isis_af_defaults"].append("fast-reroute ti-lfa mode node-protection")

        # Overlay protocol
        if self.shared_utils.overlay_routing_protocol == "none":
            router_isis["redistribute_routes"] = [{"source_protocol": "connected"}]

        if self.shared_utils.underlay_sr is True:
            router_isis["advertise"] = {
                "passive_only": get(self._hostvars, "isis_advertise_passive_only", default=False),
            }
            # TODO - enabling IPv6 only in SR cases as per existing behavior
            # but this could probably be taken out
            if self.shared_utils.underlay_ipv6 is True:
                router_isis["address_family"].append("ipv6 unicast")
            router_isis["segment_routing_mpls"] = {"router_id": self.shared_utils.router_id, "enabled": True}

        return router_isis

    @cached_property
    def _isis_net(self) -> str | None:
        isis_system_id_prefix = get(self.shared_utils.switch_data_combined, "isis_system_id_prefix")
        if isis_system_id_prefix is not None:
            isis_area_id = get(self._hostvars, "isis_area_id", default="49.0001")
            if self.shared_utils.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.shared_utils.hostname}' and is required to set ISIS NET address using prefix")

            return f"{isis_area_id}.{isis_system_id_prefix}.{self.shared_utils.id:04d}.00"

        return None

    @cached_property
    def _is_type(self) -> str:
        default_is_type = get(self._hostvars, "isis_default_is_type", default="level-2")
        is_type = str(get(self.shared_utils.switch_data_combined, "is_type", default=default_is_type)).lower()
        if is_type not in ["level-1", "level-2", "level-1-2"]:
            is_type = "level-2"
        return is_type
