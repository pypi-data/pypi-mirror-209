from dataclasses import dataclass
from enum import Enum
from cerbeyra.src.dto.commons.item import Item


class _ScanType(Enum):
    NETWORK = 'network'
    WEB = 'web'


@dataclass(kw_only=True)
class _ScanResult(Item):
    asset_id: int
    asset_name: str
    target: list
    type: str
    perimeter: str
    vulns: dict
    status: str
    start_at: str
    end_at: str
    probe_id: int = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"<ScanResult asset={self.asset_name} target={self.target} vuln={self.vulns}>"


class NetworkScanResult(_ScanResult):

    def __post_init__(self):
        if not self.type == _ScanType.NETWORK.value:
            raise TypeError()

    def __repr__(self):
        return f"<NetworkScanResult asset={self.asset_name} target={self.target} status={self.status} vuln={self.vulns}>"


class WebScanResult(_ScanResult):

    def __post_init__(self):
        if not self.type == _ScanType.WEB.value:
            raise TypeError()

    def __repr__(self):
        return f"<WebScanResult asset={self.asset_name} target={self.target} status={self.status} vuln={self.vulns}>"
