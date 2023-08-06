from dataclasses import dataclass
from cerbeyra.src.dto.commons.item import Item


@dataclass(kw_only=True)
class WebHostVuln(Item):
    asset_id: int
    asset_name: str
    host_id: int
    host: str
    vuln_id: int
    vulnerability: str
    threat: str
    vuln_excluded: bool
    host_excluded: bool
    asset_excluded: bool
    last_detection: str
    first_detection: str = None
    label: str = None
    family: str = None
    description: str = None
    solution: str = None
    affected_url_count: int = None
    evidence: str = None
    attack: str = None
    param: str = None
    other: str = None
    affected_urls: list[str] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"<WebHostVuln host={self.host} threat={self.threat} vuln={self.vulnerability}>"
