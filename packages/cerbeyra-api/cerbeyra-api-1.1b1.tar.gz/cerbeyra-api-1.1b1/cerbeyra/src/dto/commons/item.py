from dataclasses import dataclass, fields


@dataclass
class Item:

    def __init__(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items() if k in self.fields]

    @property
    def fields(self) -> list[str]:
        return [field.name for field in fields(self)]

    def get_field(self, field: str):
        return getattr(self, field, '')

    def check_field(self, field: str, value) -> bool:
        return getattr(self, field, '') == value
