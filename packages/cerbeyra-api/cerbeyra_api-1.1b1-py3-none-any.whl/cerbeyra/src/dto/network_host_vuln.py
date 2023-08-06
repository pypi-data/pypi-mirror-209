from dataclasses import dataclass, fields
from cerbeyra.src.dto.commons.item import Item


@dataclass(kw_only=True)
class NetworkHostVuln(Item):
    asset_id: int
    asset_name: str
    host_id: int
    host: str
    port: str
    protocol: str
    vuln_id: int
    vulnerability: str
    threat: str
    cvss: float
    vuln_excluded: bool
    host_excluded: bool
    asset_excluded: bool
    last_detection: str
    first_detection: str = None
    host_label: str = None
    hostname: str = None
    family: str = None
    summary: str = None
    description: str = None
    solution: str = None
    insight: str = None
    impact: str = None
    affected: str = None
    references: list[str] = None
    cve: list[str] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"<NetworkHostVuln host={self.host} threat={self.threat} vuln={self.vulnerability}>"


