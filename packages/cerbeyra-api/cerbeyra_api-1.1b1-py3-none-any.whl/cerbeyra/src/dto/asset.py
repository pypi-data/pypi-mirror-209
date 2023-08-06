from dataclasses import dataclass
from cerbeyra.src.dto.commons.item import Item


@dataclass(kw_only=True)
class Asset(Item):
    asset_id: int
    asset_name: str
    target: list[str] | str
    perimeter: str
    type: str
    excluded: bool

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f'[{self.asset_id}] {self.asset_name}'


if __name__ == '__main__':
    print(Asset().fields)
