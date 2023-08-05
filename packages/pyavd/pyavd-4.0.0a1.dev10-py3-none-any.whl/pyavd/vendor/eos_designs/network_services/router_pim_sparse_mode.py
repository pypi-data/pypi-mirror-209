from __future__ import annotations

from functools import cached_property

from pyavd.vendor.utils import get
from pyavd.vendor.eos_designs.network_services.utils import UtilsMixin


class RouterPimSparseModeMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_pim_sparse_mode(self) -> dict | None:
        """
        return structured config for router_pim

        Used for to configure RPs on the VRF
        """

        if not self.shared_utils.network_services_l3:
            return None

        vrfs = []
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                if vrf_rps := get(vrf, "_pim_rp_addresses"):
                    vrfs.append(
                        {
                            "name": vrf["name"],
                            "ipv4": {
                                "rp_addresses": vrf_rps,
                            },
                        }
                    )

        if vrfs:
            return {"vrfs": vrfs}

        return None
