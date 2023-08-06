from dataclasses import dataclass
from cerbeyra.src.dto.commons.item import Item


@dataclass(kw_only=True)
class Host(Item):
    asset_id: int
    asset_name: str
    host_id: int
    host: str
    perimeter: str
    type: str
    host_excluded: str
    asset_excluded: str
    host_label: str = None
    index: str = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f'<Host [{self.host_id}] host={self.host}>'
