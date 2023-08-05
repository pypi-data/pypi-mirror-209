from extras.plugins import PluginConfig
from .version import __version__


class CiscoMaintenanceConfig(PluginConfig):
    name = "netbox_cisco_maintenance"
    verbose_name = "Cisco Support APIs"
    description = "Gathering device info using Cisco Support APIs"
    version = __version__
    author = "Willi Kubny"
    author_email = "willi.kubny@gmail.com"
    base_url = "cisco-maintenance"
    min_version = "3.5.0"
    required_settings = ["cisco_client_id", "cisco_client_secret"]
    default_settings = {"manufacturer": "Cisco"}


config = CiscoMaintenanceConfig
