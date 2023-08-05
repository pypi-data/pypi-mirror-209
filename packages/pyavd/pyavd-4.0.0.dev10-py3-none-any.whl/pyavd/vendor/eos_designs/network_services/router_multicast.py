from __future__ import annotations

from functools import cached_property

from pyavd.vendor.utils import get
from pyavd.vendor.eos_designs.network_services.utils import UtilsMixin


class RouterMulticastMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_multicast(self) -> dict | None:
        """
        return structured config for router_multicast

        Used to enable multicast routing on the VRF.
        """

        if not self.shared_utils.network_services_l3:
            return None

        vrfs = []
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                if get(vrf, "_evpn_l3_multicast_enabled"):
                    vrfs.append({"name": vrf["name"], "ipv4": {"routing": True}})

        if vrfs:
            return {"vrfs": vrfs}

        return None
